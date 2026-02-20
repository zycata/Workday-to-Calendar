from flask import Flask, request, send_file, jsonify, send_from_directory
from flask_cors import CORS
import io, os
import backend.converter as conv
from backend.hope import retrieve_quote

current_dir = os.path.dirname(os.path.abspath(__file__))

# This points to /app/frontend/dist
dist_path = os.path.join(current_dir, "..", "frontend", "dist")

app = Flask(__name__, static_folder=dist_path, static_url_path='/')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if not app.static_folder:
        return "Static folder not configured", 500
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/get-word')
def get_word():
    return jsonify({"word": retrieve_quote()})

@app.route('/convert-ics', methods=['POST', 'GET'])
def convert_ics():
    if 'file' not in request.files:
        return "Missing file part", 400
        
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file", 400
    try:
        cal = conv.convert_xlsx_to_ics(file)
        return send_file(
            io.BytesIO(cal),
            mimetype='text/calendar',
            as_attachment=True,
            download_name='schedule.ics'
        )
    except TypeError as e:
        return "Error parsing excel file", 400
    except ValueError as e:
        return "Error converting excel file to ics", 400
    except Exception as e:
        return "Unknown error occured with server", 500

@app.errorhandler(404)
def not_found(e):
    if not app.static_folder:
        return "Static folder not configured", 500
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    # This is exactly what you wanted
    app.run(host="0.0.0.0", debug=True, port=5100)
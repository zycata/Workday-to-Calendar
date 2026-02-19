from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import io
import src.converter as conv

import random

app = Flask(__name__)
CORS(app)
@app.route('/get-word')
def get_word():
    return jsonify({"word": random.choice(["Apple", "Banana", "67"])})

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


if __name__ == "__main__":
    # This is exactly what you wanted
    app.run(host="0.0.0.0", debug=True, port=5100)
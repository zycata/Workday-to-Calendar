from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import io
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
    file_content = file.read()

    return send_file(
        io.BytesIO(file_content),
        mimetype='text/calendar',
        as_attachment=True,
        download_name='converted.ics'
    )

if __name__ == "__main__":
    # This is exactly what you wanted
    app.run(host="0.0.0.0", debug=True, port=5100)
from flask import Flask, request, send_file
import os
from u2net_test.u2net_infer import remove
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No image uploaded", 400
    img = request.files['image']
    filename = secure_filename(img.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(RESULT_FOLDER, filename.replace('.', '_nobg.'))
    img.save(input_path)
    remove(input_path, output_path)
    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
from flask import Flask, render_template, request, redirect, url_for
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            img = Image.open(file.stream)
            # Here you can add your model prediction code
            return render_template('display.html', img=img.show())
    return redirect(url_for('index'))

@app.route('/capture', methods=['POST'])
def capture_image():
    img_data = request.form.get('imageBase64')
    if img_data:
        img_data = img_data.split(",")[1]  # Remove the "data:image/png;base64," part
        image = Image.open(BytesIO(base64.b64decode(img_data)))
        # Here you can add your model prediction code
        return render_template('display.html', img=image.show())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

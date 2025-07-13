from flask import Flask, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')  # phục vụ file HTML tĩnh

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form.get("text", "")
    color = request.form.get("color", "#000000")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=6,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color="white")

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype="image/png", as_attachment=True, download_name="ma_qr.png")

if __name__ == '__main__':
    app.run(debug=True)
from fileinput import filename
from flask import Flask, request, send_file, render_template
import mimetypes

app = Flask(__name__)

formatList = {
    'jpeg': 'jpeg',
    'jpg': 'jpeg',
    'png': 'png',
    'gif': 'gif',
    'tif': 'tiff',
}


@app.route('/process-image', methods=["POST", "GET"])
def process_image():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        # Saving the received file as temp.*
        f = request.files["image"]
        file_name = f.filename
        dot_index = file_name.rfind('.')
        file_format = formatList[file_name[dot_index+1:]]
        file_name = f"temp.{file_format}"
        mime = mimetypes.guess_type(file_name)[0]
        f.save(file_name)

        # Read the temp.* image here and overwrite the manuplated image to temp.*

        return send_file(file_name, mimetype=mime)


if __name__ == "__main__":
    app.run(debug=True)

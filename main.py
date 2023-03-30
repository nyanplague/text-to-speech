from flask import Flask, render_template, redirect, url_for, flash, request, g, abort, send_file
from flask_bootstrap import Bootstrap
from pdf_to_text import Reader
from text_to_speech import Converter

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/success', methods = ['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        reader = Reader(f.filename)
        text = reader.read()
        converter = Converter()
        audio = converter.convert(text)

        return render_template("success.html", name = f.filename, audio = audio)


@app.route('/get_file')
def returnAudioFile():
    path_to_audio_file = request.args["file_path"]
    return send_file(
       path_to_audio_file,
       mimetype="audio/mp3",
       as_attachment=True
    )


if __name__ == '__main__':
    app.run(debug=True)
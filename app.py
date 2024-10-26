from flask import Flask, render_template

from helpers.bot import init_bot

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/download')
def download():
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True)
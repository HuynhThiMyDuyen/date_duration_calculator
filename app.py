from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from datetime import datetime
import webbrowser

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def form():
    return render_template("form.html")


@app.route("/data", methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        start_str = str(request.form.get('starttime'))
        end_str = str(request.form.get('endtime'))
        start = datetime(int(start_str[:4]), int(start_str[5:7]), int(start_str[8:10]), int(start_str[11:13]), int(start_str[14:16]))
        end = datetime(int(end_str[:4]), int(end_str[5:7]), int(end_str[8:10]), int(end_str[11:13]), int(end_str[14:16]))
        distance = end - start

        return render_template('data.html', start=start, end=end, distance=distance)


if __name__ == "__main__":
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run() 
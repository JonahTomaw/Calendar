from flask import Flask, render_template, request
from alert import check_alerts
from create_event import event_create

app = Flask(__name__)

@app.route("/")
def home():

    events = check_alerts()

    return render_template("index.html", events=events)


@app.route("/create", methods=["POST"])
def create():
    
    title = request.form["title"]
    start = request.form["start"]
    end = request.form["end"]
    time_before = request.form["time_before"]

    event_create(title, start, end, time_before)

    return "Event Received"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
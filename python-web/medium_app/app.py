from flask import Flask, render_template
from jinja2 import Template


import requests
request = requests.get("http://api.open-notify.org/astros.json")
#print(request.text)
print(request.status_code)
request_json = request.json()

nasaRequest = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
#requests.get("https://api.nasa.gov/planetary/apod?api_key=rseity3hLhv4OPBf9MdUszCxBY24wi1oIfuXYbQN")
nasaRequest_json = nasaRequest.json()
nasaPicOfDayURL = nasaRequest_json["url"]

spaceList = []
for i in request_json["people"]:
     spaceList.append(i["name"])

craftList = []
for i in request_json["people"]:
     craftList.append(i["craft"])


astronautDeets = []
astronautDeets.append(spaceList)
astronautDeets.append(craftList)

print(astronautDeets)


numInSpace = request_json["number"]

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("index.html", 
    numInSpace = numInSpace, 
    spaceList = spaceList,
    craftList = craftList,
    astronautDeets = astronautDeets,
    nasaPicOfDayURL = nasaPicOfDayURL)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.errorhandler(404)
def error_page(i):
    return render_template("error.html")


app.run(debug=True)

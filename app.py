from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return "Skill Camp!"

@app.route("/create")
def create():
    return "Make a new thing!"

@app.route("/<int:uid>/view")
def view(uid):
    return "Look at %d" % (uid,)

@app.route("/<int:uid>/edit")
def edit(uid):
    return "I'm editing %d" % (uid,)

if __name__ == "__main__":
    app.run()

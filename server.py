from flask import Flask #from tool file import class / function/ variable
import json
from about import me

app = Flask(__name__) # create a instance of Flask class. needs a name inside ().

### web server ###
@app.get("/")
def home():
    return "hello world from a flask server"

@app.get("/test")
def test():
    return "this is a test page"


########################################
########     API SERVER ################
########################################
#application programming interface- a program designed to be consumed by the other service
# data back and forth

@app.get("/api/version")
def version():
    return json.dumps("1.0")

@app.get("/api/about")
def about():
    return json.dumps(me)

# start the server
app.run(debug=True)   #do not use in production

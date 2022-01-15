from crypt import methods
from flask import Flask, request
from users import create_user
import json

app = Flask(__name__)

@app.route("/signup/", methods=["POST"])
def signup():
    username = request.form["username"]
    email = request.form["email"]
    user_password = request.form["password"]
    status = create_user(username, user_password,email)
    return json.dumps({"status":status})


@app.route("/", methods=["GET"])
def hello_world():
    
    return json.dumps({"status":"ok"})
    
# if __name__ == "__main__":
#   app.run(host="192.168.22.157", port=8080, debug=True)

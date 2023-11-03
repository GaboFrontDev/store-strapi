import subprocess
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

pullCommand = ["make", "pull"]
buildCommand = ["make", "build"]
tagCommand = ["make", "tag"]
pushCommand = ["make", "push"]

@app.route("/", methods=["POST"])
def build():
    print("Deploy request init")
    try:
        print("building")
        p1 = subprocess.Popen(buildCommand, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(tagCommand, stdin=p1.stdoutl,  stdout=subprocess.PIPE)
        subprocess.Popen(pushCommand, stdin=p2.stdoutl, stdout=subprocess.PIPE)
    except Exception as e:
        print(e)
        return jsonify({"msg": "Deploy failed"}), 500
    return jsonify({"msg": "Deployed"}), 200


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5510, debug=True)

import subprocess
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

pullCommand = ["make", "pull"]
buildCommand = ["make", "build"]
tagCommand = ["make", "tag"]
pushCommand = ["make", "push"]

commands = [
  pullCommand,
  buildCommand,
  tagCommand,
  pushCommand,
]

@app.route("/", methods=["POST"])
def build():
    print("building request init")
    try:
        print("building")
        p = None
        for cmd in commands:
            if p:
              p = subprocess.Popen(cmd, stdin=p.stdoutl, stdout=subprocess.PIPE)
            else:
              p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    except Exception as e:
        print(e)
        return jsonify({"msg": "Deploy failed"}), 500
    return jsonify({"msg": "Deployed"}), 200


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5510, debug=False)

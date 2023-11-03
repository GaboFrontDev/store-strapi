import subprocess
from flask import Flask, jsonify, request


app = Flask(__name__)

pullCommand = ["make", "pull"]
buildCommand = ["make", "build"]
tagCommand = ["make", "tag"]
pushCommand = ["make", "push"]

commands = [
  "make pull",
  "make build",
  "make tag",
  "make push",
]

@app.route("/", methods=["POST"])
def build():
    data = request.get_json()
    print("building request init")
    print(data['repository']['ssh_url'])
    try:
        print("building")
        for cmd in commands:
          process = subprocess.Popen(cmd, shell=True)
          process.wait()
    except Exception as e:
        print(e)
        return jsonify({"msg": "Deploy failed"}), 500
    return jsonify({"msg": "Deployed"}), 200


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5510, debug=False)

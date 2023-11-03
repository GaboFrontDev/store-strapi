import subprocess
from flask import Flask, jsonify, request
import os


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
    repo_url = data['repository']['ssh_url']
    directory = data['repository']['name']
    try:
      if not os.path.exists(directory):
        print("cloning")
        process = subprocess.Popen("git clone {}".format(repo_url), shell=True)
        process.wait()

      print("building")
      os.chdir(directory)
      for cmd in commands:
        process = subprocess.Popen(cmd , shell=True)
        process.wait()
      os.chdir("..")
      return jsonify({"msg": "Deployed"}), 200
    except FileNotFoundError:
      print(f"La carpeta '{directory}' no existe.")
    except Exception as e:
      print(f"Ocurrió un error: {e}")
    os.chdir("..")
    return jsonify({"msg": "Deploy failed"}), 500


if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5510, debug=False)


import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        command = request.form.get("command")
        output = run_command(command)
        return render_template("index.html", output=output)
    return render_template("index.html", output=None)

def run_command(command):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

if __name__ == "__main__":
    app.run(debug=True, port=8080)

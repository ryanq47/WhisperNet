from flask import Flask, send_file, abort
import os

app = Flask(__name__)

def fileserver_start(ip="0.0.0.0",port=80):

    app.run(port=port, host=ip)
@app.route('/<path:path>')
def serve_file(path):
    # Get the absolute path to the file
    file_path = os.path.abspath(os.path.join('httpserver/static-serve', path))

    # Make sure the file exists
    if not os.path.exists(file_path):
        abort(403)

    # Serve the file
    return send_file(file_path)


if __name__ == "__main__":
    app.run()
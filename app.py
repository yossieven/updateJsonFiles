import json

from flask import Flask, render_template, request

from jsonfilemanager import get_file, update_file

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def update_json_file():
    if request.method == 'POST':
        result = update_file(request.form.get('hidden-file'), request.form.get('content'))
        return render_template('index.html', **result)
    else:
        filename = request.args.get("filename")
        result = get_file(filename)
        return render_template('index.html', **result)


if __name__ == '__main__':
    app.run()

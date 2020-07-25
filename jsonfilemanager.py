import json

from json.decoder import JSONDecodeError


def get_file(filename):
    if filename is None:
        return {}
    elif filename == '':
        return {'text': ["You must choose a file first!"]}
    else:
        try:
            file = open(filename, 'r')
            data = json.load(file)
            dumps = json.dumps(data, indent=4)
            lines = dumps.split("\n")
            file.close()
            return {'text': lines, 'filename': filename}
        except JSONDecodeError as e:
            file = open(filename, 'r')
            lines = file.read().split('\n')
            file.close()
            return {'text': lines, 'filename': filename}


def update_file(filename, content):
    if filename is None:
        return {}
    elif filename == '':
        return {'text': ["You must choose a file first!"]}
    else:
        final = content.replace("\r\n", "\n")
        file = open(filename, 'w')
        file.write(final)
        file.close()
        return {'text': ['Success!']}

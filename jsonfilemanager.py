import json

from json.decoder import JSONDecodeError


def get_file(filename):
    if filename is None:
        return {}
    elif filename == '':
        return {'text': ["You must choose a file first!"], 'contentColor': 'black'}
    else:
        try:
            file = open(filename, 'r')
            data = json.load(file)
            dumps = json.dumps(data, indent=4)
            lines = dumps.split("\n")
            file.close()
            return {'text': lines, 'filename': filename, 'contentColor': 'black'}
        except JSONDecodeError as e:
            file = open(filename, 'r')
            lines = []
            lines.append('JSON file is not well formed:')
            lines.append(e.args[0])
            lines.append('delete these lines before saving JSON file again!')
            file_lines = file.read().split('\n')
            for line in file_lines:
                lines.append(line)

            file.close()
            return {'text': lines, 'filename': filename, 'contentColor': 'red'}


def update_file(filename, content):
    if filename is None:
        return {}
    elif filename == '':
        return {'text': ["You must choose a file first!"], 'contentColor': 'black'}
    else:
        final = content.replace("\r\n", "\n")
        file = open(filename, 'w')
        file.write(final)
        file.close()
        return {'text': ['Success!'], 'contentColor': 'black'}

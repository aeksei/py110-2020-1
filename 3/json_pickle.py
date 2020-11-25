import json
import pickle


def to_json_string(obj, indent=4):
    print(json.dumps(obj, indent=indent))


def to_pickle_file(obj, filename):
    # todo endwith for filename
    with open(filename, 'wb') as pickle_file:
        pickle.dump(obj, pickle_file)


def to_json_file(obj, filename, indent=1, separators=None):
    # todo найти в лекции аргумент, чтобы записать всё в одну строку
    if not filename.endswith('.json'):
        filename += '.json'
    with open(filename, 'w') as f:
        json.dump(obj, f, indent=indent, separators=separators)


if __name__ == '__main__':
    dict_json = {
        1: 1,
        "2": 5,
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
    }
    # to_json_string(dict_json)

    dict_pickle = {  # todo to_json_string(dict_pickle)
        1: 1,
        "2": 5,
        (5, 7): "test",
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
        "func": to_json_string
    }
    # to_pickle_file(dict_json, 'dump_tmp.pickle')
    # to_pickle_file(dict_pickle, 'dump_tmp.pickle')

    to_json_file(dict_json, 'tmp_json_indent_0', indent=0, separators='')
    to_json_file(dict_json, 'tmp_indent_4.json', indent=4)

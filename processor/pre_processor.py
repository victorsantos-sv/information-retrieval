import string
from unidecode import unidecode


def remove_duplicated_words(data):
    return list(dict.fromkeys(data))


def remove_punctuation(data):
    for punctuation in string.punctuation:
        data = data.replace(punctuation, '')

    return data


def sort(data):
    data.sort()

    return data


def unidecode_data(data):
    _unidecode_terms = list()

    for term in data:
        unidecode_str = unidecode(term)
        _unidecode_terms.append(unidecode_str)

    return sort(_unidecode_terms)


def process_data(data):
    _data_lowercase = data.lower()
    _data_punctuation = remove_punctuation(_data_lowercase)
    _data_split = _data_punctuation.split()
    _unidecode_terms = unidecode_data(_data_split)

    return _unidecode_terms

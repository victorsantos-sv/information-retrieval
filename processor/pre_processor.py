import string
import re
from unidecode import unidecode
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer


def remove_duplicated_words(data):
    return list(dict.fromkeys(data))


def _remove_punctuation(data):
    for punctuation in string.punctuation:
        data = data.replace(punctuation, '')

    return data


def _sort(data):
    data.sort()

    return data


def remove_numbers(data):
    _number_pattern = r'[0-9]'

    return re.sub(_number_pattern, '', data)


def _unidecode_data(data):
    _unidecode_terms = list()

    for term in data:
        unidecode_str = unidecode(term)
        _unidecode_terms.append(unidecode_str)

    return _sort(_unidecode_terms)


def _remove_stopwords(data):
    _stopwords = set(stopwords.words('portuguese'))

    tokens = word_tokenize(data)

    return [word for word in tokens if not word.lower() in _stopwords]


def _stem_data(data):
    _stemmer = RSLPStemmer()
    _stemmed_data = list()

    for word in data:
        _stemmed = _stemmer.stem(word)
        _stemmed_data.append(_stemmed)

    return _stemmed_data


def process_data(data):
    _data_lowercase = data.lower()
    _data_without_number = remove_numbers(_data_lowercase)
    _data_punctuation = _remove_punctuation(_data_without_number)
    _data_without_stopwords = _remove_stopwords(_data_punctuation)
    _unidecode_terms = _unidecode_data(_data_without_stopwords)
    _stemmed_data = _stem_data(_unidecode_terms)

    return _stemmed_data

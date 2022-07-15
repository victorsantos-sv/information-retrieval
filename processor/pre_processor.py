import string
import re
from unidecode import unidecode
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer


def remove_duplicated_words(data):
    return list(dict.fromkeys(data))


def remove_punctuation(data):
    for punctuation in string.punctuation:
        data = data.replace(punctuation, '')

    return data


def sort(data):
    data.sort()

    return data


def remove_numbers(data):
    number_pattern = r'[0-9]'

    return re.sub(number_pattern, '', data)


def unidecode_data(data):
    unidecode_terms = list()

    for term in data:
        unidecode_str = unidecode(term)
        unidecode_terms.append(unidecode_str)

    return sort(unidecode_terms)


def remove_stopwords(data):
    portuguese_stopwords = set(stopwords.words('portuguese'))

    tokens = word_tokenize(data)

    return [word for word in tokens if not word.lower() in portuguese_stopwords]


def stem_data(data):
    stemmer = RSLPStemmer()
    stemmed_data = list()

    for word in data:
        _stemmed = stemmer.stem(word)
        stemmed_data.append(_stemmed)

    return stemmed_data


def process_data(data):
    data_lowercase = data.lower()
    data_without_number = remove_numbers(data_lowercase)
    data_punctuation = remove_punctuation(data_without_number)
    data_without_stopwords = remove_stopwords(data_punctuation)
    unidecode_terms = unidecode_data(data_without_stopwords)
    stemmed_data = stem_data(unidecode_terms)

    return stemmed_data

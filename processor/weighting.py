from math import log as logarithm
from processor.pre_processor import remove_duplicated_words


def calculate_tf(tf_frequency):
    return logarithm(tf_frequency, 2) + 1


def calculate_idf(idf_frequency, collection_size):
    for term, frequency in idf_frequency.items():
        if frequency == 0:
            idf = 0
        else:
            idf = logarithm((collection_size / frequency), 2)
        idf_frequency[term] = idf

    return idf_frequency


def calculate_tf_idf(tf, idf):
    return tf * idf


def count_idf_frequency(documents, vocabulary):
    term_frequency = dict()

    for document in documents:
        for term in remove_duplicated_words(document.processed_terms):
            word = term

            if word in vocabulary and word in term_frequency:
                term_frequency[word] += 1
            elif word in vocabulary and word not in term_frequency:
                term_frequency[word] = 1
            else:
                term_frequency[word] = 0

    return dict(sorted(term_frequency.items(), key=lambda item: item[0]))

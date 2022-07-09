from math import log as logarithm


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
    tf_idf = "{:.3f}".format(tf * idf)

    return tf_idf


def count_idf_frequency(terms, vocabulary):
    term_frequency = dict()

    for term in terms:
        word = term.word

        if word in vocabulary and word in term_frequency:
            term_frequency[word] += 1
        elif word in vocabulary and word not in term_frequency:
            term_frequency[word] = 1
        else:
            term_frequency[word] = 0
        # for unique_term in document.unique_terms:

    return dict(sorted(term_frequency.items(), key=lambda item: item[0]))

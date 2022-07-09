import sys
from helper.file_helper import read_file, open_file, close_file, write_in_file
from helper.model_helper import get_terms, get_documents
from processor.pre_processor import remove_duplicated_words, process_data
from processor.weighting import calculate_idf, count_idf_frequency, calculate_tf_idf
from model.Model import Document


def _get_tf_idf():
    vocabulary = read_file(sys.argv[2])

    files = read_file(sys.argv[1])
    documents = get_documents(files)
    terms = get_terms(documents)
    idf_frequency = count_idf_frequency(terms, vocabulary)

    idf = calculate_idf(idf_frequency, len(documents))

    for term in terms:
        _tf = term.tf
        term.idf = idf[term.word]
        _idf = idf[term.word]
        term.tf_idf = calculate_tf_idf(_tf, _idf)

    return terms


def create_tf_idf():
    terms = _get_tf_idf()

    for term in terms:
        print(f'Document: {term.document.document_name} --------- Term: {term.word} ---------- TF-IDF: {term.tf_idf}\n')


def get_bow():
    files = read_file(sys.argv[1])
    documents = get_documents(files)
    vocabulary = list()

    for document in documents:
        for content in document.processed_terms:
            vocabulary.append(content)

    vocabulary.sort()

    vocabulary_file = open_file('vocabulary.txt', 'w')

    vocabulary = remove_duplicated_words(vocabulary)

    for word in vocabulary:
        write_in_file(vocabulary_file, word + '\n')

    close_file(vocabulary_file)

    bag_of_words = list()

    for document in documents:
        internal_file_bag = list()

        for word in vocabulary:
            if word in document.unique_terms:
                internal_file_bag.append(1)
            else:
                internal_file_bag.append(0)

        bag_of_words.append({'FILE': document.document_name, 'BoW': internal_file_bag})

    for file_bag in bag_of_words:
        print(file_bag)


def get_cosine_similarity():
    files = read_file(sys.argv[1])
    vocabulary = read_file(sys.argv[2])
    query = sys.argv[3]
    terms = _get_tf_idf()
    query_as_document = list()
    query_as_document.append(Document('query', query))

    query_terms = get_terms(query_as_document)

    for query_term in query_terms:
        print(query_term.tf)

    # print(query_terms)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_bow()
    elif len(sys.argv) == 3:
        create_tf_idf()
    else:
        get_cosine_similarity()

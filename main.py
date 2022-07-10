import sys
from helper.file_helper import read_file, open_file, close_file, write_in_file
from helper.model_helper import get_terms, get_documents, to_list
from processor.pre_processor import remove_duplicated_words
from processor.weighting import calculate_idf, count_idf_frequency, calculate_tf_idf
from processor.cosine import calculate_norm, calculate_inner_product, calculate_cosine_similarity
from model.Model import Document


def _get_tf_idf():
    vocabulary = read_file(sys.argv[2])

    files = read_file(sys.argv[1])
    documents = get_documents(files)
    idf_frequency = count_idf_frequency(documents, vocabulary)
    idf = calculate_idf(idf_frequency, len(documents))

    for document in documents:
        for term in document.unique_terms:
            _tf = term.tf
            term.idf = idf[term.word]
            _idf = idf[term.word]
            term.tf_idf = calculate_tf_idf(_tf, _idf)

    return documents


def get_tf_idf():
    documents = _get_tf_idf()

    for document in documents:
        for term in document.unique_terms:
            _tf_idf = "{:.3f}".format(term.tf_idf)

            print(f'Document: {document.document_name} --------- Term: {term.word} ---------- TF-IDF: {_tf_idf}\n')


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
            if word in remove_duplicated_words(document.processed_terms):
                internal_file_bag.append(1)
            else:
                internal_file_bag.append(0)

        bag_of_words.append({'FILE': document.document_name, 'BoW': internal_file_bag})

    for file_bag in bag_of_words:
        print(file_bag)


def get_cosine_similarity():
    query = sys.argv[3]
    documents = _get_tf_idf()
    query_as_document = Document('query', query)
    get_terms(to_list(query_as_document))

    calculate_inner_product(documents, query_as_document)
    calculate_norm(documents)
    calculate_norm(to_list(query_as_document))

    ordered_by_cosine = calculate_cosine_similarity(documents, query_as_document)

    for document in ordered_by_cosine:
        _cosine_similarity = '{:.3f}'.format(document.cosine_similarity)
        print(f'Documento: {document.document_name} - Grau de similaridade = {_cosine_similarity}')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_bow()
    elif len(sys.argv) == 3:
        get_tf_idf()
    else:
        get_cosine_similarity()

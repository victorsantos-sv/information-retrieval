import sys
from helper.file_helper import read_file, open_file, close_file, write_in_file
from helper.model_helper import get_terms, get_documents, to_list
from processor.pre_processor import remove_duplicated_words
from processor.weighting import calculate_idf, count_idf_frequency, calculate_tf_idf
from processor.cosine import calculate_norm
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


def create_tf_idf():
    documents = _get_tf_idf()

    for document in documents:
        for term in document.unique_terms:
            print(f'Document: {document.document_name} --------- Term: {term.word} ---------- TF-IDF: {term.tf_idf}\n')


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
    documents = _get_tf_idf()
    query_as_document = Document('query', query)
    query_documents = get_terms(to_list(query_as_document))
    query_terms = query_as_document.unique_terms
    inner_product = dict()
    terms = list()

    for document in documents:
        for term in document.unique_terms:
            terms.append(term)

    # for query_document in query_documents:
    #     for query_term in query_document.unique_terms:
    #         term_index = [document_term.word for document_term in terms].index(query_term.word)
    #
    #         query_term.idf = terms[term_index].idf
    #         query_term.tf_idf = calculate_tf_idf(query_term.tf, query_term.idf)

    for document in documents:
        _inner_product_sum = 0
        inner_product = dict()
        for term in document.unique_terms:
            try:
                query_term_index = [query_term.word for query_term in query_terms].index(term.word)

                _idf = term.idf

                query_terms[query_term_index].idf = _idf
                query_terms[query_term_index].tf_idf = calculate_tf_idf(query_terms[query_term_index].tf, _idf)

                inner_product[term.word] = float(term.tf_idf) * float(query_terms[query_term_index].tf_idf)
            except:
                pass

        for value in inner_product.values():
            _inner_product_sum += value

        document.inner_product = _inner_product_sum

    # for query_document in query_documents:
    #     for query_term in query_document.unique_terms:
    #         query_term.tf_idf = calculate_tf_idf(query_term.tf, query_term.idf)
    #
    #         term_index = [document_term.word for document_term in terms].index(query_term.word)
    #
    #         inner_product[query_term.word] = float(query_term.tf_idf) * float(terms[term_index].tf_idf)

    calculate_norm(terms)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        get_bow()
    elif len(sys.argv) == 3:
        create_tf_idf()
    else:
        get_cosine_similarity()

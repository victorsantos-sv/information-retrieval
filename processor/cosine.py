from math import sqrt, pow
from processor.weighting import calculate_tf_idf


def calculate_inner_product(documents, query):
    query_terms = query.unique_terms

    for document in documents:
        inner_product_sum = 0
        inner_product = dict()
        for term in document.unique_terms:
            try:
                query_term_index = [query_term.word for query_term in query_terms].index(term.word)

                idf = term.idf

                query_terms[query_term_index].idf = idf
                query_terms[query_term_index].tf_idf = calculate_tf_idf(query_terms[query_term_index].tf, idf)

                inner_product[term.word] = term.tf_idf * query_terms[query_term_index].tf_idf
            except:
                pass

        for value in inner_product.values():
            inner_product_sum += value

        document.inner_product = inner_product_sum


def calculate_norm(documents):
    for document in documents:
        summation = 0

        for term in document.unique_terms:
            if term.tf_idf is None:
                term.tf_idf = 0.0
            if term.idf is None:
                term.idf = 0.0
            summation += pow(term.tf_idf, 2)

        document.norm = sqrt(summation)


def calculate_cosine_similarity(documents, query):
    for document in documents:
        cosine_similarity = 0.0

        if query.norm != 0 and document.norm != 0:
            cosine_similarity = document.inner_product / (document.norm * query.norm)

        document.cosine_similarity = cosine_similarity

    return sorted(documents, key=lambda doc: doc.cosine_similarity, reverse=True)

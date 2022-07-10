from processor.weighting import calculate_tf
from processor.pre_processor import remove_duplicated_words, process_data


class Term:
    def __init__(self, word, frequency):
        self.tf_idf = None
        self.idf = None
        self.tf = None
        self.word = word
        self.frequency = frequency

        self.tf = calculate_tf(self.frequency)


class Document:
    def __init__(self, document_name="", content=""):
        self.processed_terms = None
        self.norm = None
        self.unique_terms = None
        self.inner_product = None
        self.cosine_similarity = None
        self.document_name = document_name
        self.content = content

        self.processed_terms = process_data(self.content)

    def populate_terms(self, terms):
        self.unique_terms = remove_duplicated_words(terms)

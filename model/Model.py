from processor.weighting import calculate_tf
from processor.pre_processor import remove_duplicated_words, process_data


class Term:
    def __init__(self, word, frequency):
        self.tf_idf = None
        self.idf = None
        self.tf = None
        self.document = None
        self.word = word
        self.frequency = frequency

        self.tf = calculate_tf(self.frequency)

    def calculate_norm(self):
        print(self.tf_idf)


class Document:
    def __init__(self, document_name="", content=""):
        self.processed_terms = None
        self.document_name = document_name
        self.content = content
        self.norm = None

        self.processed_terms = process_data(self.content)
        self.unique_terms = remove_duplicated_words(self.processed_terms)

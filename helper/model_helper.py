from model.Model import Document, Term


def get_documents(files):
    documents = list()

    for file in files:
        documents.append(Document(file['name'], file['content']))

    return documents


def get_terms(documents):
    _term_list = list()

    for document in documents:
        _term_frequency = dict()

        for word in document.processed_terms:
            if word in _term_frequency:
                _term_frequency[word] += 1
            else:
                _term_frequency[word] = 1

        for word, frequency in _term_frequency.items():
            term = Term(word, frequency)
            term.document = document
            _term_list.append(term)

    return _term_list

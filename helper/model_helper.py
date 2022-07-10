from model.Model import Document, Term


def get_documents(files):
    documents = list()

    for file in files:
        documents.append(Document(file['name'], file['content']))

    documents = get_terms(documents)

    return documents


def get_terms(documents):
    _term_list = None

    for document in documents:
        _term_list = list()
        _term_frequency = dict()

        for word in document.processed_terms:
            if word in _term_frequency:
                _term_frequency[word] += 1
            else:
                _term_frequency[word] = 1

        for word, frequency in _term_frequency.items():
            term = Term(word, frequency)
            _term_list.append(term)

        document.populate_terms(_term_list)

    return documents


def to_list(model):
    object_list = list()
    object_list.append(model)

    return object_list

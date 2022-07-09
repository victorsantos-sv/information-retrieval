import os


def read_file(path):
    if os.path.isdir(path):
        documents = list()

        for file_name in sorted(os.listdir(path)):
            document_file = open_file(path + '/' + file_name, 'r')
            file_content = document_file.read().lower()
            document_file.close()

            documents.append({'name': file_name, 'content': file_content})

        return documents

    else:
        vocabulary_content = open_file(path, 'r')

        return vocabulary_content.read().lower().split()


def open_file(path, mode):
    file_context = None

    if mode == 'r':
        if os.path.exists(path):
            file_context = open(path, mode)
    else:
        file_context = open(path, mode)

    return file_context


def close_file(file_context):
    file_context.close()


def write_in_file(file_context, content):
    file_context.write(content)

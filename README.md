# Information Retrieval using Vector Spaces Model

## This code was created for a college project.
### The project has 3 options at the moment
- Create a bag of words based on a list of documents.
- Calculate the TF-IDF Weighting.
- Return a list of documents based on a query.

### Before running the project, you need to install some dependencies for pre-processing the documents.
- NLTK
- Unidecode

### To install the dependencies, simply run the command
```
$ pip3 install -r requirements.txt
```

### After installing it, you need to download the nltk packages
- start python on terminal and then run the following commands
```
  >>> import nltk
  
  >>> nltk.download('stopwords')
  >>> nltk.download('rslp')
```

### Now you can start the code.
- For the first option, you need to pass the documents folder through command line
```
$ python3 main.py ./documents/anthems
```

- For the second option, you need to pass the documents folder with the vocabulary file, which was created at the first step, also throug command line
```
$ python3 main.py ./documents/anthems ./vocabulary.txt
```

- And for the third option, you need to send your query alongside the documents folder and the vocabulary file
```
$ python3 main.py ./documents/anthems ./vocabulary.txt "paulista tricolor"
```

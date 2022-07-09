import string
import sys
import os
from unidecode import unidecode
from math import log

class Term:
    def __init__(self, term, frequency):
        self.term = term
        self.frequency = frequency

        self.calculateTF()

    def calculateTF(self):
        self.tf = log(self.frequency, 2) + 1
    
    def calculateTFIDF(self, idf, doc):
        self.tfIdf = "{:.4f}".format(self.tf * idf)

        print(f'Document: {doc} --------- Term: {self.term} ---------- TF-IDF: {self.tfIdf}\n')

class Document:
    def __init__(self, documentName="", content=""):
        self.documentName = documentName
        self.content = content
        self.terms = list()

        self.processData()
        self.uniqueTerms = removeDuplicatedWords(self.processedTerms)
        self.countTFFrequency()
    
    def countTFFrequency(self):
        termFrequency = dict()

        for term in self.processedTerms:
            if term in termFrequency:
                termFrequency[term] += 1
            else:
                termFrequency[term] = 1
        
        for term, frequency in termFrequency.items():
            self.terms.append(Term(term, frequency))

    def processData(self):
        unidecodedContent = list()

        for punctuation in string.punctuation:
            self.content = self.content.replace(punctuation, "")
        
        self.content = self.content.split()
        
        for term in self.content:
            unicodeStr = unidecode(term)
            unidecodedContent.append(unicodeStr)

        unidecodedContent.sort()

        self.processedTerms = unidecodedContent

def countIDFFrequency(documents, vocabulary):
    termFrequency = dict()

    for document in documents:
        for term in document.uniqueTerms:
            if term in vocabulary and term in termFrequency:
                termFrequency[term] += 1
            elif term in vocabulary and term not in termFrequency:
                termFrequency[term] = 1
            else:
                termFrequency[term] = 0
    
    return dict(sorted(termFrequency.items(), key=lambda term: term[0]))

def calculateIDF(idfFrequency, collectionSize):
    for term, frequency in idfFrequency.items():
        if (frequency == 0):
            idf = 0
        else:
            idf = log((collectionSize / frequency), 2)
        idfFrequency[term] = idf
    
    return idfFrequency

def removeDuplicatedWords(rawTerms):
    return list(dict.fromkeys(rawTerms))

def readDocuments():
    directory = sys.argv[1]

    documents = list()

    for fileName in sorted(os.listdir(directory)):
        documentFile = open(directory + '/' + fileName, 'r')
        fileContent = documentFile.read().lower()
        documentFile.close()
        
        documents.append(Document(fileName, fileContent))
    
    return documents

def readVocabulary():
    vocabularyFileName = sys.argv[2]

    vocabularyFile = open(vocabularyFileName, 'r')

    return vocabularyFile.read().lower().split()

def createTFIDF():
    vocabulary = readVocabulary()

    documents = readDocuments()
    print(len(documents))
    idfFrequency = countIDFFrequency(documents, vocabulary)
    
    idf = calculateIDF(idfFrequency, len(documents))

    for document in documents:
        for term in document.terms:
            if term.term in idf.keys():
                term.calculateTFIDF(idf[term.term], document.documentName)

def createBoW():
    documents = readDocuments()

    vocabulary = list()

    for document in documents:
        for content in document.processedTerms:
            vocabulary.append(content)
    
    vocabulary.sort()

    vocabularyFile = open('vocabulary.txt', 'w')

    vocabulary = removeDuplicatedWords(vocabulary)

    for word in vocabulary:
        vocabularyFile.write(word + '\n')

    vocabularyFile.close()

    bagOfWords = list()

    for document in documents:
        internalFileBag = list()

        for word in vocabulary:
            if (word in document.uniqueTerms):
                internalFileBag.append(1)
            else:
                internalFileBag.append(0)
        
        bagOfWords.append({'FILE': document.documentName, 'BoW': internalFileBag})

    print(bagOfWords)

if __name__ == "__main__":
    if len(sys.argv) > 2:
        createTFIDF()
    else:
        createBoW()
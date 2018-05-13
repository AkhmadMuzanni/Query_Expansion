from __future__ import division
import math
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

#------------------------------------------------------------------------#

#Fungsi

def binary_term_frequency(term, tokenized_document):
    return term in tokenized_document

def raw_term_frequency(term, tokenized_document):
    return tokenized_document.count(term)

def log_term_frequency(term, tokenized_document):
    count = tokenized_document.count(term)
    if count == 0:
        return 0
    return 1 + math.log10(count)

def inverse_document_frequencies(tokenized_documents, all_tokens_set):
    idf_values = {}
    for tkn in all_tokens_set:
        contains_token =map(lambda doc: tkn in doc, tokenized_documents)
        print (tkn)
        print (len(tokenized_documents))
        y = sum(contains_token)
        print(y)
        idf_values[tkn] = math.log10(len(tokenized_documents)/y)
    return idf_values

def tfidf(documents, idf):
    tfidf_documents = []
    for document in documents:
        doc_tfidf = []
        for term in idf.keys():
            tf = log_term_frequency(term, document)
            doc_tfidf.append(tf * idf[term])
        tfidf_documents.append(doc_tfidf)
    return tfidf_documents

#------------------------------------------------------------------------#
#Preprocessing Dokumen Training

document_0 = "Saya Makan Nasi"
document_1 = "Saya minum air dan minuman dingin, minum"
document_2 = "Nasi makan saya"

train_documents = [document_0, document_1, document_2]
print ("Dokumen Training Asal: ")
print (train_documents)

factory = StemmerFactory()
stemmer = factory.create_stemmer()
train_documents_stemmed = [stemmer.stem(d) for d in train_documents]
print ("Hasil Stemming Dokumen Training: ")
print (train_documents_stemmed)

tokenize = lambda doc: doc.lower().split(" ")
train_documents_tokenized = [tokenize(d) for d in train_documents_stemmed]
print ("Hasil Tokenisasi Dokumen Training: ")
print (train_documents_tokenized)

stop_words=[]
with open("stopword\\stop_words.txt") as f:
    content = f.readlines()
stop_words = [x.strip() for x in content]
#stop_words = ['dan', 'atau', 'itu']
filter = lambda doc: [w for w in doc if w not in stop_words]
train_documents_filtered = [filter(d) for d in train_documents_tokenized]
print ("Hasil Filtering Dokumen Training: ")
print (train_documents_filtered)

all_tokens_set = set([item for sublist in train_documents_filtered for item in sublist])
print ("Term Unik: ")
print (all_tokens_set)

idf = inverse_document_frequencies(train_documents_filtered, all_tokens_set)
print ("IDF: ")
print (idf)

print ("TF-IDF Dokumen Training:")
print (tfidf(train_documents_filtered, idf))

"""
#Preprocessing Dokumen Testing
document_2 = "Matahari di Langit itu terang."
document_3 = "Kita bisa melihat matahari bersinar, Matahari yang terang."

test_documents = [document_2, document_3]
print "Dokumen Testing Asal: "
print test_documents

test_documents_stemmed = [stemmer.stem(d) for d in test_documents]
print "Hasil Stemming Dokumen Testing: "
print test_documents_stemmed

test_documents_tokenized = [tokenize(d) for d in test_documents_stemmed]
print "Hasil Tokenisasi Dokumen Testing: "
print test_documents_tokenized

test_documents_filtered = [filter(d) for d in test_documents_tokenized]
print "Hasil Filtering Dokumen Testing: "
print test_documents_filtered

print "TF-IDF Dokumen Testing:"
print tfidf(test_documents_filtered, idf)
"""

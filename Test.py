from __future__ import division
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import glob
import re
import math
text = []
path="D:\KULIAH\SEMESTER VI\INFORMATION RETRIEVAL SYSTEM\Query_Expansion"
def array_data_gather(path):
      # array
    txt_files = glob.glob(path + "/*.txt")  # ambil file from folder
    for gw in range(len(txt_files)):
        files = open(txt_files[gw])
        text.append(files.read())  # ganti enter d/spasi. ambil data dari folder
        gw + +1
    print (text)
    return text  # balikan dalam bentuk array of text

def log_term_frequency(term, match_pattern):
    count = match_pattern.count(term)
    if count == 0:
        return 0
    return 1 + math.log10(count)

def inverse_document_frequencies(match_pattern, all_tokens_set):
    idf_values = {}
    for tkn in all_tokens_set:
        contains_token =map(lambda doc: tkn in doc, match_pattern)
        print (tkn)
        print (len(match_pattern))
        contains = sum(contains_token)
        print(contains)
        idf_values[tkn] = math.log10(len(match_pattern)/contains)
    return idf_values

def tfidf(match_pattern, idf):
    tfidf_documents = []
    for document in match_pattern:
        doc_tfidf = []
        for term in idf.keys():
            tf = log_term_frequency(term, document)
            doc_tfidf.append(tf * idf[term])
        tfidf_documents.append(doc_tfidf)
    return tfidf_documents

def sigma_tfidf_document(nilaitfidf) :
    hasil = []
    for doc in nilaitfidf :
        nilai_tfidf_document=[]
        for value in doc :
            nilai = math.pow(value,2)
            nilai_tfidf_document.append(nilai)
        jumlah = (sum(nilai_tfidf_document))
        hasil.append(jumlah)
    return hasil

def normalisasi_tfidf_dokumen(nilaitfidf, nilaisigma):
    hasil = []
    for x in range(len(nilaisigma)) :
        nilai_normalisasi = []
        for y in range(len(nilaitfidf[0])):
            nilai_normalisasi.append(nilaitfidf[x][y]/nilaisigma[x])
        hasil.append(nilai_normalisasi)
    return hasil

def tfidfquery(query_token, idf):
    tfidf_query = []
    doc_tfidf = []
    for term in idf.keys():
        tf = log_term_frequency(term, query_token)
        doc_tfidf.append(tf * idf[term])
    tfidf_query.append(doc_tfidf)
    return doc_tfidf

def sigma_tfidf_query(nilaitfidfquery) :
    nilai = 0
    for value in nilaitfidfquery :
        nilai = nilai + math.pow(value,2)
    
    return nilai

def normalisasi_tfidf_query(nilaitfidfquery, nilaisigmaquery):
    hasil = []
    for x in nilaitfidfquery :
        hasil.append(x/nilaisigmaquery)
    return hasil
            
def cosinsimiliraty(nilainormalisasidokumen, nilainormalisasiquery) :
    hasil = []
    for x in range(len(nilainormalisasidokumen)) :
        nilai_cosin=[]
        for y in range(len(nilainormalisasidokumen[0])) :
            nilai_cosin.append(nilainormalisasidokumen[x][y]*nilainormalisasiquery[y])
        jumlah = (sum(nilai_cosin))
        hasil.append(jumlah)
    return hasil     
       
array_data_gather(path)
factory = StemmerFactory()
stemmer = factory.create_stemmer()
train_documents_stemmed = [stemmer.stem(d) for d in text]
tokenize = lambda doc: doc.lower().split(" ")
match_pattern = [tokenize(d) for d in train_documents_stemmed]
stop_words=[]
with open("stopword\\stop_words.txt") as f:
    content = f.readlines()
stop_words = [x.strip() for x in content]
#stop_words = ['dan', 'atau', 'itu']
filter = lambda doc: [w for w in doc if w not in stop_words]
train_documents_filtered = filter(match_pattern)
all_tokens_set = set([item for sublist in train_documents_filtered for item in sublist])
print ("Term Unik: ")
print (all_tokens_set)
print ("Dokumen : ")
print(match_pattern)
idf = inverse_document_frequencies(match_pattern, all_tokens_set)
print ("IDF: ")
print (idf)

print ("TF-IDF Dokumen Training:")
nilaitfidf=tfidf(match_pattern, idf)
print (nilaitfidf)

print ("Normalisasi dokumen : ")
nilaisigma = sigma_tfidf_document(nilaitfidf)
nilainormalisasidokumen = normalisasi_tfidf_dokumen(nilaitfidf, nilaisigma)
print (nilainormalisasidokumen)

query = "indonesia raya"
query_token = tokenize(query)
print (query_token)

print ("TF-IDF Query:")
nilaitfidfquery = tfidfquery(query_token, idf)
print(nilaitfidfquery) 

print ("Normalisasi Query : ")
nilaisigmaquery = sigma_tfidf_query(nilaitfidfquery)
nilainormalisasiquery = normalisasi_tfidf_query(nilaitfidfquery, nilaisigmaquery)
print (nilainormalisasiquery)

print("nilai cosin : ")
print(cosinsimiliraty(nilainormalisasidokumen, nilainormalisasiquery))
'''
frequency = {}
for doc in range(len(match_pattern)):
    for word in match_pattern[doc]:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    
print (frequency)
'''
'''
frequencytf = {}
tfidf_documents = []
for document in match_pattern:
    doc_tfidf = []
    for term in all_tokens_set:
        tf = log_term_frequency(term, document)
        doc_tfidf.append(tf)
        count = frequencytf.get(term,tf)
        frequencytf[term]= count 
    tfidf_documents.append(frequencytf)

print (tfidf_documents)
print (frequencytf)
'''




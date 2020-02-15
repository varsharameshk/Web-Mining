import csv
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

inverted_idx = {}
stop_words = set(stopwords.words("english"))
stop_words = stop_words.union(";", "(", ")", ".", "#", "{", "}", "[", "]", ":", "!", ",", "@", "?")
porter = nltk.PorterStemmer()


def search_query(query):
    query = str(query).split()
    query = [word.lower() for word in query]
    query = list(set(query))
    with open('JEOPARDY_CSV.csv') as f:
        reader = csv.reader(f, delimiter=",")
        next(reader)
        for i, row in enumerate(reader):
            text = " ".join([row[3], row[5], row[6]]).split()  # Tokenization
            text = [word.lower() for word in text]
            text = list(set(text))  # deduplication
            for word in text:
                w = porter.stem(word)  # stemmer
                if w not in stop_words and w not in inverted_idx:  # removing stopwords
                    inverted_idx[word] = []
                    inverted_idx[word].append(i)
                for x in query:
                    if word == x:
                        print(word)
                        print(row[6])  # printing Jeopardy answers for the query
                    else:
                        print("no match found")


input_query = input("Enter a query")
search_query(input_query)

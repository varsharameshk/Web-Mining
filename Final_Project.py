Scrape_blog.py
========================================================================================================================================
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = ['https://indianbloggers.org/', 'https://www.indiblogger.in']
content = requests.get(url).text

# initalizing an empty dictionary that would be written as Pandas Data-frame and then CSV
d = {'TITLE': [], 'LINKS': []}

# initializing blog hosting category
cat = {'blogspot': 0, 'wordpress': 0, 'others': 0}

soup = BeautifulSoup(content, "html.parser")

for link in soup.find_all('a', ):
    if len(link.text.strip()) > 1 and bool(re.match('^http', link['href'])) and not bool(
            re.search('indianbloggers|twitter|facebook', link['href'])):
        d['TITLE'].append(link.text)
        d['LINKS'].append(link['href'])
        # finding the blog hosting type
        if re.search('blogspot', link['href']):
            cat['blogspot'] += 1
        elif re.search('wordpress', link['href']):
            cat['wordpress'] += 1
        else:
            cat['others'] += 1

blog_list = pd.DataFrame(d).set_index('TITLE')
print(blog_list.head())
blog_list.to_csv('blog_list.csv', encoding='utf-8')
print(str(len(blog_list.index)) + ' rows written')
print(cat)

========================================================================================================================================
Flask_app.py
========================================================================================================================================
import pandas as pd
from flask import Flask, request, render_template, flash
import numpy as np
from collections import defaultdict
import math

blogs_df = pd.read_csv("testdata.csv")
blogs_df['url'] = blogs_df['url']
blogs_df['topic'] = blogs_df['topic'].str.lower()
blogs = np.array(blogs_df)


dicD = defaultdict(lambda: defaultdict(int))
index = 0
wordsD = defaultdict(set)
output = defaultdict(list)
for url, topic in blogs:
    descWords = topic.split()
    for word in descWords:
        word = word.strip()
        dicD[url][word] += 1
        wordsD[word].add(url)
    output[url].append(topic)
app = Flask(__name__)


@app.route('/')
def topicName():
    query = request.args.get("query", None)
    print(query)
    if query:
        query = query.lower().strip().split()
        score = defaultdict(float)
        for word in query:
            word = word.strip()
            for doc, word_value in dicD.items():
                if word in word_value.keys():
                    tf = word_value[word] / len(word_value.keys())

                    if doc in wordsD[word]:
                        idf = math.log(len(dicD) / len(wordsD[word]))

                    else:
                        idf = 0
                    score[doc] = score[doc] + (tf * idf)
                else:
                    continue

        sorted_d = sorted(score.items(), key=lambda x: x[1], reverse=True)
        top = 0
        results = []
        for doc, value in sorted_d:
            if top == 30:
                break
            results.append(doc)
            top += 1
        return render_template('results.html', query=query, results=results)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

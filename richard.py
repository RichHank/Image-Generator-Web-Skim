from typing import Counter
from bs4 import BeautifulSoup
from pip._vendor import requests
from selenium import webdriver

stop_list = [ "After","InquiriesU.S","usAffiliatesMedia","Results","FoundNo", "FoundTerms", "ServiceAdvertise","Search","minutes","here","replies","that","about", "blog", "contact","would","season","forum","this","more","full", "have", "list","will","this,","views", "need", "news", "their", "with", "your", "posts", "hours", "discussion","what","world" ]
count = Counter()
result = sorted(count, key = count.__getitem__, reverse = True)
url = 'https://www.infowars.com'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
all_words = soup.get_text(" ").lower().split()
output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head',
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]
whitelist= [
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'p',

]
for t in text:
    if len(t.text)>9:
        sentence_text= t.text.replace('\n', '')
        new_sentence_text= sentence_text.replace('		', '',)
        if t.parent.name in whitelist:
            output += new_sentence_text
            continue
        if t.parent.name in stop_list:
            continue
list_output=output.split(' ')
for word in list_output:
    cln_word = word.strip('.,?')
    # ignore words less 4 char long
    if len(cln_word) > 3:
        # ignore words in our custom stop list
        if cln_word in stop_list:
            continue
        count[cln_word] += 1
#print(word_count)
no_num=''
for value in count:
    no_num+= (value+', ')
print (no_num)
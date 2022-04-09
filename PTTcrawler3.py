# -*- coding: utf-8 -*-
"""
@author: 通識中心 施孟賢
"""
import requests
from bs4 import BeautifulSoup

#pip install jieba
#import jieba.posseg # https://github.com/fxsjy/jieba

def ptt_scraping(url):
    articles = []
    r = requests.get(url=URL, cookies={"over18":"1"})
    soup = BeautifulSoup(r.text, "lxml")
    tag_divs = soup.find_all("div", class_="r-ent")
    for tag in tag_divs:
        if tag.find("a"):
            href = tag.find("a")["href"]
            title = tag.find("a").text
            
            r2=requests.get(url="http://ptt.cc"+href, cookies={"over18":"1"})
            soup2 = BeautifulSoup(r2.text, "lxml")
            articles.append({"title":title, "href":href, "text":soup2.text})
    return articles

#pip install jieba
import jieba.posseg # https://github.com/fxsjy/jieba
import time
#Stock (4980,4995) (2022/3/21重新抓取)
#iOS (5094,5114)

for i in range(5000, 5093): #index9900.html --> 2021/5/15 雙北升3級
    URL = "http://ptt.cc/bbs/iOS/index%d.html" % i #10610->5/19全國3級
    print("URL", URL)

    articles = ptt_scraping(url=URL)
    for article in articles:    
        filename = article["href"].split("/")[-1]
        print("full-href", URL[:13] + article["href"])

        with open(file="iOS/"+filename+".txt", mode="w", encoding="utf8") as file1:
            tagged_words = jieba.posseg.cut(article["text"])
            words = [word for word, pos in tagged_words]
            file1.write(" ".join(words))
            print(" ".join(words).strip()[:22])
        
#       print("title", list(tagged_words)[4:9])#article["title"])
    time.sleep(1)
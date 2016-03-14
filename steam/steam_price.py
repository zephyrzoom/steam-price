#!/usr/bin/env python
#coding=utf-8
""" 
This program is for getting the steam price.
"""
__author__ = "707<707472783@qq.com>"

import urllib
import re
from bs4 import BeautifulSoup

def getPage():
    url = 'http://store.steampowered.com/search/?%s'
    params = urllib.urlencode({'specials':1, 'sort_by':'Name_ASC', 'page': 1})
    f = urllib.urlopen(url % params)
    html = f.read()
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find('div', class_='search_pagination_left').string.strip()
    total = re.match(r'.*of (.*)', total).group(1)
    page = (int(total) + 24) / 25
    return page

def get(page):
    url = 'http://store.steampowered.com/search/?%s'
    params = urllib.urlencode({'specials':1, 'sort_by':'Name_ASC', 'page': page})
    f = urllib.urlopen(url % params)
    html = f.read()
    with open('price.html', 'w') as f:
        f.write(html)
    name_list = []
    price_list = []
    review_list = []
    soup = BeautifulSoup(html, 'lxml')
    for row in soup.find_all('a', class_ = 'search_result_row'):
        price = row.find('div', class_='search_price').contents[3].strip()
        price = re.match(r'\xa5 (.*)', price)
        if price:
            price = price.group(1)
        else:
            price = 0
        review = row.find('span', class_='search_review_summary')
        if review:
            review = review['data-store-tooltip']
            review = re.match(r'.*>(.*)%.*', review).group(1)
        else:
            review = 0
        print row.span.string, price, review




#def getSteam():
#    url = 'http://store.steampowered.com/search/?%s'
#    params = urllib.urlencode({'specials':1, 'sort_by':'Name_ASC', 'page': 1})
#    f = urllib.urlopen(url % params)
#    html = f.read()
#    #print html
#    with open('price.html', 'w') as f:
#        f.write(html)
#    name_list = []
#    price_list = []
#    review_list = []
#    soup = BeautifulSoup(html, 'lxml')
#    for row in soup.find_all('a', class_ = 'search_result_row'):
#        price = row.find('div', class_='search_price').contents[3].strip()
#        price = re.match(r'\xa5 (.*)', price)
#        if price:
#            price = price.group(1)
#        else:
#            price = 0
#        review = row.find('span', class_='search_review_summary')
#        if review:
#            review = review['data-store-tooltip']
#            review = re.match(r'.*>(.*)%.*', review).group(1)
#        else:
#            review = 0
#        print row.span.string, price, review
#
#    total = soup.find('div', class_='search_pagination_left').string.strip()
#    total = re.match(r'.*of (.*)', total).group(1)
#    page = (int(total) + 24) / 25
#    print total, page
    

if __name__ == '__main__':
    page = getPage()
    #for i in range(page):
    #    try:
    #        get(i+1)
    #    except Exception, e:
    #        get(i+1)
    for i in range(page):
        while True:
            try:
                get(i+1)
                break
            except Exception, e:
                print e


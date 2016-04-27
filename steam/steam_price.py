#!/usr/bin/env python
#coding=utf-8
""" 
This program is for getting the steam price.
"""
__author__ = "707<707472783@qq.com>"

import urllib
import re
from bs4 import BeautifulSoup

# 获取页数
def getPage():
    # 构造链接 
    url = 'http://store.steampowered.com/search/?%s'
    params = urllib.urlencode({'specials':1, 'sort_by':'Name_ASC', 'page': 1})
    
    # 获取数据
    f = urllib.urlopen(url % params)
    html = f.read()

    # 解析
    soup = BeautifulSoup(html, 'lxml')
    total = soup.find('div', class_='search_pagination_left').string.strip()
    total = re.match(r'.*of (.*)', total).group(1)

    page = (int(total) + 24) / 25
    return page

# 获取某页的数据
def get(page):
    # 构造链接
    url = 'http://store.steampowered.com/search/?%s'
    params = urllib.urlencode({'specials':1, 'sort_by':'Name_ASC', 'page': page})

    # 请求数据
    f = urllib.urlopen(url % params)
    html = f.read()

    # 将网页信息写入文件
    with open('price.html', 'w') as f:
        f.write(html)

    # 游戏名
    name_list = []
    # 打折后价格
    price_list = []
    # 评分
    review_list = []
    soup = BeautifulSoup(html, 'lxml')

    # 解析页面
    for row in soup.find_all('a', class_ = 'search_result_row'):
        price = row.find('div', class_='search_price')
        # 没有原价
        if len(price) < 4:
            price = re.match(r'\xa5 (.*)', price.contents[0].strip()).group(1)
        # 正常情况
        else:
            price = re.match(r'\xa5 (.*)', price.contents[3].strip())
            if price:
                price = price.group(1)
            # 免费或者没有价钱
            else:
                price = 0

        review = row.find('span', class_='search_review_summary')
        if review:
            review = review['data-store-tooltip']
            review = re.match(r'.*>(.*)%.*', review).group(1)
        else:
            # 无评分显示0
            review = 0
        print row.span.string, price, review


   

if __name__ == '__main__':
    page = getPage()
    for i in range(page):
        while True:
            try:
                get(i+1)
                break
            except Exception, e:
                print "********************************" + str(i)
                print e


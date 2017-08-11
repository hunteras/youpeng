#!/usr/bin/env python3
import sys
from requests import get
from bs4 import BeautifulSoup
from json import dumps, loads
from utils import filecontent

path = 'data/tagtable.json'

class TagTable:
    def __init__(self):
        global path
        json = filecontent(path)
        self.table = loads(json)
        self.simple = list(map((lambda x: {x['code']:x['name']}), self.table))

def main():
    url = 'http://www.cnblogs.com/wq920/p/5622583.html'
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup('tr')[1:]
    tags = []
    for tr in table:
        es = list(map((lambda x: x.get_text()), tr('td')))
        tags.append({'code':es[0].strip(), 'name':es[1].strip(), 'comment':es[2].strip()})
    global path
    with open(path, 'w') as w:
        w.write(dumps(tags, ensure_ascii=False))

if __name__ == '__main__':
    main()


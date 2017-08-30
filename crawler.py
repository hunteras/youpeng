#!/usr/bin/env python3
import sys
from requests import get
from bs4 import BeautifulSoup
from json import dumps, loads
from utils import loadjson
import os.path

SJ = 'http://www.gushiwen.org/guwen/shiji.aspx'

path = 'sj/toc.json'

def get_toc():
    global SJ
    toc = []
    r = get(SJ)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.select("span > a"):
        toc.append({ 'url': a.get('href'), 'name': a.get_text() })
    with open(path, 'w') as w:
        w.write(dumps(toc, ensure_ascii=False))
    return toc

def load_toc():
    return loadjson(path)

def chapters():
    toc = load_toc()
    for e in toc:
        print("GET {0} FROM {1}".format(e['name'], e['url']))
        name = get_chapter(e['url'])
        print("WROTE {0}".format(name))
    
    
def get_chapter(url):
    pars = []
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for p in soup.find_all("div", class_="contson")[0].select("p"):
        pars.append(p.get_text())
    text = "\n".join(pars)
    name = soup.h1.contents[0].strip() + ".txt"
    with open(os.path.join('sj', name), 'w') as w:
        w.write(text)
    return name

if __name__ == '__main__':
    chapters()


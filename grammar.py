#!/usr/bin/env python3
import sys
from utils import filecontent, lltod
from json import loads

class Grammar:
    def __init__(self, filename):
        self.json = filecontent(filename)
        self.obj = loads(self.json)
        self.tag = self.obj[0]['tag']
        self.word = self.obj[0]['word']
        self.uniqtag = set(self.tag)
        self.tagmap = lltod(self.tag, self.word)

        # nr m q

        
def main():
    if len(sys.argv) == 1:
        print("Usage:%s [Param] [...]" % sys.argv[0])
        return

    g = Grammar('data/kzsj.json')
    print(g.obj)
    
if __name__ == '__main__':
    main()


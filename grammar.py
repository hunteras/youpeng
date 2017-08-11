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

    def sentences(self, tags):
        '''return sentences constructed with tags. '''
        indices = range(len(self.tag))
        for j, t in enumerate(tags):
            indices = [i for i in indices if self.tag[j+i] == t]
        # return list(map((lambda x: (x, self.word[x:x+len(tags)])), indices))
        return indices

    def yearmark(self):
        tags = ['nr', 'm', 'q']
        indices = self.sentences(tags)
        indices = filter((lambda i: self.word[i+len(tags)-1] == '年'), indices)
        return list(map((lambda x: (x, self.word[x:x+len(tags)])), indices))

    def markbetween(self, i, tag):
        length = len(self.tag)
        left = i
        while (left > 0):
            if (self.tag[left] == tag):
                break
            else:
                left = left - 1
        right = i
        while (right < length):
            if (self.tag[right] == tag):
                break
            else:
                right = right + 1
        return (left, right)

    def yearsentence(self):
        s = []
        ym = self.yearmark()
        for m in ym:
            (i, a) = m
            (left, right) = self.markbetween(i, 'wj')
            print(''.join(self.word[left+1:right+1]))
            s.append((i, self.word[left+1:right+1]))
        return s

def main():
    if len(sys.argv) == 1:
        print("Usage:%s [Param] [...]" % sys.argv[0])
        return

    g = Grammar('data/kzsj.json')
    print(g.yearsentence())

if __name__ == '__main__':
    main()

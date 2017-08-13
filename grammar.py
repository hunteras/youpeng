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
        # tags = ['nr', 'm', 'q']
        tags = ['m', 'q']
        indices = self.sentences(tags)
        indices = filter((lambda i: self.word[i+len(tags)-1] == '年'), indices)
        return list(map((lambda x: (x, self.word[x:x+len(tags)])), indices))

    def markbetween(self, i, ltags, rtags):
        length = len(self.tag)
        left = i
        while (left > 0):
            if (self.tag[left] in ltags):
                break
            else:
                left = left - 1
        right = i
        while (right < length):
            if (self.tag[right] in rtags):
                break
            else:
                right = right + 1
        return (left, right)

    def yearsentence(self):
        s = []
        ym = self.yearmark()
        for m in ym:
            (i, a) = m
            (left, right) = self.markbetween(i, ['wj', 'wyy', 'wyz'], ['wj'])
            # print(''.join(self.word[left+1:right+1]))
            s.append((left+1, self.word[left+1:right+1]))
        return s

    def yeargong(self):
        yg = []
        ys = self.yearsentence()
        for s in ys:
            (i, a) = s
            for w in a:
                if (w.find('公') != -1):
                    yg.append(s)
                    break
        return yg

    def timeline(self):
        l = []
        yg = self.yeargong()
        for s in yg:
            (i, a) = s
            elements = []
            j = 0
            length = len(a)
            while (j < length):
                w = a[j]
                if (w.find('公') != -1) or (w.find('王') != -1):
                    if (len(w) == 1):
                        elements.append(''.join(a[j-1:j+1]))
                        # elements.append(w)
                    else:
                        elements.append(w)
                    j += 1
                    continue
                if (w.find('卒') != -1) or (w.find('立') != -1):
                    elements.append(w)
                    j += 1
                if (j+1 < length):
                    # print(w, ' ', self.tag[i+j], ' ', self.tag[i+j+1])
                    if (self.tag[i+j] == 'm') and (self.tag[i+j+1] == 'q'):
                        elements.append(''.join(a[j:j+2]))
                        j += 2
                        continue
                j += 1
            l.append((i, a, elements))
        return l

def main():
    if len(sys.argv) == 1:
        print("Usage:%s [Param] [...]" % sys.argv[0])
        return

    g = Grammar(sys.argv[1])
    # for s in g.yeargong():
    #     (i, a) = s
    #     print(''.join(a))

    for es in g.timeline():
        (i, a, e) = es
        print(''.join(a), " : ", e)
        # for j, w in enumerate(a):
        #     print("    :{0} {1} {2}".format(w, g.tag[i+j], g.word[i+j]))
        # print("    :", g.tag[i:i+len(a)])

if __name__ == '__main__':
    main()

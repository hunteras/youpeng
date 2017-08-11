#!/usr/bin/env python3

def filecontent(filename):
    contents = ''
    with open(filename, 'r') as r:
        contents = r.read()
    return contents

def lltod(a, l):
    s = set(a)
    d = {}
    for t in s:
        ws = []
        for i, m in enumerate(a):
            if (m == t):
                ws.append(l[i])
        d[t] = ws
    return d

def sortcount(a):
    s = set(a)
    c = []
    for e in s:
        c.append(a.count(e))
    return zip(list(s), c)
    
def main():
    s = ['h', 'c', 'c']
    l = ['hello', 'color', 'cool']
    print(lltod(s, l))

    a = ['hello', 'color', 'color']
    for e in sortcount(a):
        print(e)
    
if __name__ == '__main__':
    main()


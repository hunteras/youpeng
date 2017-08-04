#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from __future__ import print_function, unicode_literals
from bosonnlp import BosonNLP

class Timeline:
    def __init__(self, contents):
        self.contents = contents

def main():
    if len(sys.argv) == 1:
        print("Usage:%s [Param] [...]" % sys.argv[0])
        return

if __name__ == '__main__':
    main()


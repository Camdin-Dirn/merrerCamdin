#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re

word_pattern = re.compile(r'^[a-zA-Z]+$')

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if word_pattern.match(word):
            print(f'{word.lower()}\t1')


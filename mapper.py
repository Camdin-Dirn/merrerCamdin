#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys 

[[print(\'%s\t%s\' % (word, 1)) for word in [\'\'.join([c for c in chars if c.isalpha()]) for chars in line.split()] if word] for line in sys.stdin]


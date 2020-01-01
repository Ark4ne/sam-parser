#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from src.Evaluator.Cigar import Cigar
from src.Evaluator.Flag import Flag
from src.Evaluator.Mdz import Mdz
from src.Parser import Parser

try:
    file = sys.argv[1]
except IndexError:
    print('File is required')
    exit(1)

try:
    method = sys.argv[2]
except IndexError:
    print('Method is required')
    exit(1)

if method == 'cigar':
    evaluator = Cigar()
elif method == 'flag':
    evaluator = Flag()
elif method == 'mdz':
    evaluator = Mdz()
else:
    print('Unknown method ' + method)
    exit(1)

parser = Parser(file)

headers = parser.headers()
status = parser.analyse(evaluator)

print('+------ HEADERS ------+')
headers.print()
print('')
print('+------ DATA ---------+')
status.print()

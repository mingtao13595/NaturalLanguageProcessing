# coding: UTF-8
#!/usr/bin/env python

import MeCab
import CaboCha
import re
import json

mt = CaboCha.Parser()
targ = "太郎はこの本を次郎を見た女性に渡した"

print(mt.parseToString(targ))

tree = mt.parse(targ)
print("--------------------------")
print(tree.toString(CaboCha.FORMAT_TREE))

print("--------------------------")
print(tree.toString(CaboCha.FORMAT_LATTICE))

print("---------------------------")
print(tree.toString(CaboCha.FORMAT_XML))

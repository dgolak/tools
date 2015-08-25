#!/usr/bin/env python
"""
How to use: ./deobfuscate.py < vir.txt
Chr(71) & Chr(69) & "T" Chr(104) & Chr(116) & "t"
"""

import re
import sys
data=sys.stdin.read()

t=""
r = re.compile('(Chr\((\S+)\)|\"(\S+)\")')
i = re.findall(r,data)
for match in i:
    if match[0].find("Chr") == 0:
	t=str(t)+str(chr(int(match[1])))
    else:
	t=str(t)+str(match[2])
print t

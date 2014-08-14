#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    file = open(sys.argv[1])
    s1 = file.readline()
    s2 = file.readline()
elif len(sys.argv) == 3:
    s1, s2 = sys.argv[1:]
else:
    print("Problem!!")
    sys.exit(2)

hamm = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        hamm += 1

print hamm

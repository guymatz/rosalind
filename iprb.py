#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    file = open(sys.argv[1])
    line = file.readline().strip()
    k,m,n = line.split()
    file.close()
elif len(sys.argv) == 3:
    k, m, n = sys.argv[1:]
else:
    print("Problem!!")
    sys.exit(2)



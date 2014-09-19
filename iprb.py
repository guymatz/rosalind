#!/usr/bin/env python

import sys

if len(sys.argv) == 2:
    file = open(sys.argv[1])
    line = file.readline().strip()
    k,m,n = map(float, line.split())
    file.close()
elif len(sys.argv) == 4:
    k, m, n = map(float, sys.argv[1:])
else:
    print("Problem!! %i " % len(sys.argv) )
    sys.exit(2)

km1 = k - 1 
mm1 = m - 1
nm1 = n - 1
total = float(k + m + n)
tm1 = k + m + n -1
p1 = k/total * ( km1/tm1 + m/tm1 + n/tm1  ) 
p2 = m/total * ( k/tm1 + (3/4.0)*(mm1/tm1) + (1/2.0)*(n/tm1)  ) 
p3 = n/total * ( k/tm1 + (1/2.0)*(m/tm1) ) 
print p1 + p2 + p3

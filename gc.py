#!/usr/bin/env python

import sys
ffile = sys.argv[1]
gc_by_id = {}

with open(ffile) as file:
    orf = ''
    label = ''
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if orf != '' :
                gc_by_id[label] =  100 * (orf.count('G') + orf.count('C') ) / float(len(orf))
            orf =''
            label = line[1:]
            continue
        orf += line

max = max(zip(gc_by_id.values(), gc_by_id.keys() ) )
print max[1]
print max[0]

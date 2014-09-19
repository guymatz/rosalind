#!/usr/bin/env python

from rna_codon import rna_codon
import sys
from os import path

if path.isfile(sys.argv[1]):
    with open(sys.argv[1]) as file:
      rna_string = file.readlines()[0].strip()
else:
    rna_string = sys.argv[1]

#print rna_string

def to_aa(codon):
  if rna_codon[codon] == 'Stop':
      return ''
  else:
      return rna_codon[codon]

proteins = [ to_aa(rna_string[x:x+3]) for x in range(0, len(rna_string), 3) ]
proteins = ''.join([ to_aa(rna_string[x:x+3]) for x in range(0, len(rna_string), 3) ])

print proteins

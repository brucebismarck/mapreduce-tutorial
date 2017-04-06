#!/usr/bin/python
import re
import sys

for line in sys.stdin:
    vals = line.strip()    # strip is used to remove start and end signs
    if vals.split(',')[5] == 'lithium carbonate':
        key = vals.split(',')[0] + '_'+ vals.split(',')[1]
        print '%s\t%s' %(key, 1)


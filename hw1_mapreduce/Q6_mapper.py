#!/usr/bin/python
import re
import sys

for line in sys.stdin:
    vals = line.strip()    # strip is used to remove start and end signs
    if vals.split(',')[6] == 'LITHIUM CARBONATE' or vals.split(',')[5] == 'RISPERDAL':
        key = vals.split(',')[0] + '_'+ vals.split(',')[1]+'_'+vals.split(',')[6]
        print '%s\t%s' %(key, 1)

#!/usr/bin/python
import re
import sys

last_key_pat = None
key_med_list = list()
key_pat_list = list()
for line in sys.stdin:
    (key, val) = line.strip().split("\t")
    key_med = key.split('_')[2]
    key_pat = key.split('_')[0] +'_'+ key.split('_')[1]
    if key_pat != last_key_pat:
        key_pat_list.append(key_pat)
        key_med_list.append(1)
        last_key_med = key_med
        last_key_pat = key_pat
    else:
        if key_med != last_key_med:
     	    key_med_list[-1] = key_med_list[-1] + int(val)
     	    last_key_med = key_med

position = [i for i,x in enumerate(key_med_list) if x == 2]
patients = list(key_pat_list[i] for i in position)
print patients

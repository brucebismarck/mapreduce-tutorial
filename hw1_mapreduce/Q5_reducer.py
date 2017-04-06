#!/usr/bin/python
import re
import sys

last_key_med = None
key_med_list = list()
key_pat_list = list()
for line in sys.stdin:
	(key,val) = line.strip().split("\t")
	key_pat = key.split('_')[1] + key.split('_')[2]
	key_med = key.split('_')[0]
	if key_med != last_key_med:
            key_med_list.append(key_med)
            key_pat_list.append(1)
            last_key_pat = key_pat
            last_key_med = key_med
        else:
            if key_pat != last_key_pat:
                key_pat_list[-1] = key_pat_list[-1] + int(val)
                last_key_pat = key_pat
            
max_index = key_pat_list.index(max(key_pat_list))
max_pat_num = max(key_pat_list)

print max_pat_num
print key_med_list[max_index]

#!/usr/bin/python
import re
import sys

(last_key, sum_val) = (None, 0)

for line in sys.stdin:
   (key, val) = line.strip().split("\t")
   if last_key != key:
       (last_key, sum_val) = (key, sum_val + int(val))
             
print 'There is in total ', '\t', sum_val, ' unique patients who are taking or have taken lithium carbonate'

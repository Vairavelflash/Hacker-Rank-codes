#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

if __name__ == '__main__':
    # s = input()

 
 S = input()
 S = sorted(S)
 FREQUENCY = Counter(list(S))
#  print (FREQUENCY)
 for k, v in FREQUENCY.most_common(3):
    print(k, v)
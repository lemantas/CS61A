#!/usr/bin/env python3

import sys
from mr import values_by_key, emit


def count_vowels(line):
    for vowel in 'aeiou':
        count = line.count(vowel)
        if count > 0:
            emit(vowel, count)
            
try:
    for key, value_iterator in values_by_key(sys.stdin):
        emit(key, sum(value_iterator))
except KeyboardInterrupt:
    print("\nbye bye!")

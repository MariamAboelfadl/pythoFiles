#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    s = input()
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1


    frequencies = list(frequencies.items())


    frequencies = sorted(frequencies, key=lambda item: item[0])

    frequencies = sorted(frequencies, key=lambda item: item[1], reverse=True)


    for char, frequency in frequencies[:3]:
        print(char, frequency)
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    val=sentence.split(" ")
    val.reverse()
    ans=""
    for i in val:
        for j in i:
            if (j.isupper()):
                ans+=j.lower()
            else:
                ans+=j.upper()
        ans+=" "   
    return ans
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()

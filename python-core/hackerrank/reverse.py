#!/bin/python3

import os


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
# STDIN                 Function
# -----                 --------
# aWESOME is cODING  →  sentence = "aWESOME is cODING"
# OUTPUT: Coding IS Awesome


def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    strings = sentence.split(" ")

    result = []
    for str in strings:
        result.insert(0, str.swapcase())

    return " ".join(result)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # sentence = input()
    sentence = "aWESOME is cODING"
    result = reverse_words_order_and_swap_cases(sentence)

    print(result)
    # fptr.write(result + '\n')
    # fptr.close()

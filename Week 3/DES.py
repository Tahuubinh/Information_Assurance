import numpy as np
import random
from random import sample

# Make keys
origin = list()
list_32_first_ints = list(range(32))
list_48_first_ints = list(range(48))
list_56_first_ints = list(range(56))
list_64_first_ints = list(range(64))
choice_48_from_56 = sample(list_56_first_ints, 48)
choice_32_PC2 = sample(list_32_first_ints, 32)
choice_48_PC2 = sample(list_48_first_ints, 48)
choice_64_PC1 = sample(list_64_first_ints, 64)
inverse_choice_64 = list()
for i, v in enumerate(choice_64_PC1):
    inverse_choice_64.append(v)
keys = list()
keys = list()

def rotateList(bits_list, length, k = -1):
    if k == -1:
        k = random.randint(0, length - 1)
    return bits_list[k:] + bits_list[:k]

# def mergeList(bits_list, length):
#     half_length = length / 2
#     bits_left = bits_list[:half_length]
#     bits_right = bits_list[half_length:]
#     bits_left = rotateList(bits_left, half_length)
#     bits_right = rotateList(bits_right, half_length)
#     bits_merge = bits_left + bits_right
#     bits_merge = rotateList(bits_left, length)

def mergeList(bits_left, bits_right, length):
    half_length = length / 2
    bits_left = rotateList(bits_left, half_length, 27)
    bits_right = rotateList(bits_right, half_length, 26)
    bits_merge = bits_left + bits_right
    #bits_merge = rotateList(bits_merge, length)
    return bits_left, bits_right, bits_merge

def choiceList(bits_list, choice):
    # length = len(bits_list)
    temp = list()
    #print(bits_list)
    for index, value in enumerate(choice):
        temp.append(bits_list[value])
    return temp
    
for _ in range(64):
    k = random.randint(0, 1) 
    origin.append(k)

origin = choiceList(origin, choice_64_PC1)

bits_56 = list()

for index, value in enumerate(origin):
    if index % 8 != 7:
        bits_56.append(value)

bits_left = bits_56[0:28]
bits_right = bits_56[28:]

for i in range(16):
    bits_left, bits_right, mergetemp = mergeList(
                    bits_left, bits_right, 56)

    result = choiceList(mergetemp, choice_48_from_56)
    result = choiceList(result, choice_48_PC2)
    keys.append(result)

# Encode
news = list()
for _ in range(64):
    k = random.randint(0, 1) 
    news.append(k)

news = choiceList(news, choice_64_PC1)

bits_left = news[:32]
bits_right = news[32:]

def expansionPermutation(bits, small, big):
    addition = big - small
    for _ in range(addition):
        k = random.randint(0, 1) 
        bits.append(k)
    return bits

def xorList(a, b):
    temp = list()
    for i, j in zip(a, b):
        temp.append(i ^ j)
    return temp

def pseudoSBoxes(bits):
    temp = list()
    for i, v in enumerate(bits):
        if (i % 6 in [1, 3]):
            continue
        temp.append(v)
    return temp

def f(bits_right, key):
    bits_right = expansionPermutation(bits_right, 32, 48)
    bits_right = xorList(bits_right, key)
    bits_right = pseudoSBoxes(bits_right)
    bits_right = choiceList(bits_right, choice_32_PC2)
    return bits_right



for i in range(16):
    old_bits_left = bits_left
    bits_left = bits_right
    bits_right = xorList(bits_left, f(bits_right, keys[i]))

encode_news = bits_left + bits_right
encode_news = choiceList(encode_news, inverse_choice_64)

print(encode_news)






    



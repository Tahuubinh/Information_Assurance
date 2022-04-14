import numpy as np
import random
from random import sample

origin = list()
list_56_first_ints = list(range(56))
choice_48_PC2 = sample(list_56_first_ints, 48)
keys = list()
results = list()

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
    bits_left = rotateList(bits_left, half_length)
    bits_right = rotateList(bits_right, half_length)
    bits_merge = bits_left + bits_right
    bits_merge = rotateList(bits_merge, length)
    return bits_left, bits_right, bits_merge

def choiceList(bits_list, choice_48_PC2):
    # length = len(bits_list)
    temp = list()
    #print(bits_list)
    for index, value in enumerate(choice_48_PC2):
        temp.append(bits_list[value])
    return temp
    
for _ in range(64):
    k = random.randint(0, 1) 
    origin.append(k)

bits_56 = list()

for index, value in enumerate(origin):
    if index % 8 != 7:
        bits_56.append(value)

bits_left = bits_56[0:28]
bits_right = bits_56[28:]

for i in range(16):
    bits_left, bits_right, mergetemp = mergeList(
                    bits_left, bits_right, 28)

    result = choiceList(mergetemp, choice_48_PC2)
    results.append(result)

for result in results:
    print(result)

    



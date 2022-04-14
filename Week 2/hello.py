l = m = Nr = 4

def binToDec(binary_num):
    return int(binary_num, 2)

def decToBin(dec_num):
    if not dec_num:
        return '0'
    ans = ''
    while (dec_num):
        ans = str(dec_num % 2) + ans
        dec_num = dec_num // 2
    lenans = len(ans)
    if (lenans % 4):
        ans = '0' * (4 - lenans % 4) + ans
    return ans

listS = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7]
listSbin = [decToBin(i) for i in listS]
listP = [1,5,9,13,2,6,10,14,3,7,11,15,4,8,12,16]

K1 = "0011101010010100"
K2 = "0011101010011101"
K3 = "1001010011010110"
K4 = "0100110101100011"
K5 = "1101011000111111"
K = ['0', K1, K2, K3, K4, K5]


def piS(x):
    ans = ''
    while x !='':
        tempdec = binToDec(x[:4])
        tempSdec = listS[tempdec]
        ans += decToBin(tempSdec)
        x = x[4:]
    return ans

def piP(x):
    ans = ['0'] * 16
    for ind, val in enumerate(listP):
        ans[val - 1] = x[ind]
    res = ''
    for i in ans:
        res += i
    return res

def xorBit(x, y):
    return decToBin(binToDec(x) ^ binToDec(y))

def SPN(x):
    w = x
    for r in range(1, Nr):
        u_r = decToBin(binToDec(w) ^ binToDec(K[r]))
        v_r = piS(u_r)
        w = piP(v_r)
    u = decToBin(binToDec(w) ^ binToDec(K[Nr]))
    for i in range(1, m + 1):
        v = piS(u)
    y = decToBin(binToDec(v) ^ binToDec(K[Nr + 1]))
    return y

input = "0010011010110111"
# print(K1)
# print(binToDec(K1))
# print(decToBin(14996))
# print(K1[4:])
# print(K1[:4])
# print(piP(K1))
print(SPN(input))



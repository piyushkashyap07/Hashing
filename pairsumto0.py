# Pair Sum To 0
# Send Feedback
# Given a random integer array A of size N. Find and print the count of pair of elements in the array which sum up to 0.
# Note: Array A can contain duplicate elements as well.
# Input format:
# The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
# The following line contains N space separated integers, that denote the value of the elements of the array.
# Output format:
# The first and only line of output contains the count of pair of elements in the array which sum up to 0.
# Constraints:
# 0 <= N <= 10 ^ 4
# Time Limit: 1 sec
# Sample Input 1:
# 5
# 2 1 - 2 2 3
# Sample Output 1:
# 2
from sys import stdin
from math import factorial

# n choose 2 will be used to decide how many times pair (0,0) is to be printed


def nc2(n):
    ans = 0
    if n != 1:
        ans = factorial(n) / (factorial(2)*factorial(n-2))
    return int(ans)

# For creating frequency map


def freqMap(l):
    map = {}
    for num in l:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    return map


def pairSum0(l, n):
    m = freqMap(l)  # HashMap(integer,integer) frequencyMap
    count = 0
    for num in m:
        # if(frequencyMap contains the key âcomplementâ)
        if num > 0 and -num in m:
            # //print pair frequencyMap[complement] times
            count = count + (m[num]*m[-num])

        if num == 0:
            # //frequencyMap[element] is initially 0
            count = count + nc2(m[num])
    return count


def takeInput():
    #To take fast I/O
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n


arr, n = takeInput()
print(pairSum0(arr, n))

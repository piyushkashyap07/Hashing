# Longest subset zero sum
# Send Feedback
# Given an array consisting of positive and negative integers, find the length of the longest subarray whose sum is zero.
# Input Format:
# The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
# The following line contains N space separated integers, that denote the value of the elements of the array.
# Output Format
# The first and only line of output contains length of the longest subarray whose sum is zero.
# Constraints:
# 0 <= N <= 10 ^ 8
# Time Limit: 1 sec
# Sample Input 1:
# 10
# 95 - 97 - 387 - 435 - 5 - 70 897 127 23 284
# Sample Output 1:
# 5
# Explanation:
# The five elements that form the longest subarray that sum up to zero are: -387, -435, -5, -70, 897
def subsetSum(l):
    n = len(l)
    sum = [0] * n
    sum[0] = l[0]
    m = {l[0]: 0}
    start, end = -1, -2
    if sum[0] == 0:
        start, end = 0, 0
    for i in range(1, n):
        sum[i] = sum[i-1] + l[i]
        if sum[i] == 0:
            start, end = 0, i
        elif sum[i] in m:
            #Found a subset with zero Sum
            if i-m[sum[i]] > end-start+1:
                start, end = m[sum[i]]+1, i
        else:
            m[sum[i]] = i
    return end-start+1


# Main
n = int(input())
l = list(int(i) for i in input().strip().split(' '))
print(subsetSum(l))

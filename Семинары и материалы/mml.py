def msrt(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = msrt(arr[:mid])
    right = msrt(arr[mid:])
    return merge(left, right)


def merge(left, right):
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

def erat(n):
    blst = [True for i in range(n + 1)]
    blst[0], blst[1] = False, False
    for i in range(2, n + 1):
        for j in range(i + i, n + 1, i):
            blst[j] = False
    return blst

def z(s):
    z = [0 for i in range(len(s))]
    l, r = 0, 0
    for i in range(1, len(s)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z
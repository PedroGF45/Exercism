def triplets_with_sum(number):
    ans = []
    for i in range(1, number + 1, 1):
        for j in range(i + 1, int(number - (2 / i)), 1):
            k = number - i - j
            if ((i**2 + j**2 == k**2) and (i < j) and (j < k) and (i + j + k == number)):
                ans.append([i, j, k])
    return ans

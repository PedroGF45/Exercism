def append(list1, list2):
    return list1 + list2

def concat(lists):
    ans = []
    for list in lists:
        ans = append(ans, list)
    return ans

def filter(function, list):
    ans = []
    for item in list:
        if function(item):
            ans = append(ans, [item])
    return ans

def length(list):
    l = 0
    for item in list:
        l += 1
    return l

def map(function, list):
    ans = []
    for item in list:
        ans = append(ans, [function(item)])
    return ans

def foldl(function, list, initial):
    ans = initial
    for index in range(len(list)):
        ans = function(ans, list[index])
    return ans

def foldr(function, list, initial):
    ans = initial
    for index in range(len(list) -1, -1 , -1):
        ans = function(list[index], ans)
    return ans

def reverse(list):
    ans = []
    for index in range(len(list) - 1, -1, -1):
        ans = append(ans, [list[index]])
    return ans

from itertools import product

def solution(word):
    dict = []
    for i in range(1, 6):
        for j in product('AEIOU', repeat=i):
            dict.append(''.join(list(j)))
    dict.sort()
    return dict.index(word) + 1
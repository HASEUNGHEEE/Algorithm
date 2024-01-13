def solution(n, words):
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            return [i%n+1, i//n+1]
        w = words[:i]
        if words[i] in w:
            return [i%n+1, i//n+1]
    return [0,0]
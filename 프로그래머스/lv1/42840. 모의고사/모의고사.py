def solution(answers):
    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    ans = []
    
    for idx, answer in enumerate(answers):
        # tc1 : (0, 1) (1, 2) (2, 3) (3, 4) (4, 5)
        if answer == pattern_1[idx % len(pattern_1)]:
            scores[0] += 1
        if answer == pattern_2[idx % len(pattern_2)]:
            scores[1] += 1
        if answer == pattern_3[idx % len(pattern_3)]:
            scores[2] += 1
    
    for idx, score in enumerate(scores):
        if score == max(scores):
            ans.append(idx+1)
            
    return ans
from collections import deque

def bfs(begin, target, words):
    q = deque()
    q.append([begin, 0]) # 시작 단어 begin과 단계 0
    while q:
        now, step = q.popleft() # 현재 단어, 현재 단계
        
        if now == target:
            return step
        
        for word in words:
            diff_cnt = 0
            for i in range(len(now)):
                if word[i] != now[i]: # 같지 않은 알파벳 개수 확인하여 cnt 증가
                    diff_cnt += 1
                    
            if diff_cnt == 1: # 알파벳 한 글자만 다르다면 큐에 [현재 단어, 현재 단계 + 1] 추가
                q.append([word, step+1])
    
def solution(begin, target, words):
    # 변환할 수 없는 경우 0 리턴
    if not target in words: 
        return 0
    
    return bfs(begin, target, words)
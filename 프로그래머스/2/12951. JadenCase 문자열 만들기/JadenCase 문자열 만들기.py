def solution(s):
    answer = ''
    s = s.title() # 문자열의 각 단어의 첫 글자를 대문자로 만들고 나머지는 소문자로 변환
    for i in range(len(s)):
        if s[i-1].isdecimal():
            answer += s[i].lower()
        else:
            answer += s[i]
    
    return answer
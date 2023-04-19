def parse(p):
    left = 0
    right = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:i+1], p[i+1:]

def check(u):
    stack = []
    
    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()
    return True
    
def solution(p):
    if len(p) == 0: return p
    
    u, v = parse(p)
    
    if check(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('
            
        return answer
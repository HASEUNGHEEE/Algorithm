def solution(quiz):
    answer = []
    for str in quiz:
        exp = str.split()
        if exp[1] == '-':
            if int(exp[0]) - int(exp[2]) == int(exp[-1]):
                answer.append('O')
            else:
                answer.append('X')
        elif exp[1] == '+':
            if int(exp[0]) + int(exp[2]) == int(exp[-1]):
                answer.append('O')
            else:
                answer.append('X')
            
    return answer
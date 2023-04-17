def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    
    for i in range(len(numbers)): # i = 0,1,2,3
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer

# i = 0, stack = [0]
# i = 1, answer[0] = numbers[1], answer = [3, -1, -1, -1], stack = [1]
# i = 2, stack = [1, 2]
# i = 3, 
#  answer[2] = numbers[3], answer = [3, -1, 5, -1], stack = [1]
#  answer[1] = numbers[3], answer = [3, 5, 5, -1]
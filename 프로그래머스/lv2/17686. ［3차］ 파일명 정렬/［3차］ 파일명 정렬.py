def solution(files):
    answer = []
    
    for file in files:
        # head, number, tail 분리
        head, number, tail = '', '', ''
        for i in range(len(file)):
            if not file[i].isdigit() and not number:
                head += file[i]
            elif file[i].isdigit() and head:
                number += file[i]
            else:
                tail += file[i:]
                break
        answer.append((head, number, tail))
        
    # 정렬
    answer.sort(key = lambda x: [x[0].lower(), int(x[1])])
    
    
    return [''.join(i) for i in answer]
def solution(book_time):
    time_dic = {}
    
    # book_time을 분으로 바꾸고, 퇴실 시간에 청소 시간(10분)을 더한다
    book_time = [[int(i[0][:2]) * 60 + int(i[0][3:]), int(i[1][:2]) * 60 + int(i[1][3:]) + 10] for i in book_time]
    
    for start, end in book_time:
        for i in range(start, end):
            if time_dic.get(i) == None:
                    time_dic[i] = 1
            else:
                time_dic[i] += 1
            
    return max(time_dic.values())

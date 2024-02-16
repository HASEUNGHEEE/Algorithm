def solution(genres, plays):
    answer = []
    total_count = {} # 장르별 총 재생횟수
    genre_dic = {} # 장르별 [재생횟수 & 고유번호]
    
    # dictionary에 값을 추가한다.
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in total_count.keys():
            total_count[genre] += play
            genre_dic[genre].append([play, i])
        else:
            total_count[genre] = play
            genre_dic[genre] = [(play, i)]
    
    # total_count 딕셔너리를 재생횟수 기준(x[1])으로 내림차순 정렬한다.
    # items() : 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있는 함수
    total_count = sorted(total_count.items(), key=lambda x: x[1], reverse=True)
    
    
    for key in total_count:
        playlist = genre_dic[key[0]] # 재생횟수 & 고유번호
        playlist = sorted(playlist, key=lambda x: x[0], reverse=True) # 재생횟수 기준(x[0])으로 내림차순 정렬한다.
        for i in range(len(playlist)):
            if i == 2:
                break
            answer.append(playlist[i][1]) # answer 리스트에 고유번호를 추가한다.
            
    return answer
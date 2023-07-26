# 치환하는 함수
def replace(music):
    return music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

def solution(m, musicinfos):
    answer = []
    idx = 0
    
    # 네오가 기억한 멜로디 치환
    m = replace(m)
    
    for info in musicinfos:
        idx += 1
        info = info.split(',')
       # 재생 시간
        start_min = int(info[0][:2]) * 60 + int(info[0][3:])
        end_min = int(info[1][:2]) * 60 + int(info[1][3:])
        time = end_min - start_min
        if start_min != 0 and end_min == 0: raise KeyError
        # 악보 치환
        sheet = replace(info[3])
        # 재생된 음악
        music = sheet * (time // len(sheet)) + sheet[:time % len(sheet)]
        
        
        if m in music:
            answer.append((time, idx, info[2]))
    
    if answer:
        answer = sorted(answer, key=lambda x: (-x[0], x[1]))
        return answer[0][2]
    return "(None)"
def solution(name):
    answer = 0
    # 기본 최소 이동 횟수
    move = len(name) - 1
    
    for idx, char in enumerate(name):
        # 상하이동 횟수 구하기 => 각 문자의 가중치 계산하여 더하기
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        """
        A부터 Z까지 가중치는 다음과 같다
        A B C D E F G H I J K  L  M  N  O  P  Q  R S T U V W X Y Z
        0 1 2 3 4 5 6 7 8 9 10 11 12 13 12 11 10 9 8 7 6 5 4 3 2 1
        """
        
        # 해당 문자 다음부터 연속된 문자열 A 찾기
        next = idx + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        # 기존의 최소 이동 횟수, 연속된 문자열 A를 왼쪽에서 시작해서 찾는 방식, 연속된 문자열 A를 오른쪽에서 시작해서 찾는 방식 중 최소값 찾아 갱신하기
        move = min([move, 2*idx + len(name)-next, idx + 2*(len(name)-next)])
    
    # 상하이동 횟수에 좌우이동 횟수 더하기
    answer += move
    
    return answer
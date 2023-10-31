import sys
input = sys.stdin.readline

if __name__ == '__main__':
    while True:
        nums = list(map(int, input().split()))
        nums.sort()
        if 0 in nums:
            break
        else:
            # 삼각형 조건 만족 x
            if nums[2] >= nums[0] + nums[1]: print("Invalid")
            # 세 변의 길이 모두 같은 경우
            elif nums[0] == nums[1] and nums[1] == nums[2]: print("Equilateral")
            # 두 변의 길이만 같은 경우
            elif nums[0] == nums[1] or nums[1] == nums[2]: print("Isosceles")
            # 세 변의 길이가 모두 다른 경우
            else: print("Scalene")


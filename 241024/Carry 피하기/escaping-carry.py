def is_valid(stack, num):
    # 스택에 있는 숫자들과 num을 더했을 때 carry가 발생하는지 확인
    for s in stack:
        s_digits = list(map(int, str(s).zfill(10)))  # 각 숫자의 자릿수를 맞춰줌
        num_digits = list(map(int, str(num).zfill(10)))
        
        for i in range(10):  # 각 자리수를 비교
            if s_digits[i] + num_digits[i] >= 10:
                return False
    return True

def dfs(index, selected, nums, max_count):
    # 현재 index에서 선택한 숫자들로 탐색을 진행하는 함수
    max_count[0] = max(max_count[0], len(selected))  # 최댓값 갱신
    
    if index == len(nums):
        return
    
    # 현재 숫자를 선택하는 경우
    if is_valid(selected, nums[index]):
        selected.append(nums[index])
        dfs(index + 1, selected, nums, max_count)  # 다음 숫자 탐색
        selected.pop()  # 선택을 취소하고 다른 선택을 시도
    
    # 현재 숫자를 선택하지 않는 경우
    dfs(index + 1, selected, nums, max_count)

def solve():
    n = int(input())  # 숫자의 개수
    nums = [int(input()) for _ in range(n)]  # 주어진 숫자 리스트
    
    max_count = [0]  # 최대 개수를 저장할 리스트 (mutable로 전달하기 위해 리스트 사용)
    
    dfs(0, [], nums, max_count)  # DFS 탐색 시작
    
    print(max_count[0])

# 테스트 실행
solve()
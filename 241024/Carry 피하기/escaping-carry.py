def is_valid(stack, num):
    # 스택에 있는 숫자들과 num을 더했을 때 carry가 발생하는지 확인
    for s in stack:
        s_digits = list(map(int, str(s).zfill(10)))  # 각 숫자의 자릿수를 맞춰줌
        num_digits = list(map(int, str(num).zfill(10)))
        
        for i in range(10):  # 각 자리수를 비교
            if s_digits[i] + num_digits[i] >= 10:
                return False
    return True

def solve():
    n = int(input())  # 숫자의 개수
    nums = [int(input()) for _ in range(n)]  # 주어진 숫자 리스트
    
    stack = []
    max_count = 0
    i = 0
    
    while True:
        if i == n:
            # 모든 숫자를 처리한 후, 최대 개수를 기록하고 돌아감
            max_count = max(max_count, len(stack))
            if not stack:  # 스택이 비어있다면 종료
                break
            # 스택에서 하나를 빼고 그 위치로 돌아가서 다른 선택을 시도
            i = stack.pop()[1] + 1
        elif is_valid([x[0] for x in stack], nums[i]):
            # 스택에 현재 숫자를 추가 (숫자와 그 인덱스 기록)
            stack.append((nums[i], i))
            i += 1
        else:
            # 현재 숫자를 스택에 추가하지 않고 다음 숫자로 넘어감
            i += 1

    print(max_count)

# 테스트 실행
solve()
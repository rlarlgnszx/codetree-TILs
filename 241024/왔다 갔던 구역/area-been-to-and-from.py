import sys
input = sys.stdin.readline


n = int(input())
temp = []
cur_idx = 0
for _ in range(n):
    a,b  = input().split()
    a = int(a)
    if b=="R":
        next_idx= a+cur_idx
    else:
        next_idx = cur_idx-a
    goto = [cur_idx,next_idx]
    goto.sort()
    temp.append(goto[:])
    cur_idx = next_idx


ans = 0
temp.sort()
min_value = temp[0][0]
max_value = temp[-1][-1]
board = [0] * (abs(max_value-min_value) +1)
if min_value<0:
    for a,b in temp:
        a += abs(min_value)
        b += abs(min_value)
        board[a]+=1
        if b < len(board):
            board[b]-=1
else:
    for a,b in temp:
        board[a]+=1
        board[b]+=1
ans = 0
if board[0]>=2:
    ans+=1

for k in range(1,len(board)):
    board[k] += board[k-1]
    if board[k]>=2:
        ans+=1

print(ans)
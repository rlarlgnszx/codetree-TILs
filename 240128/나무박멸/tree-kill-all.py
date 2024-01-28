import sys
from collections import defaultdict
from heapq import heappop,heappush
n,m,k,c= map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().strip().split())) for x in range(n)]

herb = [[0] * (n ) for _ in range(n)]
a,b = len(board), len(board[0])

ans = 0
## 나무성장
def tree_grow(a,b):
    goto = [[0,1],[1,0],[-1,0],[0,-1]]
   
    update_stack = defaultdict(int)
    stack= []
    for j in range(a):
        for i in range(b):
            if board[i][j]>=1:
                stack.append([i,j])
    while stack:
        c,d = stack.pop()
        # 4방향 살핀후
        update = defaultdict(int)
        update2 = defaultdict(list)
        ## 나무 1년치 성장
        for x,y in goto:
            nx,ny  = c+x,d+y
            if 0<=nx< a and 0<=ny< b :
                # 나무가 있는 것
                if board[nx][ny]>=1:
                    update[(c,d)]+=1
                elif board[nx][ny]==0:
                    update2[(c,d)].append([nx,ny])
        ## 나무 번식 메커니즘
        # if update:
        for key in update:
            x,y = key
            board[x][y]+= update[(x,y)]
            if update2[(x,y)]:
                spride = board[x][y]//len(update2[(x,y)])
                for i,j in update2[(x,y)]:
                    update_stack[(i,j)] += spride
    for key in update_stack:
        x,y  = key
        board[x][y] += update_stack[key]

# tree_grow(a,b)

def step_three(a,b):
    global ans

    dxs, dys = [-1, 1, 1, -1], [-1, -1, 1, 1]

    max_del, max_x, max_y = 0, 0 , 0 
    for i in range(0, n):
        for j in range(0, n):
            
            if board[i][j] <= 0: 
                continue
            cnt = board[i][j]
            for dx, dy in zip(dxs, dys):
                nx, ny = i, j
                for _ in range(k):
                    nx, ny = nx + dx, ny + dy
                    if not (0<=nx< a and 0<=ny< b):
                        break
                    if board[nx][ny] <= 0: 
                        break
                    cnt += board[nx][ny]

            if max_del < cnt:
                max_del = cnt
                max_x = i
                max_y = j

    ans += max_del
    # print(max_x,max_y)
    # 찾은 칸에 제초제
    if board[max_x][max_y] > 0:
        board[max_x][max_y] = 0
        herb[max_x][max_y] = c

        for dx, dy in zip(dxs, dys):
            nx, ny = max_x, max_y
            for _ in range(k):
                nx, ny = nx + dx, ny + dy
                if  not (0<=nx< a and 0<=ny< b):
                    break
                if board[nx][ny] < 0: 
                    break
                if board[nx][ny] == 0:
                    herb[nx][ny] = c
                    break

                board[nx][ny] = 0
                herb[nx][ny] = c


# step_three(a,b)

def delete_herb():
    for i in range(n):
        for j in range(n): 
            if herb[i][j] > 0: 
                herb[i][j] -= 1

# tree_grow(a,b)
# step_three(a,b)
# delete_herb()

for _ in range(m):
    # 1단계 : 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다.
    tree_grow(a,b)

    # 제초제의 기간을 1년 감소시킵니다.
    delete_herb()

    # 3단계 : 가장 많이 박멸되는 칸에 제초제를 뿌립니다.
    step_three(a,b)

print(ans)
## 방식
## 분당 출발


goto=[[-1,0],[0,-1],[0,1],[1,0]]
## 사람이 편의점 방문시 긺막힘
## t <=m이라면 편의점에서 가까운 베이스캠프

import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().strip().split())) for x in range(n)]
store = [list(map(int,sys.stdin.readline().strip().split())) for x in range(m)]
## 초기 세팅
base_camp = set()
for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            base_camp.add((i,j))
moving_person = []
## 최단거리구하기
def find_basecamp(i):
    x,y = None,None
    c,d = store[i]
    c-=1
    d-=1
    min_lenghth = float('inf')
    count = 0
    for (a,b) in base_camp:
        if abs(a-c) + abs(b-d) < min_lenghth:
            x,y = a,b
            min_lenghth = abs(a-c)+abs(b-d)
            count = i
    board[x][y]=-1
    moving_person.append([x,y])
    base_camp.remove((x,y))


def bfs(start,end):
    visited= set()
    e,f = start
    stack= deque([[e,f,-1]])
    fx,fy = end
    one_count = False
    while stack:
        k = stack.popleft()
        x,y,c = k
        for i,(a,b) in enumerate(goto):
            if 0<=a+x<n and 0<=b+y<n and board[a+x][b+y]!=-1 and (a+x,y+b) not in visited:
                visited.add((a+x,y+b))
                if a+x==fx and b+y==fy:
                    return c
                if one_count:
                    stack.append([a+x,b+y,c])
                else:
                    stack.append([a+x,b+y,i])
        one_count =True
    
ans = m

for i in range(m):
    find_basecamp(i)
    len2  = len(moving_person)
    print("START:",moving_person)
    for i in range(len2):
        x,y = moving_person[i]
        c,d = store[i]
        print(store[i])
        c-=1
        d-=1

        cango = bfs(moving_person[i],[c,d])
        if cango==0:
            moving_person[i]= [x-1,y]
        elif cango==1:
            moving_person[i]= [x,y-1]
        elif cango==2:
            moving_person[i]= [x,y+1]
        elif cango==3:
            moving_person[i]= [x+1,y]
        ## 도착했을시 pop
        print(moving_person)
        if moving_person[i]==[c,d]:
            board[x][y]=-1
            store.pop(i)
            moving_person.pop(i)
print(moving_person)


# while moving_person:
#     # one_minute_move_person()
#     ans+=1
#     for i in range(len2):
#         cango = bfs(moving_person[i],store[i])
#         if cango==0:
#             moving_person[i]= [moving_person[i][0]-1,moving_person[i][1]]
#         elif cango==1:
#             moving_person[i]= [moving_person[i][0],moving_person[i][1]-1]
#         elif cango==2:
#             moving_person[i]= [moving_person[i][0],moving_person[i][1]+1]
#         elif cango==3:
#             moving_person[i]= [moving_person[i][0]+1,moving_person[i][1]]
#         if moving_person[i]==store[i]:
#             board[moving_person[i][0]][moving_person[i][1]]=-1
#             store.pop(i)
#             moving_person.pop(i)
# print(ans)
import sys
input =sys.stdin.readline

n,k = map(int,input().split())
temp = [list(map(int,input().split())) for j in range(n)]
temp.sort()
temp.sort(key=lambda x:x[1])
ans = 0
ticket = 1
for a,b in temp:
    if k-(a+b) < 0 and ticket:
        ticket-=1
        if k-(a//2)-b >=0:
            ans+=1
            k-= ((a//2)+b)
        else:
            break
    elif k-(a+b)>=0:
        k-= (a+b)
        ans+=1
print(ans)
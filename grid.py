def dfs(n,tst,ci,cj):
    if n==7:
        sset.add(tst) #중복제거
        return

    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = ci+di,cj+dj
        if 0<=ni<4 and 0<=nj<4:
            dfs(n+1,tst+arr[ni][nj],ni,nj)


T = int(input())
for tc in range(1,T+1):
    arr = [input().split() for _ in range(4)]
    sset = set()

    for i in range(4):
        for j in range(4):
            dfs(1,arr[i][j],i,j)
    ans = len(sset)

    print(f'#{tc} {ans}')

    #문자열보다 int로 받는것이 빠르게 처리됨

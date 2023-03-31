def dfs(n,sm):
    global ans
    if ans <= sm:
        return

    if n>12:
        ans = min(ans,sm)
        return

    dfs(n+1,sm+day*lst[n])
    dfs(n+1,sm+mon)
    dfs(n+3,sm+mon3)
    dfs(n+12,sm+year)


T = int(input())
for tc in range(1,T+1):
    day,mon,mon3,year =map(int,input().split())
    lst = [0] + list(map(int,input().split()))

    ans = 3000*365  #최악의경우
    dfs(1,0)

    print(f'{tc} {ans}')


# def dfs(n,sm):
#     global ans
#     if ans <= sm:
#         return
#
#     if n>12:
#         ans = min(ans,sm)
#         return
#
#     dfs(n+1,sm+day*lst[n])
#     dfs(n+1,sm+mon)
#     dfs(n+3,sm+mon3)
#     dfs(n+12,sm+year)


# T = int(input())
# for tc in range(1,T+1):
#     day,mon,mon3,year =map(int,input().split())
#     lst = [0] + list(map(int,input().split()))
#
#     s = [0]*13
#     for i in range(1,13):
#         #가능한 방법중 i달까지의 최소비용
#         s[i] = s[i-1]*day*lst[i] #일권
#         s[i] = min(s[i],s[i-1]+mon) #월간권
#         if i>=3:
#             s[i] = min(s[i],s[i-3]+mon3)
#         if i >= 12:
#             s[i] = min(s[i], s[i - 12] + year)
#         ans = s[12]
#
#     print(f'#{tc} {ans}')
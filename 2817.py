#백트래킹:가능한 모든경우-tree 를 풀어서 답냄
#1)반드시 끝나는 종료조건 설정 (n:숫자번호)
#2)시각적으로 표현 이진트리-멀티트리 고려
#부분집합


def dfs(n,sm):
    global ans
    if n == N: #n에 관한 걸로 종료조건 반드시 여기서만 정답처리
        if sm==K:
            ans += 1
        return
    #하부호출 가능한 경우에만
    #포함
    dfs(n+1,sm+lst[n])
    #포함x
    dfs(n+1,sm)

T = int(input())
for tc in range(1,T+1):
    N,K =map(int,input().split())
    lst = list(map(int,input().split()))

    ans = 0
    dfs(0,0) #dfs(n,sm)

    print(f'{tc} {ans}')


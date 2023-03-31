# T = int(input())
#
# # (current, next) = 0,1 -> 1,2 -> 2,0
# def dfs(current, tmp):
#     global res
#     if tmp < res:
#         if 0 not in visited[1:]:  # 전부 방문했다면
#             res = min(res, tmp + a[current][0])  # 결과값 갱신하고 함수 종료
#             return
#         for next in range(1, N):
#             if a[current][next] != 0 and visited[next] == 0:
#                 visited[next] = 1
#                 dfs(next, tmp + a[current][next])
#                 visited[next] = 0
#
#
# for tc in range(1, T+1):
#     N = int(input())
#     a = [list(map(int, input().split())) for _ in range(N)]
#
#     res = 10000
#     for i in range(1, N):
#         visited = [0] * N
#         visited[i] = 1
#         dfs(i, a[0][i])  # current_y, tmp_sum
#     print("#{} {}".format(tc, res))
#
#
#
#


def dfs(i,sm):
    global ans

    if i == N:


    for k in range(N):




T = int(input().split())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)] #배열안에 배터리 사용량 주어짐

    ans = 10000 #최솟값을 구해야하므로
    visited = [ [False]*N ] #각구역을 한번씩만 방문해야하므로 방문체크
    for i in range(1,N): #사무실부터 도니까 1부터 넣어줌
        visited[i] = True #방문체크
        dfs(i,arr[0][i])  #탐색순번, 좌표

    print(f'{tc} {ans}')

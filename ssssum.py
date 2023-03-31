# # 방향 벡터
# dx = [1, 0]
# dy = [0, 1]
#
#
# # 오른쪽 아래까지 이동하는 함수
# def gogo(x, y, total):
#     global answer
#
#     if answer < total:  # 이미 합이 크다면 가볼 필요 없음
#         return
#
#     if x == y == n - 1:  # 오른쪽 아래까지 왔다면
#         if total < answer:  # 지금까지 지나온 길의 합이 answer에 들어있는 값보다 작은 경우 갱신
#             answer = total
#         return
#
#     for i in range(2):  # 오른쪽, 아래 이동
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx <= n - 1 and ny <= n - 1:  # 주어진 범위 안
#             gogo(nx, ny, total + arr[ny][nx])  # 그렇다면 이동
#
#
# tc = int(input())
# for idx in range(1, tc + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#
#     answer = 99999999  # 정답 초기화
#     gogo(0, 0, arr[0][0])
#     print('#{} {}'.format(idx, answer))




# 오른쪽이나 아래로만 이동
# 시작은 (0,0)에서부터 도착은 (N-1,N-1)
dr = [0,1]
dc = [1,0]


def gogo(row,col,sm):
    global ans

    if sm > ans: #지금하고 있는게 이전 값보다 크면 더 볼 필요 없음
        return

    if row == N-1 and col == N-1:
        ans = min(sm,ans)
        return

    for i in range(2): #오른쪽이나 아래로 이동해야하니까
        nr = row+dr[i]
        nc = col+dc[i]
        if 0<=nr<N and  0<=nc<N: #좌표 유효성검사
            gogo(nr,nc,sm+arr[nr][nc])


T = int(input()) #테스트케이스
for tc in range(1,T+1):
    N = int(input()) #가로세로칸 수
    #N*N의 배열
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 50000

    gogo(0,0,arr[0][0]) #(0,0)에서부터 시작해서 값은 0을 가지고 탐색한다

    print(f'#{tc} {ans}')













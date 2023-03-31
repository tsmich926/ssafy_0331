# T = int(input())
# for tc in range(1,T+1):
#     lst = []
#     N = int(input()) #사용신청서
#     for _ in range(N): #신청서수만큼 작업시간 입력받기
#         plst = list(map(int,input().split()))
#     #끝나는 시간이 빠른것부터 정렬
#     plst.sort(key=lambda x: x[1],reverse=False) #두번째 값-끝나는시각을 기준으로 내림차순 정렬
#
#     ans = 0
#     last = 0
#     for s,e in lst:
#         if s <= last: #이전회의가 끝나는시각보다 다음회의가 시작하는 시간이 더 나중이거나 같아야함
#             ans += 1
#             last = e    #끝나는 시간을 시작 시간으로 바꿔준다.
#
#     print(f'{tc} {ans}')


#처음 1이 나타난 곳과 마지막으로 1이 나타난곳을 찾는다
# 처음 1이 나타난곳을 찾으려면 앞에서부터 탐색 찾으면 멈춤
# 마지막으로 1이 나타난곳을 찾으려면 뒤에서부터 탐색 찾으면 멈춤


T = int(input())
for tc in range(1,T+1):
    N,M= map(int,input().split()) #세로,가로
    arr = [list(input()) for _ in range(N)]
    for i in range(N): # 끝에서 부터 가로로 탐색
        if '1' in arr[i]:
            for j in range(N-1,1,-1):
                if arr[i][j] == '1':
                    scret = arr[i][j-57:j]
                    break
    print(scret)


        
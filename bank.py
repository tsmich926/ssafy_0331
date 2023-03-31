# def twos(i,k,num2):
#     n2 = len(num2)
#     if i == n2:
#         return
#
#     if num2[i] == '0':
#         num2[i] == '1'
#     else:
#         num2[i] == '0'
#
#     #바꾸는 경우
#     twos(i+1,k,num2)
#     #안바꾸는 경우
#     twos(1+1)
#
#     for i in range(n2): #0,1,2,3..번째 자릿수 바꾸기
#         twos(i,num2)
#
# def threes(num3):
#     n3= len(num3)


def twos(num2):
    lst = []
    n2 = len(num2)
    for i in range(n2): #0,1,2,3..번째 자릿수 바꾸기
        if num2[i] == 0:
            num2[i] = 1
        else:
            num2[i] = 0
        lst.append(num2)


def threes(num3):
    n3= len(num3)
    for i in range(n3):





T = int(input())
for tc in range(1,T+1):
    num2 = list(map(int,input())) #str형식으로 입력받음
    num3 = list(map(int,input()))


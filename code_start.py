def getcode(s):
    PATT = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
    return PATT[s]


TC = int(input())
for tc in range(1, TC + 1):
    N, M = map(int, input().split()) #세로,가로

    arr = [input() for _ in range(N)] #직사각형배열
    for row in range(N):
        if arr[row].count('1') > 0:
            st = M - 1 - arr[row][::-1].index('1') - 55
            break

    codes = []
    for code in range(8):
        codes.append(getcode(arr[row][st:st + 7]))
        st += 7

    # sum1=0
    # sum2=0
    # sum1 = codes[0] + codes[2] + codes[4] +codes[6]
    # sum2 = (codes[1] + codes[3] + codes[5]+codes[7]
    # an = (sum1 * 3) + sum2
    # if an%10 == 0:
    #     ans = sum1+sum2
    # else:
    #     ans = 0
    #
    # print(f'#{tc} {ans}')
    sumV = 0

    for i in range(8):
        if i % 2 == 0:
            sumV += codes[i] * 3
        else:
            sumV += codes[i]

    if sumV % 10:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {sum(codes)}')
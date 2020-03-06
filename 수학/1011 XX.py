# 답 - 고민중..
import sys

a = int(sys.stdin.readline().rstrip())

for i in range(a):
    str = sys.stdin.readline().rstrip()
    dist = int(str.split()[1]) - int(str.split()[0])
    cnt = 0
    cntr = 0
    i = 1
    while True:
        if dist > cnt:
            cnt += i
            cntr += 1
            if dist > cnt:
                cnt += i
                cntr += 1
                i += 1
        else:
            break
    print(cntr)
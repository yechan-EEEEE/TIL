"""
5

4 10
1 2 3 4
            4
4 11
1 2 3 4
            5
1 3
5
            2
6 6
1 3 5 2 4 6
            3
6 10000000
1 3 5 2 4 6
            2857144
"""
import sys
input = sys.stdin.readline
135246
x = 10000000
y = 0
cnt = 0
while True:
    y+=1
    cnt+=1
    if y>x:
        break
    y+=3
    cnt+=1
    if y>x:
        break
    y+=5
    cnt+=1
    if y>x:
        break
    y+=2
    cnt+=1
    if y>x:
        break
    y+=4
    cnt+=1
    if y>x:
        break
    y+=6
    cnt+=1
    if y>x:
        break
print(cnt)
import sys
input = sys.stdin.readline

bottles = map(int, input().split())
price = sum(bottles) * 5
print(price)
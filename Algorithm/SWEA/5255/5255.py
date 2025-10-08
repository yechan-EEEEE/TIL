T = int(input())

for t in range(1, T + 1):
    N = int(input())
    tiles = [0] * (N + 1)
    tiles[1] = 1
    tiles[2] = 3
    tiles[3] = 6

    for i in range(4, N + 1):
        tiles[i] = tiles[i-1] + 2 * tiles[i-2] + tiles[i-3]
    
    print(f"#{t} {tiles[N]}")

n, m, k = [int(x) for x in input().split()]
canwin = False
for i in range(k):
        x, y = [int(x) for x in input().split()]
        if (min(min(x-1,n-x),min(y-1,m-y))<=4):
                canwin = 1
print("YES" if canwin else "NO")

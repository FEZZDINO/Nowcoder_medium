#python 3.5.2
import sys 
while True:
    line = sys.stdin.readline()
    if not line:
        break
    num = int(line.split()[0])
     
    min_x = 1e+9
    max_x = -1e+9
    min_y = 1e+9
    max_y = -1e+9
 
    for i in range(num):
        line = sys.stdin.readline()
        a = list(map(int, line.split()))
        min_x = min(min_x, a[0])
        max_x = max(max_x, a[0])
        min_y = min(min_y, a[1])
        max_y = max(max_y, a[1])
 
    ans = max(max_x - min_x, max_y - min_y)**2
 
    print(ans)
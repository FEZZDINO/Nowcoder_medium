#python 3.5.2

import sys 
while True:

    try:
        line = input().split()
        list2 = []
        flag= -1
        #print(int(line[1]))
        for i in range(int(line[1])):
            k = input()
            list2.append(int(k))
        #print(list2)
        a = [0]*int(line[0])
        b = int(line[1])
        #print(line[0])
        for i in range(0, b):
            k = list2[i] % len(a)
            if a[k] == 0:
                a[k] = 1
                #print(k)
            else:
                flag = i+1
                break
        print(flag)
    except:
        break
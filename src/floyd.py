
import math
import time
import random
import math

def floyd(graph):
    
    dis = graph.copy()
    
    for k in range(len(graph)):
        dis_k = dis.copy()
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dis[i][k] + dis[k][j] < dis[i][j]:
                    dis_k[i][j] = dis[i][k] + dis[k][j]
        dis = dis_k.copy()
    
    return dis_k

n = 50 #n值为点的个数
s = [[math.inf for i in range(n)]for i in range(n)]
for i in range(n):
    s[i][i] = 0
for i in range(n - 1):
    num1 = random.randrange(i +1,n)
    num2 = random.randrange(i + 1,n)
    s[i][num1] = random.randrange(2000,4000)
    s[i][num2] = random.randrange(2000,4000)
    s[num1][i] = s[i][num1]
    s[num2][i] = s[i][num2]
inf = math.inf

starttime = time.time()
h = floyd(s)
endtime = time.time()
print("运行时间",endtime - starttime)


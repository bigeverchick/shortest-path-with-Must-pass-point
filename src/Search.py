
import random
graph =[[1,2, 3],[0,3,4],[0,4, 5, 6],[0, 1,2, 6,10],
[1,2, 5, 7,8],[2,4,6,8],[2,3,5,8,9],[4,8,10],
[4,5,6,7,9,10],[6,8,10],[3,7,8,9]]
path = [0]
visited = [0]

def search(i): #i为第i次，i为0，path[0]=0,graph[0]= (1,3)
    
    if set(path) == set([q for q in range(len(graph))]):
        return path #结束搜索
    temp = graph[path[i]] #i次搜索到的点的邻接点
    
    if set(visited) > set(list(temp)):#visited包含了temp
        for t in range(1,len(path) + 1):
            path.append(path[i - t])
            temp_t = graph[path[len(path) - 1]]
            if set(visited) > set(temp_t):
                continue
            else:
                return search(len(path) -1)
             #回到上一个有未经邻接点的点
        
    for j in temp:
        #如果邻接的点中有没经过（不在visited中）的点，作为下一个
        
        if j not in visited:
            path.append(j)
            visited.append(j)
            return search(i+1)
    return -1
res = set()
for times in range(100):
    for n in range(len(graph)):
        random.shuffle(graph[0])
    for n in range(1,len(graph)):
        path= [0]
        visited = [0]
        path[0] = n
        visited[0] = n

        res.add(tuple(search(0)))



# In[ ]:





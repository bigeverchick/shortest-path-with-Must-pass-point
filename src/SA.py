import copy
import math
import random
import matplotlib.pyplot as plt
#需要先在此处定义distance矩阵

#初始温度
T0 = 1000
# 终止温度
Tend = 1e-3
#温度下的迭代次数（链长）
L = 250
#降温速率
q = 0.9
res = set() #存储路径
#产生新的路径解
def gen_new_path(path):
    new_path = copy.copy(path)
    idx1 = random.randint(0, len(path) - 1)
    idx2 = random.randint(0, len(path) - 1)
    #随机交换两个城市
    temp = new_path[idx1]
    new_path[idx1] = new_path[idx2]
    new_path[idx2] = temp
    return new_path


#计算路径总距离
def path_distance(path, distance):
    total_distance = 0
    for i in range(len(path) - 1):
            total_distance += distance[path[i]-1][path[i + 1]-1]
    return total_distance


#Metropolis准则函数
def metropolis(old_path, new_path, distance, t):
    delta = path_distance(new_path, distance) - path_distance(old_path, distance)
    if delta < 0:
        return copy.copy(new_path), path_distance(new_path, distance)
    #若新路径能量高于旧路径，则按exp(-delta/t)概率接受新路径解
    if math.exp(-delta/t) >= random.uniform(0, 1):
        return copy.copy(new_path), path_distance(new_path, distance)
    return copy.copy(old_path), path_distance(old_path, distance)
# 绘制进化过程
def draw_evolution(evolution):
    x = [i for i in range(len(evolution))]
    plt.clf()
    plt.plot(x, evolution)
    plt.savefig('tsp_sa_evolution.png', dpi=800)
# 模拟退火算法
def simulated_annealing():
    #初始路径解使用0到n的顺序
    path = [i for i in range(1,len(distance)+1)]

    # 初始路线长度
    total_distance = path_distance(path, distance)
    print("初始路线：", [p for p in path])
    print("初始总距离：", total_distance)
    # 温度
    t = T0
    # 进化过程，每一次迭代的路径总距离
    evolution = []
    # 循环直到冷却后停止
    while t > Tend:
        for _ in range(L):
            # 产生新路径
            new_path = gen_new_path(path)
            # 更新最佳路径及对应的距离
            path, total_distance = metropolis(path, new_path, distance, t)
            # 更新进化过程
            evolution.append(total_distance)
            if total_distance <= 20:
                res.add(tuple(new_path))
                res.add(total_distance)
        #降温
        t = t * q
    print("最佳路线：", [p for p in path])
    print("最佳距离：", total_distance)
    #迭代过程
    draw_evolution(evolution)


if __name__ == "__main__":
    simulated_annealing()




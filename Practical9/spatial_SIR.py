import numpy as np
import matplotlib.pyplot as plt

# 模型参数
size = 100
beta = 0.3
gamma = 0.05
time_steps = 100

# 初始化：全部易感（0）
pop = np.zeros((size, size), dtype=int)

# 随机选一个点感染
outbreak = np.random.choice(size, 2)
x0, y0 = outbreak[0], outbreak[1]
pop[x0, y0] = 1

# 绘图初始状态
plt.figure(figsize=(6,4), dpi=150)
plt.imshow(pop, cmap='viridis', interpolation='nearest')
plt.title('Time 0')
plt.show()

# 时间循环
for step in range(time_steps):
    # 复制当前状态，避免边改边算出错
    current = pop.copy()
    # 找到所有感染点
    infected = np.argwhere(current == 1)
    
    for (i,j) in infected:
        # 恢复过程
        if np.random.rand() < gamma:
            pop[i,j] = 2
        
        # 感染8邻域
        for di in [-1,0,1]:
            for dj in [-1,0,1]:
                if di ==0 and dj ==0:
                    continue
                ni = i + di
                nj = j + dj
                if 0<=ni<size and 0<=nj<size:
                    if current[ni, nj] == 0 and np.random.rand() < beta:
                        pop[ni, nj] = 1
    
    # 每10步画一次图
    if step %10 ==0:
        plt.imshow(pop, cmap='viridis', interpolation='nearest')
        plt.title(f'Time {step}')
        plt.show()
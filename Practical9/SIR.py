# 导入需要的库
import numpy as np
import matplotlib.pyplot as plt

# 模型参数设置
N = 10000          # 总人口
beta = 0.3         # 感染率
gamma = 0.05       # 恢复率
time_steps = 1000  # 模拟时间步数

# 初始状态
S = N - 1  # 易感者：总人数 - 1个初始感染者
I = 1      # 感染者：初始1人
R = 0      # 恢复者：初始0人

# 用于保存每一步数据的列表
S_list = [S]
I_list = [I]
R_list = [R]

# 时间循环
for t in range(time_steps):
    # 计算新感染人数：随机按概率选择
    new_infected = np.random.binomial(S, beta * (I / N))
    # 计算新恢复人数
    new_recovered = np.random.binomial(I, gamma)
    
    # 更新三类人群数量
    S = S - new_infected
    I = I + new_infected - new_recovered
    R = R + new_recovered
    
    # 记录到列表
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

# 绘图
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S_list, label='Susceptible')
plt.plot(I_list, label='Infected')
plt.plot(R_list, label='Recovered')
plt.xlabel('Time steps')
plt.ylabel('Number of people')
plt.title('Stochastic SIR Model')
plt.legend()
plt.savefig('SIR.png', dpi=150)
plt.show()
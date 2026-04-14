import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N = 10000
beta = 0.3
gamma = 0.05
time_steps = 1000

# 要测试的疫苗接种比例
vaccine_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
plt.figure(figsize=(6,4), dpi=150)

# 遍历每个疫苗比例
for idx, v in enumerate(vaccine_rates):
    # 初始接种人数
    V = int(N * v)
    
    # 修复点1：强制确保 S >= 0，防止 n < 0 报错
    S = max(0, N - V - 1) 
    I = 1
    R = 0
    I_list = [I]
    
    for t in range(time_steps):
        # 修复点2：再次确保S非负，防止循环内波动导致异常
        S = max(0, S)
        if S <= 0 or I <= 0:
            # 若无易感者或感染者，后续传播停止
            I_list.extend([0] * (time_steps - t))
            break
            
        new_infected = np.random.binomial(S, beta * (I / N))
        new_recovered = np.random.binomial(I, gamma)
        
        S = S - new_infected
        I = I + new_infected - new_recovered
        R = R + new_recovered
        I_list.append(I)
    
    # 绘制不同疫苗率的感染曲线
    plt.plot(I_list, label=f'Veccine {int(v*100)}%', color=cm.viridis(idx*25))

plt.xlabel('Time steps')
plt.ylabel('Infected people')
plt.title('SIR with Vaccination')
plt.legend(bbox_to_anchor=(1.05,1), loc='upper left')
plt.tight_layout()
plt.savefig('SIR_vaccine.png', dpi=150)
plt.show()
import numpy as np
import matplotlib.pyplot as plt

T_comp = 2e-09
T_read = 1e-04
T_comm = 1e-06
P = np.arange(1,1000+1)

N = 10 ** np.arange(6,10)
plt.figure(figsize = (12,8))
plt.title("Efficiency Curve")
plt.xlabel("Number of Processors")
plt.ylabel("Efficiency")

plt.text(32,0.0007,'N = 10^6',fontsize = 12)
plt.text(100,0.0003,'N = 10^7',fontsize = 12)
plt.text(316,0.0001,'N = 10^8',fontsize = 12)
plt.text(800,0.0000,'N = 10^9',fontsize = 12)


for i in N:
    Ts = i * T_comp
    Tp = T_comp * (P + i/P) + T_read + 2 * (P-1) * T_comm
    plt.plot(P,Ts/(i * Tp)*100)
    print("Serial algorithm time for N = ",i,"is",Ts)
    print("For N =",i,"best efficiency value is",np.max(Ts/(i * Tp)*100), "with P", 
          int(np.where(Tp == np.min(Tp))[0]+1))

plt.show()

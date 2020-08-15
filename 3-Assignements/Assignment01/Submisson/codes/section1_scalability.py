import numpy as np
import matplotlib.pyplot as plt

T_comp = 2e-09
T_read = 1e-04
T_comm = 1e-06
P = np.arange(1,1000+1)

N = 10 ** np.arange(6,10)
plt.figure(figsize = (12,8))
plt.title("Scalability Curve")
plt.xlabel("Number of Processors")
plt.ylabel("Scalability")

plt.text(450,-15,'N = 10^6',fontsize = 12)
plt.text(450,50,'N = 10^7',fontsize = 12)
plt.text(450,150,'N = 10^8',fontsize = 12)
plt.text(450,450,'N = 10^9',fontsize = 12)


for i in N:
    Ts = i * T_comp
    Tp = T_comp * (P - 1 + i/P) + T_read + 2 * (P-1) * T_comm
    plt.plot(P,Ts/Tp)
    print("Serial algorithm time for N = ",i,"is ",Ts)
    print("For N =",i,"best speed up value when P is",int(np.where(Tp == np.min(Tp))[0]+1),"\n")

plt.show()

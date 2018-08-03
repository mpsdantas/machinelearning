import matplotlib.pyplot as plt
import numpy as np

x = np.matrix('1872; 1890; 1900; 1920; 1940; 1950; 1960; 1970; 1980; 1991; 1996');
y = np.matrix('9.9 ;14.3 ;17.4 ;30.6 ;41.2 ;51.9 ;70.2 ;93.1 ;119.0 ;146.2 ;157.1')
plt.plot(x,y, 'ro')

def mmq(x, y, grauDoAjuste):
    A = np.ones((x[:,0].size,1))
    for i in range(1,grauDoAjuste+1):
        A = np.concatenate((A,np.power(x,i)), axis=1)
    AtA = np.matmul(A.T,A)
    
    AtY = np.matmul(A.T,y)
    x = np.linalg.solve(AtA, AtY)
    return x
def resultMmqFunction(x, B):
    soma = 0
    for i in range(B.size):
        soma = soma + B[i,0]*np.power(x,i)
    return soma
B = mmq(x, y, 2)
print(B)

plt.plot(2010,resultMmqFunction(2010,B), 'bo')
#plt.plot(mmqFunction(x, B))

plt.show()
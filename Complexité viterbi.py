import matplotlib.pyplot as plt
x=[6,12,30,120,300,600,900,1800,5400,6000,15000,30000,60000,90000]
y=[0.0003,0.00034,0.000565,0.000988,0.00256,0.00493,0.0084,0.028,0.173,0.214,1.212,4.507,17.31,39.88]
plt.plot(x,y)
plt.xlabel('Taille de la séquence observée ')
plt.ylabel('Secondes')
plt.title('Complexité du code de Viterbi')
plt.show()
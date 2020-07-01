import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
y=[8.17*(10**-5),4.88*(10**-5),0.0001,0.0005,0.0009,0.003,0.0108,0.247,0.0838,0.264,0.858,2.95,9.77,30.82]
plt.plot(x,y)
plt.xlabel('Taille de la séquence observée ')
plt.ylabel('Secondes')
plt.title('Complexité du code Naif')
plt.show()
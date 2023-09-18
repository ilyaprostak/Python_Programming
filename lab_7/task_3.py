import numpy as np
import matplotlib.pyplot as plt

figure = plt.figure()
figure.suptitle('График функции:')
graph = figure.add_subplot(projection='3d')
x = np.linspace(-np.pi, np.pi)
y = x
z = np.tan(x)
graph.plot(x, y, z, color='red')
graph.set_xlabel('x')
graph.set_ylabel('y')
graph.set_zlabel('z')
plt.show()
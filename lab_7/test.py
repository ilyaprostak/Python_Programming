import numpy as np
import csv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


arr = np.genfromtxt('data1.csv', delimiter=',')
arr = arr[1:]
daysInYear = 365.25

age = np.int_(arr[:,1] / daysInYear)

fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot()
ax.hist(age, 100, (50, 60))
ax.grid()
plt.show()
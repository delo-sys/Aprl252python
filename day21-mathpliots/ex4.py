import matplotlib.pyplot as plt 
import numpy as np
x=np.array([1,2,3,4])
y=np.array([400,500,80,200])

plt.hist(y,bins=4)
plt.show()
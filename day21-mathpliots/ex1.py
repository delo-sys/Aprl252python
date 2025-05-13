import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([0,2,4,6,8])
ypoint=np.array([2,8,0,12,14])

xpoint1=np.array([1,2,3,4,5])
ypoint1=np.array([5,10,15,25,30])
plt.plot(xpoint,ypoint,marker="o")
plt.plot(xpoint1,ypoint1,'*:g')
plt.show()

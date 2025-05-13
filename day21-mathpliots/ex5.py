import matplotlib.pyplot as plt 
import numpy as np

w = [300, 500, 200, 100, 400]
labels = ['food', 'rent', 'clothes', 'bills', 'bank']

plt.pie(w, labels=labels, startangle=90, shadow=False)
plt.legend(labels)
plt.show()

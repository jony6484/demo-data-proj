# %%
import numpy as np 
print("hello")

import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x)

plt.plot(x, y)
plt.show()

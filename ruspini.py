#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("ruspini.csv")
print(data)

#visualisasi
plt.figure('Ruspini')
plt.scatter(data['x'].values,
            data['y'].values,
            color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
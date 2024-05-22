# Find-S-Algorithm

import pandas as pd
import numpy as np

data = pd.read_csv("./dataset1.csv")
features = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

for i,val in enumerate(target):
    if val == 'yes':
        specific_h = features[i].copy()
        break
print(specific_h)
for i,val in enumerate(features):
    if target[i] == 'yes':
        for x in range(len(specific_h)):
            if val[x] != specific_h[x]:
                specific_h[x] = '?'
print(specific_h)
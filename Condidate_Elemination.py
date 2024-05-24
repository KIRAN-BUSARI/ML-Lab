# Candidate Elimination Algorithm

import numpy as np
import pandas as pd

data = pd.read_csv('./Datasets/dataset2.csv')

features = np.array(data)[:,:-1]

target = np.array(data)[:,-1]

print("Initialization of specific Hypothesis and General Hypothesis")
specific_h = features[0].copy()

general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]

for i,h in enumerate(features):
    if target[i] == 'yes':
        for x in range(len(specific_h)):
            if h[x] != specific_h[x]:
                specific_h[x] = '?'
                general_h[x][x] = '?'

    if target[i] == 'no':
        for x in range(len(specific_h)):
            if h[x] != specific_h[x]:
                general_h[x][x] = specific_h[x]
            else:
                general_h[x][x] = '?'
            print(specific_h,'\n')
            print(general_h,'\n')

indices = [i for i,val in enumerate(general_h) if val == ['?','?','?','?','?','?']]

for i in indices:
    general_h.remove(['?','?','?','?','?','?'])

print("\n Final Specific Hypothesis: ", specific_h,sep='\n')
print("\n Final General Hypothesis: ", general_h,sep='\n')
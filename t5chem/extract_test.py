import pandas as pd
import os
import sys

df = pd.read_csv(sys.argv[1])
df2 = pd.read_csv(sys.argv[2])
#print(df.head())

#df = df.drop(0)
source = []
for item1, item2 in zip(df2["Reactant SMILES"], df["prediction_1"]):
    source.append(item1+'.'+item2)
target = df2["Product SMILES"]

with open(os.path.join(sys.argv[3], 'test.source'), 'w') as fout:
    for item in source:
        fout.write(item+'\n')

with open(os.path.join(sys.argv[3], 'test.target'), 'w') as fout:
    for item in target:
        fout.write(item+'\n')
#df.to_csv('predictions_try.csv', index = False, encoding = 'utf8')


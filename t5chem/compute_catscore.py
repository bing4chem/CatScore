import pandas as pd
import sys

df = pd.read_csv(sys.argv[1])
total_llh = 0
total_words = 0
for row in df.iloc:
    total_llh += row['log_likelihood_total']
    total_words += row['num_words']

print (total_llh/total_words)

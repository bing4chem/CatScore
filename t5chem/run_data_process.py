import pandas as pd

path_to_file = "/scratch/by2192/reaction_prediction/t5chem/t5chem/sample_10_wo.csv"
data = pd.read_csv(path_to_file,encoding='utf-8')

# create an empty dataframe
df = pd.DataFrame(columns = ['Reactants', 'Predictions', 'Label'])

# target,label,source,prediction_1,prediction_2,prediction_3,prediction_4,prediction_5,prediction_6,       prediction_7,prediction_8,prediction_9,prediction_10,rank
for i in range(80000,len(data)):  
    df.loc[i*10] = [data.loc[i,'source'], data.loc[i,'prediction_1'], data.loc[i,'label']]
    df.loc[i*10+1] = [data.loc[i,'source'], data.loc[i,'prediction_2'], data.loc[i,'label']]
    df.loc[i*10+2] = [data.loc[i,'source'], data.loc[i,'prediction_3'], data.loc[i,'label']]
    df.loc[i*10+3] = [data.loc[i,'source'], data.loc[i,'prediction_4'], data.loc[i,'label']]
    df.loc[i*10+4] = [data.loc[i,'source'], data.loc[i,'prediction_5'], data.loc[i,'label']]
    df.loc[i*10+5] = [data.loc[i,'source'], data.loc[i,'prediction_6'], data.loc[i,'label']]
    df.loc[i*10+6] = [data.loc[i,'source'], data.loc[i,'prediction_7'], data.loc[i,'label']]
    df.loc[i*10+7] = [data.loc[i,'source'], data.loc[i,'prediction_8'], data.loc[i,'label']]
    df.loc[i*10+8] = [data.loc[i,'source'], data.loc[i,'prediction_9'], data.loc[i,'label']]
    df.loc[i*10+9] = [data.loc[i,'source'], data.loc[i,'prediction_10'], data.loc[i,'label']]
    if i % 1000 == 0:
        print(i)
df.to_csv("data_10_wo_part3.csv", index=False, encoding='utf8')

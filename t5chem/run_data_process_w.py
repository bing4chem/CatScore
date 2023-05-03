import pandas as pd

path_to_file_wo = "/scratch/by2192/reaction_prediction/t5chem/t5chem/sample_10_wo.csv"
data_wo = pd.read_csv(path_to_file_wo,encoding='utf-8')

path_to_file_w = "/scratch/by2192/reaction_prediction/t5chem/t5chem/sample_10_w.csv"
data_w = pd.read_csv(path_to_file_w,encoding='utf-8')

# create an empty dataframe
df = pd.DataFrame(columns = ['Reactants', 'Predictions', 'Label'])

# target,label,source,prediction_1,prediction_2,prediction_3,prediction_4,prediction_5,prediction_6,       prediction_7,prediction_8,prediction_9,prediction_10,rank
for i in range(40000,80000):  
    df.loc[i*10] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_1'], data_w.loc[i,'label']]
    df.loc[i*10+1] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_2'], data_w.loc[i,'label']]
    df.loc[i*10+2] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_3'], data_w.loc[i,'label']]
    df.loc[i*10+3] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_4'], data_w.loc[i,'label']]
    df.loc[i*10+4] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_5'], data_w.loc[i,'label']]
    df.loc[i*10+5] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_6'], data_w.loc[i,'label']]
    df.loc[i*10+6] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_7'], data_w.loc[i,'label']]
    df.loc[i*10+7] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_8'], data_w.loc[i,'label']]
    df.loc[i*10+8] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_9'], data_w.loc[i,'label']]
    df.loc[i*10+9] = [data_wo.loc[i,'source'], data_w.loc[i,'prediction_10'], data_w.loc[i,'label']]
    if i % 1000 == 0:
        print(i)
df.to_csv("data_10_w_part2.csv", index=False, encoding='utf8')

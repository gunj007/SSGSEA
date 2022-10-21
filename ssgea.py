#data preprocessing libraries 
import numpy as np
import matplotlib.pyplot as mtp
import pandas as pd
import seaborn as sns

#import data file
data=pd.read_csv("C:/Users/GUNJAN/OneDrive/Documents/machinelearning/GSE205432_NormalizedCounts.csv")
gene_id=data['external_gene_name']
print(data,data.columns)

data.drop(['description','ensembl_gene_id'],axis=1,inplace=True)
data.to_csv("log_values.csv",index=False)
#further code in ssgea.r file

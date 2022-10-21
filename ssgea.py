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
'''
#convertinng to numpy array (matrix)
try:
    cpm=[]
    for i in range(1,len(data)):
            colsum=data.iloc[:,i].sum()

            c1=(data.iloc[:,i]/colsum)*10**6
            cpm.append(c1)
    
except:
    print("ignore error")
print(cpm)
cpm=np.array(cpm)
print(cpm)
logv=np.log2(cpm +1)
print("logv",logv)

log_value=pd.DataFrame(logv).T
log_value.columns=data.columns[1:13]
log_value['gene_id']=gene_id

col_1=log_value.pop('gene_id')
log_value.insert(0,'gene_id',col_1)
print("logval:",log_value)
#log_value.to_csv("log_value.csv",index=False)'''
#pip install seaborn
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data={
    'name':["a","b","c","d","e"],
    'age':[24,35,46,32,26],
    'salary':[15000,20000,24000,45000,40000],
    'dept':["CSE","IT","CSE","ECE","IT"],
    'joindate':pd.to_datetime(['2022-06-01','2023-05-02','2024-03-01','2025-06-03','2021-04-09'])
    }
df=pd.DataFrame(data)
#labels=df['name'].tolist()
#ages=df['age'].tolist()
#plt.bar(labels,ages,color="red")
#plt.show()
#sns.countplot(x='dept',data=df)
#combine multiple chart in single frame
fig,axs=plt.subplots(1,4,figsize=(12,5))
sns.barplot(x='dept',y='salary',data=df,estimator=sum,ax=axs[0])
sns.countplot(x='dept',data=df,ax=axs[1])
sns.histplot(df['age'],kde=True,ax=axs[2])
plt.tight_layout()
plt.show()

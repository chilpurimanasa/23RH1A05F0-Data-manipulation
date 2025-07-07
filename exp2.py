#pandas
import pandas as pd
data={
    'name':["a","b","c","d","e"],
    'age':[24,35,46,32,26],
    'salary':[15000,20000,24000,45000,40000],
    'dept':["CSE","IT","CSE","ECE","IT"],
    'joindate':pd.to_datetime(['2022-06-01','2023-05-02','2024-03-01','2025-06-03','2021-04-09'])
    }
print(data)
df=pd.DataFrame(data)
#print(df)
#print(df.head(3))
#print(df.shape)
#print(df.dtypes)
arr=df.columns.tolist()
print(arr)

#filtering
#col based filtering
print(df[['name','dept']])
print(df[df['dept']=="a"])
print(df[df['salary']>20000])
print(df[(df['dept']=="ECE") & (df['salary']>20000)])
print(df)
#find who getting more salary
#print(df['salary'].max())
#print(df.groupby('dept')['salary'].sum())
#print(df['dept'].value_counts())
#df['bonus']=df['salary']*0.10
#print(df)
#import datetime as dt
df['joiningyear']=df['joindate'].dt.year
print(df)
df.rename(columns={'joindate':'joiningdate'},inplace=True)
print(df)
df.drop(columns=['joiningyear'],inplace=True)
print(df)
df=df.sort_values(by='salary',ascending=False)
print(df)
#fetch who is getting more salary in each departed
print(df.loc[df.groupby('dept')['salary'].idxmax()])
print(df)
#seniority based on age
df['seniority']=df['age'].apply(lambda x: 'senior' if x>30 else 'junior')
print(df)

df.to_csv("employee.csv",index=False)
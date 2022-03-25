import numpy as np
import pandas as pd

# Creating the DataFrame
Names = pd.DataFrame({'StudentID':['V001', 'V002', 'V003', 'V004'],
				'Name':['Abe', 'Abhay', 'Acelin', 'Adelphos']})


# Creating the DataFrame
Marks = pd.DataFrame({'StudentID':['V001', 'V002', 'V003', 'V004'],
				'Total_marks':[95, 80, 74, 81]})

# Print the DataFrame
print(Names)
print(Marks)



df = pd.DataFrame(Names,columns=['StudentID','Name'])




df.loc[df['Name'] .str.contains("e")  == True, 'New Name'] = df['Name'].str.upper()
df.loc[df['Name'] .str.contains("e")  == False, 'New Name'] = df['Name'].str.lower()
del df["Name"]
print (df)


df_inner = pd.merge(df, Marks, on='StudentID', how='inner')

print(df_inner)

df_inner = df_inner.drop([1], axis=0)
meanupper= df_inner[['Total_marks']].mean( )
print(meanupper)

df_inner = df_inner.drop([0,2,3], axis=0)
meanlower= df_inner[['Total_marks']].mean()
print(meanlower)

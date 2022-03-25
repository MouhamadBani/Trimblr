
import pandas as pd
url = "https://raw.githubusercontent.com/helloworlddata/white-house-salaries/master/data/converted/2017.csv"
df = pd.read_csv(url)
print(df)



df.head()

df.info()

df.describe()



df.nunique()


df['SALARY'].sum


df.agg(['count','min','max','mean'])
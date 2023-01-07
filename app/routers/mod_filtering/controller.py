import pandas as pd
from app.database import get_db
from sqlalchemy.orm.session import Session


technologies = ({
    'Courses': ["Spark", "PySpark", "Hadoop", "Python", "Pandas", "Hadoop", "Spark"],
    'Fee': [22000, 25000, 23000, 24000, 26000, 25000, 25000],
    'Duration': ['30days', '50days', '55days', '40days', '60days', '35days', '55days'],
    'Discount': [1000, 2300, 1000, 1200, 2500, 1300, 1400],
    'Date': ["2020-08-14", "2020-09-20", "2020-10-16", "2021-09-26", "2021-10-08", "2021-11-17", "2021-11-29"]
})
df = pd.DataFrame(technologies)
# Convert the date to datetime64

async def get_date_now(db: Session, )
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
print(df)

# Use pandas.to_datetime() to filter dates
df2 = df[(df['Date'] > "2020-09-20") & (df['Date'] < "2021-11-17")]
print(df2)

# Filter by single day
df2 = df[df['Date'].dt.strftime('%Y-%m-%d') == "2021-10-08"]
print(df2)

# Filter by single month
df2 = df[df['Date'].dt.strftime('%Y-%m') == '2021-11']
print(df2)

# Filter by single year
df2 = df[df['Date'].dt.strftime('%Y') == '2021']
print(df2)

# Filter dates using DataFrame.loc[]
df2 = df.loc[(df['Date'] >= '2020-09-20') & (df['Date'] < '2021-11-08')]
print(df2)

# Filter data for specific weekday
df2 = df.loc[df['Date'].dt.weekday == 2]
print(type(df2))

# Use DataFrame.query() to filter DataFrame on dates
df2 = df.query("Date >= '2020-08-14' and Date < '2021-11-17'")
print(type(df2))

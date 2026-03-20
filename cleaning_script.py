import pandas as pd

# create data
data = {
    "Customer_ID": [101,102,103,103],
    "Name": ["Asha","Raj","Aman","Aman"],
    "Age": [22,None,-5,-5],
    "Gender": ["F","M","M","M"],
    "City": ["Delhi","Mumbai","Delhi","Delhi"],
    "Salary": [25000,30000,500000,500000],
    "Join_Date": ["2022-05-01","2021/06/15","2020-07-20","2020-07-20"],
    "DOB": ["2002-01-10","2001-03-20","1999-08-15","1999-08-15"]
}

df = pd.DataFrame(data)

# cleaning
df = df.drop_duplicates()
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df[df['Age'] > 0]

df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')
df['DOB'] = pd.to_datetime(df['DOB'])
df['Age_New'] = 2025 - df['DOB'].dt.year

df.to_csv("cleaned_data.csv", index=False)

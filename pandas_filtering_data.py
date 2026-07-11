import pandas as pd


data = {
    "name": ["Jessica", "Alice", "Tony", "Paula"],
    "age": [28, 23, 56, 31],
    "salary": [60000, 78000, 567000, 678001],
    "department": ["HR", "IT", "IT", "HR"]
}

df = pd.DataFrame(data)
print(df[df["age"] > 30])   #from df table, return the rows where age > 30

print(df[df["salary"] < 80000])
print(df[df["salary"] >= 80000])


print(df[df["name"] == "Jessica"])

print(df.groupby("department")["salary"].sum())

print(df.groupby("department")["salary"].min())

print(df.groupby("department")["age"].max())



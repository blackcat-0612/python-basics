import pandas as pd


data = {
    "name": ["Jessica", "Alice", "Tony", "Paula"],
    "age": [28, 23, 56, 31],
    "salary": [60000, 78000, 567000, 678001]
}

df = pd.DataFrame(data)

print(df["name"])       #the concept simply means, from table df get the name column and print it

print(df[["name","salary"]])    ##the concept simply means, from table df get the name and salary column and print it

 #note Python starts with zero based indexing
 #this concept simply means, get the row with index 0, and print it
 #index means position or label

print(df.loc[0])

print(df.loc[3])

#i still dont understand the concept of this
print(df.iloc[1])
import pandas as pd

data = {
    "employee_id": [102, 103, 104, 105],
    "name": ["Jessica", "Alice", "Tony", "Paula"],
    "age": [28, 23, 56, 31],
    "salary": [60000, 78000, 567000, 671801],
    "is_active": [True, False, True, True]
}

df = pd.DataFrame(data)
print(df.sort_values("salary", ascending=False))

print(df.sort_values("age"))        #python default sorting is ascending

#print(df[df["employee_id"] == 105]) | (df["employee_id"] == 102)       #initial code, not working


#this is like a join conditions

print (df[
    ((df["employee_id"] == 105) | (df["employee_id"] == 102))
    & (df["age"] >= 25)
])





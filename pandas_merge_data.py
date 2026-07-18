import pandas as pd

#merge

df1 = pd.DataFrame({"employee_id": [102, 103, 104],
                    "name": ["Jessica", "Alice", "Tony"],
                    "department": ["HR", "IT", "IT"]
                    })

df2 = pd.DataFrame({"employee_id": [102, 103, 104],
                    "salary": [60000, 78000, 567000]
                    })

merged_df = pd.merge(df1, df2, on="employee_id")
print(merged_df)

#pivot
pivot = merged_df.pivot_table (
    values ="salary",
    index ="department",
    aggfunc ="sum"
)
print(pivot)




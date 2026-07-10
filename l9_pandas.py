# pandas are python libraries
import pandas as pd
print("pandas is ready!")

# creating data frames
data = {
    "name": ["Jessica", "Alice", "Tony", "Paula"],
    "age": [28, 23, 56, 31],
    "salary": [60000, 78000, 567000, 678001]
}

df = pd.DataFrame (data)
print(df)

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
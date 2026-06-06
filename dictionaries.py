# dictionaries
# store data in key: value pairs
person = {"name": "Alicia", "age": 31, "city": "Shanghai","job": "Tech BA","language": "SQL, Python"}
print(person["name"])
print(person["age"])
print(person["city"])
print(person["job"])
print(person["language"])

print(person)
print(person["name"])
print(person["job"])
person ["hobby"] = "Sleeping"
print(person)

print(person.keys())        #think of it like a column or field in excel
print(person.values())      # row data
print(person.items())       # both column name and data

for key, value in person.items ():
    print(f"{key}: {value}")
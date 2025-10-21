import pandas as pd
greeting ='Hello World!'
# Create a DataFrame (like an Excel table)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math': [85, 90, 78, 92],
    'Science': [88, 76, 95, 89]
}

df = pd.DataFrame(data)

# Display the table
print("📋 Student Scores:")
print(df)
print(greeting)
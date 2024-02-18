import pandas as pd
import numpy as np

csv = pd.read_csv('he.csv', header=0)

# iterate through the rows of the csv file
for index, row in csv.iterrows():
    print("{")

    if row['Name'] and not pd.isna(row["Name"]):
        print(f"\"name\": \"{row['Name']}\",")

    if row['City'] and not pd.isna(row["City"]):
        print(f"\"city\": \"{row['City']}\",")

    if row['# of food stalls'] and not pd.isna(row["# of food stalls"]):
        print(f"\"food\": \"{row['# of food stalls']}\",")

    if row['Bars'] and not pd.isna(row["Bars"]):
        print(f"\"bars\": \"{row['Bars']}\",")

    if row['Retail'] and not pd.isna(row["Retail"]):
        print(f"\"retail\": \"{row['Retail']}\",")

    if row["Year Opened"] and not pd.isna(row["Year Opened"]):
        print(f"\"year_established\": \"{row['Year Opened']}\",")

    print("},")

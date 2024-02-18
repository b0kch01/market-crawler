import pandas as pd
import numpy as np
import random
import clipboard

csv = pd.read_csv('he.csv', header=0)

# iterate through the rows of the csv file
output = ""

for index, row in csv.iterrows():
    output += "{\n"

    if row['Name'] and not pd.isna(row["Name"]):
        output += (f"\"name\": \"{row['Name']}\",\n")

    if row['City'] and not pd.isna(row["City"]):
        output += (f"\"city\": \"{row['City']}\",\n")

    if row['State'] and not pd.isna(row["State"]):
        output += (f"\"state\": \"{row['State']}\",\n")

    if row['# of food stalls'] and not pd.isna(row["# of food stalls"]):
        output += (f"\"food\": \"{row['# of food stalls']}\",\n")

    if row['Bars'] and not pd.isna(row["Bars"]):
        output += (f"\"bars\": \"{row['Bars']}\",\n")

    if row['Retail'] and not pd.isna(row["Retail"]):
        output += (f"\"retail\": \"{row['Retail']}\",\n")

    if row["Year Opened"] and not pd.isna(row["Year Opened"]):
        output += (f"\"year_established\": \"{row['Year Opened']}\",\n")

    output += (f"\"median_income\": \"${random.randint(30000, 100000):,}\",\n")
    output += (
        f"\"population_density\": \"{random.randint(50, 200)}/sq.miles\",\n")
    output += ("},")

# copy
clipboard.copy(output)

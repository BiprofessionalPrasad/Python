# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 10:00:21 2024

@author: 9387758
"""

# combine CSV files
import pandas as pd
import os

os.chdir(r"C:\Import_Export")

# List of CSV files to join
csv_files = ["file1.csv","file2.csv", "file3.csv", "file4.csv", "file5.csv", "file6.csv", "file7.csv"]

# Initialize an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Read each CSV file, skip the header row, and append to the combined DataFrame
for file in csv_files:
    df = pd.read_csv(file,skipfooter=1)
    combined_df = pd.concat([combined_df,df], axis=0, ignore_index=True)

# Define the output CSV file name
output_csv = "All.csv"

# Export the combined DataFrame to a new CSV file
combined_df.to_csv(output_csv, index=False)

# Print a success message
print(f"Combined data from {len(csv_files)} CSV files and saved to {output_csv}.")

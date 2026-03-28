# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:34:05 2024

@author: 9387758
"""

#=========================================================================
# A) Combine all specific shift files
# B) Replace contents as specified
#=========================================================================
import csv
import pandas as pd
import os

path = r"C:\Users\9387758\OneDrive - MyFedEx\Documents\Lextedit\WMS_LMS_Audit"
os.chdir(path)

def list_files_ending_with(directory, suffix):
    return [f for f in os.listdir(directory) if f.endswith(suffix)]

def concatenate_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for filename in input_files:
            if os.path.exists(filename):
                with open(filename, 'r') as infile:
                    outfile.write(infile.read())
                outfile.write('\n')  # Add a newline between files
            else:
                print(f"Warning: File {filename} not found.")

def replace_in_file(file_path, replacements):
    # Read the file contents
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Perform replacements
    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)
    
    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

def replace_in_multiple_files(file_paths, replacements):
    for file_path in file_paths:
        if os.path.exists(file_path):
            replace_in_file(file_path, replacements)
            print(f"Replacements made in {file_path}")
        else:
            print(f"File not found: {file_path}")

#--- CODE MAIN
directory = 'C:/Users/9387758/OneDrive - MyFedEx/Documents/Lextedit/WMS_LMS_Audit'
files = list_files_ending_with(directory, '_WE.msql')

input_files = files
output_file = 'WE.sql'

concatenate_files(input_files, output_file)
print(f"Files have been concatenated into {output_file}")

file_paths = ['WE.sql']
replacements = {
    '[': '',
    ']': ';',
    'usr_tr_act': 'starprd.usr_tr_act',
    'dlytrn': 'starprd.dlytrn',
    'catch(- 1403)':'',
    'catch(- 1403)':'' ,
    'catch(-1403)':''   
}

replace_in_multiple_files(file_paths, replacements)
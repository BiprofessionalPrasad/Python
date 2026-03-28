# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 12:16:40 2022

@author: pgaiton
"""

import os
import datetime
import pandas as pd


def get_subdir_file_stats(subdirs, df):
    if len(subdirs) > 0:
        temp_df = df.loc[df['Directory'].isin(subdirs)]
        return temp_df['File Count'].sum(), temp_df['Total File Sizes'].sum()
    else:
        return 0,0

def get_files(dir):
    # Initialize File and Directory Dataframes
    file_df = pd.DataFrame()
    dir_df =  pd.DataFrame()

    # Walk through all files/directories in the given directory path
    for path, directory, files in os.walk(dir, topdown=False):

        # Initialize File Size, File Count, and Directory Count variables to put in Directory Dataframe later
        total_file_size = 0
        file_count = len(files)
        dir_count = len(directory)

        # Loop through files and add them to File Dataframe
        for file_name in files:
            try: 
                dir_name = os.path.join(path, file_name)
                stat = os.stat(dir_name)

                file_row = {'File Name': file_name,
                            'Access Date': datetime.datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d-%H:%M'),
                            'Create Date': datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d-%H:%M'),
                            'Modified Date': datetime.datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d-%H:%M'),
                            'File Size': f'{stat.st_size} bytes',
                            'File Directory': dir_name}
                
                # Keep running total of file sizes to put in Directory Dataframe
                total_file_size += stat.st_size

                file_df = file_df.append(file_row, ignore_index=True)
            except TypeError: 
                pass

        # Get the paths for the subdirectories and get the file count/size for each of those
        subdirs = [os.path.join(path, subdir) for subdir in directory]
        subdir_file_count, subdir_file_size = get_subdir_file_stats(subdirs, dir_df)

        file_count += subdir_file_count
        total_file_size += subdir_file_size

        dir_row = {'Directory': path,
                   'File Count': file_count,
                   'Subdirectory Count': dir_count,
                   'Total File Sizes': total_file_size}

        dir_df = dir_df.append(dir_row, ignore_index=True)
    
    return file_df, dir_df

#selDirectory = "I:\\avs"
selDirectory = "C:\\Test"
start_time = datetime.datetime.now()
print(start_time)
#selDirectory = 'C:\\Users\\cascrant\\OneDrive - WEAVER\\Desktop\\Test2'
test_file_df, test_dir_df = get_files(selDirectory)
print(test_file_df)
test_file_df.to_csv('.\\file_temp.csv', index=False)
test_dir_df.to_csv('.\\dir_temp.csv', index=False)
end_time = datetime.datetime.now()
print('Duration: {}'.format(end_time - start_time))
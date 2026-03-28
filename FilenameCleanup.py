# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:33:59 2020

@author: pgaiton
"""

import os 

def set_path():
#    path = r'''K:\Projects\Maconomy\Mac2p4p4\Scripts\Scripts mactest5'''
    path = r'''K:\Projects\Maconomy\Mac2p4p4\Scripts\Scripts mactest5\junk'''
    os.chdir(path)
    return(path)

def rename_prasad(file, string):
     if string in file:
         new=file.replace(string,"")
         os.rename(file, new)

def add_suffix(file,string):
    if string not in file:
        new=file+string
        os.rename(file,new)
      
def replace_names(file,text_to_search,replacement_text):
    # Read in the file
    fin = open(file,'rt',encoding='utf_16_le')
#    fout = open(file+'.sql','w',encoding='utf_16_le')
    data = fin.read()
    
    data = data.replace(text_to_search, replacement_text)
    
    fin.close()
    fin = open(file,'wt',encoding='utf_16_le')
    
    fin.write(data)
    fin.close()
#    newdata = filedata.replace(text_to_search, replacement_text)
#    for line in fin:
#        for word in line:
#            fout.write(word.replace(text_to_search, replacement_text))
#            
    
#    fout.close()
    


def main(): 
    path=set_path()    
#    for filename in os.listdir(path):
        # remove the extra suffix
#        rename_prasad(filename, ".sql")
#        rename_prasad(filename, "dbo.")
#        rename_prasad(filename, ".View")
#        rename_prasad(filename, ".UserDefinedFunction")
#        rename_prasad(filename, ".StoredProcedure")
    
#    for filename in os.listdir(path):        
        # convert to text file
#        add_suffix(filename,".txt")
    for filename in os.listdir(path):
        rename_prasad(filename, ".txt")
        
#    for filename in os.listdir(path):
#    # replace test -> prod links
#        replace_names(filename,"mactestdb1","macproddb1")
#        replace_names(filename,"wttest","wtprod")
#        # convert to sql file

    for filename in os.listdir(path):
        add_suffix(filename, ".sql")
#        
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
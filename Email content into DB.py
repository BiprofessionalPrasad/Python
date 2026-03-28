# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 13:26:20 2024



@author: 9387758
"""
# Extract the number from the email:

import win32com.client

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

for folder in outlook.Folders:
    try:
        specific_folder = folder.Folders['Inbox'].Folders['Data Group']
        break
    except Exception:
        pass

for folder in outlook.Folders:
    print(folder.Name)
    for subfolder in folder.Folders:
        print("  -", subfolder.Name)
    
inbox = outlook.GetDefaultFolder(6)  # 6 represents the inbox folder
messages = inbox.Items

# Filter messages by subject
subject = "Your specific subject"
filtered_messages = messages.Restrict("[Subject] = '" + subject + "'")

for message in filtered_messages:
    print("Subject:", message.Subject)
    print("Sender:", message.SenderName)
    print("Body:", message.Body)
    print("---")
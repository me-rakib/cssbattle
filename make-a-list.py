import os

# getting list of names
arr = os.listdir()

# sorting list
arr.sort()

# unwanted files
unwanted = [
    '.git',
    'README.md',
    'make-a-list.py'
]

# array of list without unwanted files names
arr_we_need = [ele for ele in arr if ele not in unwanted]

# Opening file to read 
file_to_write = open("README.md", "w")

# Text want to add first
text = '''# CSSBattle Solutions #\nThis repository contains all the solutions I have solved as of now.\nHere is the list:\n\n'''
file_to_write.write(text)

for i in arr_we_need:
    file_to_write.write(f'* [{i.replace(".htm", "")}](/{i})\n')

# closing file
file_to_write.close()
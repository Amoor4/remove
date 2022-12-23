import re

text =r'D:\F\Amoor Coding Notes\Python\My Projects\pthon app to remove or extract & clipboard from text\text.txt'



########### 1- remove a character or symbol from text  #########
str = open(text).read()
new_str = re.sub('-','', str)
#print(new_str)



########## 2- remove empty lines from text file   ##########
with open('edited text.txt','w') as file:
    with open (r'D:\F\Amoor Coding Notes\Python\My Projects\pthon app to remove or extract & clipboard from text\text.txt', 'r') as f:
        for line in f:
            if not line.isspace():              # this to remove empty lines from text file
                line = re.sub('-','', line)     # this to remove the symbol - from text file                   
                file.write(line)
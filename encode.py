# encode python program

import csv

reader = csv.reader(open('table.csv', 'r'))
char_dict = {}
for row in reader:
    k, v = row
    char_dict[v.replace('"', '', 2)] = k  # imports the csv conversion sheet as a dictionary char_dict

# importing files and setting an output

infile = open(input('What is the name of the file?'))
instr = infile.read()
instr = instr.replace('\n', '¶')  # broken \n workaround
outstr = ''

x = 0  # this is the 'reader' that reads through the string

for i in range(len(instr)):
    if x >= len(instr):  # if reader out of range, break the loop
        break
    if instr[x:x + 3] in char_dict:
        current_word = instr[x:x + 3]  # checks for 3 letter words in the table to replace
        x += 3
    elif instr[x:x + 2] in char_dict:
        current_word = instr[x:x + 2]  # checks for 2 letter words in the table to replace
        x += 2
    elif instr[x] in char_dict:
        current_word = instr[x]  # checks for letters in the table to replace
        x += 1

    current_str = char_dict[current_word]   # current str is the value for key current word in the dictionary
    outstr += current_str   # adds current char to out str

length = str(len(outstr))
outstr = length + '.' + outstr

outfile = open('output.txt', 'w')
outfile.write(outstr)   # writes outstr to outfile

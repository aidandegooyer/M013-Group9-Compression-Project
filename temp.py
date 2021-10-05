# decode python program

import csv

reader = csv.reader(open('table.csv', 'r'))
char_dict = {}
for row in reader:
    k, v = row
    char_dict[v.replace('"', '')] = k

infile = open(input('What is the name of the file?'))
instr = infile.read()
outstr = ''

x = 0
for i in range(len(instr)):
    if instr[x:x+3] in char_dict:
        bin_char = char_dict[instr[x:x+3]]
        x += 4
    elif instr[x:x+2] in char_dict:
        bin_char = char_dict[instr[x:x+2]]
        x += 3
    elif instr[x:x+1] in char_dict:
        bin_char = char_dict[instr[x:x+1]]
        x += 2
    else:
        bin_char = char_dict[instr[x]]
        x += 1
    outstr += bin_char

print(outstr)

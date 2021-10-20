# decode python program

import csv

reader = csv.reader(open('table.csv', 'r'))
char_dict = {}
for row in reader:
    k, v = row
    char_dict[k] = v.replace('"', '', 2)  # imports the csv conversion sheet as a dictionary char_dict

# importing files and setting an output

infile = open(input('What is the name of the file?'))
instr = infile.read()
if '.' in instr:
    splitstr = instr.split('.')
    instr = splitstr[1]
outstr = ''

x = 0  # this is the 'reader' that reads through the string

for i in range(len(instr)):
    if x >= len(instr):  # if reader out of range, break the loop
        break
    if instr[x] == '1':
        current_word = instr[x:x + 4]   # if this is a 'short character', set the current word to next 4 binary digits
        x += 4
    else:
        current_word = instr[x:x + 7]   # if this is a 'long character', set the current word to next 7 binary digits
        x += 7
    current_char = char_dict[current_word]  # current char is the value for key current word in the dictionary
    outstr += current_char  # adds current char to out str

outstr = outstr.replace('¶', '\n')  # broken \n workaround

outfile = open('output.txt', 'w')
outfile.write(outstr)   # writes outstr to outfile

# encode python program

import csv

reader = csv.reader(open('table.csv', 'r'))
char_dict = {}
for row in reader:
    k, v = row
    char_dict[v.replace('"', '')] = k

infile = open(input('What is the name of the file?'))
instr = infile.read()
instr = instr.replace('\n', '¶')
outstr = ''

x = 0
for i in range(len(instr)):
    if x >= len(instr):
        break
    if instr[x:x+3] in char_dict:
        current_word = instr[x:x+3]
        x += 3
    elif instr[x:x+2] in char_dict:
        current_word = instr[x:x+2]
        x += 2
    elif instr[x] in char_dict:
        current_word = instr[x]
        x += 1

    current_str = char_dict[current_word]
    outstr += current_str

outfile = open('output.txt', 'w')
outfile.write(outstr)

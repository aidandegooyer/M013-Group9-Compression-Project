# decode python program

import csv

reader = csv.reader(open('table.csv', 'r'))
char_dict = {}
for row in reader:
    k, v = row
    char_dict[k] = v.replace('"', '')

infile = open(input('What is the name of the file?'))
instr = infile.read()
outstr = ''

x = 0

for i in range(len(instr)):
    if x >= len(instr):
        break
    if instr[x] == '1':
        current_word = instr[x:x+4]
        x += 4
    else:
        current_word = instr[x:x+7]
        x += 7
    current_char = char_dict[current_word]
    outstr += current_char

outstr = outstr.replace('¶', '\n')

outfile = open('output.txt', 'w')
outfile.write(outstr)

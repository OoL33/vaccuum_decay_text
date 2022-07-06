
num_lines = 0
num_charc = 0
f = open('vacuumdecay.txt', 'r')
    
line = f.readline()
lineNumber = 1

while line != '':
    print(str(lineNumber ) + ' - ', line.rstrip('\n') )
    line = f.readline()
    lineNumber = lineNumber + 1
        
with open('vacuumdecay.txt', 'r') as f:
    for line in f:
        num_lines += 1
    for i in line:
        num_charc += 1

print("Line Count: ", num_lines)
print('Character Count: ', num_charc)





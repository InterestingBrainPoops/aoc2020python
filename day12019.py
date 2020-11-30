import math
filepath = 'input.txt'
global count
count = 0
def fuel(mass):
    return math.floor(mass/3)-2
def writecodehere(line):
    x = True
    temp0 = 0
    mass = fuel(int(line))
    temp1 = 0
    while(x):
        temp1 += mass
        mass = fuel(mass)
        if(mass <= 0):
            x = False
    return temp1


with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        count += writecodehere(line)
    fp.close()
print(count)
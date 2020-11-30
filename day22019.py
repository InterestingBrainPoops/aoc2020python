import re, typing
import intcode as ic
count = []
def lmap(func, *iterables):
    return list(map(func, *iterables))
def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))  # thanks mserrano!
def writecodehere(line):
    #print(line)
    line0 = line
    for x in range(0,99):
        #print(line)
        for y in range(0,99) :
            temp = line0.copy()
            temp[1] = x
            temp[2] = y
            #print(ic.evalintcode(temp))
            try:
                if ic.evalintcode(temp) == 19690720:
                    print(100*x+y)
            except IndexError:
                pass
filepath = "./input.txt"
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        count = writecodehere(ints(line))
    fp.close()
print(count)
count = [0,0,0]
import re
def getpath(poses):
    ret = [[0,0]]
    for x in range(len(poses)):
        for i in range(int(re.search(r'\d+', poses[x]).group())):
            a = poses[x][0]
            #print(ret[len(ret)-1])
            ret.append(ret[len(ret)-1])
            if(a=="U"):
                ret[len(ret)-1][0] += 1
            if(a=="D"):
                ret[len(ret)-1][0] -= 1
            if(a=="L"):
                ret[len(ret)-1][1] -= 1
            if(a=="R"):
                ret[len(ret)-1][1] += 1
            #print(ret[len(ret)-1])
    return ret
with open("./input.txt") as fp:
    for cnt, line in enumerate(fp):
        count[cnt] = line.split(',')
    fp.close()
#print(count)
w1 = getpath(count[0])
w2 = getpath(count[1])
for x in range(len(w1)):
    for y in range(len(w2)):
        if(w1[x] == w2[y]):
            print(w1[x])
#print(w2)
def evalintcode(line):
    x=0
    temp = line
    for x in range(0,len(temp),4):
        #print(temp[x])
        if(temp[x] == 1):
            temp[temp[x+3]] = temp[temp[x+1]] + temp[temp[x+2]]
        elif(temp[x] == 2):
            temp[temp[x+3]] = temp[temp[x+1]] * temp[temp[x+2]]
        elif(temp[x] == 99):
            break
        #else:
            #print(temp[x])
    return temp[0]
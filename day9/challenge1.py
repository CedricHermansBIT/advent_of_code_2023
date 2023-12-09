readings=[]

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        readings.append([int(x) for x in line.strip().split()])


total=0
for reading in readings:
    temp=[reading]
    print(reading)
    # process 1 reading at a time
    for i,r in enumerate(temp):
        # pad next step with 0s to the left so that length is always the same
        temp.append([0 for _ in range(i+1)])
        # calculate the difference between each reading and the one before it (starting from the 2nd reading, since then we have 2 readings to compare)
        for j,read in enumerate(r[i+1:]):
            # add the difference to the next step list
            temp[i+1].append(read - r[j+i])
        # if all the differences are 0, then we have reached the end of the chain
        if len(set(temp[i+1]))==1 and temp[i+1][0]==0:
            # to break out of the loop, we pop the last element (since then our for loop will reach the end of the list)
            temp.pop()
    # calculate the total based on the sum of the last element of each list 
    total+=sum(x[-1] for x in temp)
    print(temp)
            
print(total)

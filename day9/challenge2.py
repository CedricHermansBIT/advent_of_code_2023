readings=[]

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        readings.append([int(x) for x in line.strip().split()])

# basically the same as challenge 1, except we calculate the total differently
total=0
for reading in readings:
    temp=[reading]
    for i,r in enumerate(temp):
        temp.append([0 for _ in range(i+1)])
        for j,read in enumerate(r[i+1:]):
            temp[i+1].append(read - r[j+i])

        if len(set(temp[i+1]))==1 and temp[i+1][0]==0:
            temp.pop()


    # total is a bit more complicated
    # start with reversing the list
    temp.reverse()

    temptotal=0
    for i,t in enumerate(temp):
        # since our list is reversed, and we have padded the left side with 0s, we need to add the first real difference
        # note, not really adding, but we need to take that value and subtract our current temptotal from it
        temptotal=t[len(temp)-i-1]-temptotal
    # now we can add the temptotal to the total
    total+=temptotal
print(total)

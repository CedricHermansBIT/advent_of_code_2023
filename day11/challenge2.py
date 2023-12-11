with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.readlines()

galaxies=[]
for y,line in enumerate(lines):
    for x,char in enumerate(line):
        if char=="#":
            galaxies.append((x,y))
print(galaxies)

x_positions,y_positions=zip(*galaxies)
# We are not interested in missing x or y positions that are smaller or larger than the min/max
missing_x=[x for x in range(min(x_positions),max(x_positions)+1) if x not in x_positions]
missing_y=[y for y in range(min(y_positions),max(y_positions)+1) if y not in y_positions]
print(missing_x,missing_y)

total=0
for i,galaxy1 in enumerate(galaxies):
    for j,galaxy2 in enumerate(galaxies[i+1:]):
        #manhattan distance: abs(x1-x2)+abs(y1-y2)
        d=abs(galaxy1[0]-galaxy2[0])+abs(galaxy1[1]-galaxy2[1])
        # 1000000*the missing lines
        for x in missing_x:
            if galaxy1[0]<x<galaxy2[0] or galaxy2[0]<x<galaxy1[0]:
                d+=999999
        for y in missing_y:
            if galaxy1[1]<y<galaxy2[1] or galaxy2[1]<y<galaxy1[1]:
                d+=999999

        print(i+1, j+i+2,galaxy1,galaxy2,d)
        total+=d
print(total)
        




        

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[list(line.strip()) for line in ifile]

def move(x,y,dir):
    if dir==1:
        return (x,y-1)
    elif dir==2:
        return (x+1,y)
    elif dir==3:
        return (x,y+1)
    elif dir==4:
        return (x-1,y)


# 1=N, 2=E, 3=S, 4=W
# light = (x,y,dir)
lights=set()
lights.add((0,0,2))
# energized = (x,y,dir)
energized=set()
#print(lights)
while len(lights)>0:
    light=lights.pop()
    #print(light)
    if light not in energized:
        energized.add(light)
        # move forward
        #check symbol:
        s=lines[light[1]][light[0]]
        #print(s,light)
        if s in [".","/","\\"]:
            if s==".":
                newdir=light[2]
            elif s=="/":
                match light[2]:
                    case 1:
                        newdir=2
                    case 2:
                        newdir=1
                    case 3:
                        newdir=4
                    case 4:
                        newdir=3
            elif s=="\\":
                match light[2]:
                    case 1:
                        newdir=4
                    case 2:
                        newdir=3
                    case 3:
                        newdir=2
                    case 4:
                        newdir=1
            newpos=move(light[0],light[1],newdir)
            # check if newpos is in bounds
            if newpos[0]>=0 and newpos[0]<len(lines[0]) and newpos[1]>=0 and newpos[1]<len(lines):
                newlight=(newpos[0],newpos[1],newdir)
                if newlight not in energized:
                    lights.add(newlight)
        elif s in ["|","-"]:
            match light[2],s:
                # move in same direction
                case 1,"|":
                    newdir=1
                case 2,"-":
                    newdir=2
                case 3,"|":
                    newdir=3
                case 4,"-":
                    newdir=4
                # split in two directions
                case 1,"-":
                    newdir=[2,4]
                case 2,"|":
                    newdir=[1,3]
                case 3,"-":
                    newdir=[2,4]
                case 4,"|":
                    newdir=[1,3]
            if type(newdir)==int:
                newpos=move(light[0],light[1],newdir)
                # check if newpos is in bounds
                if newpos[0]>=0 and newpos[0]<len(lines[0]) and newpos[1]>=0 and newpos[1]<len(lines):
                    newlight=(newpos[0],newpos[1],newdir)
                    if newlight not in energized:
                        lights.add(newlight)
            else:
                for d in newdir:
                    newpos=move(light[0],light[1],d)
                    # check if newpos is in bounds
                    if newpos[0]>=0 and newpos[0]<len(lines[0]) and newpos[1]>=0 and newpos[1]<len(lines):
                        newlight=(newpos[0],newpos[1],d)
                        if newlight not in energized:
                            lights.add(newlight)

energized_pos=set([(l[0],l[1]) for l in energized])
for y,line in enumerate(lines):
    for x,s in enumerate(line):
        if (x,y) in energized_pos:
            print("#",end="")
        else:
            print(".",end="")
    print()
print(len(set([(l[0],l[1]) for l in energized])))



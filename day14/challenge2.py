import tqdm

with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[list(lines.strip()) for lines in ifile]

print(lines)

rocks=[(y,x) for x in range(len(lines)) for y in range(len(lines[x])) if lines[x][y] == "O"]
fixed=set((y,x) for x in range(len(lines)) for y in range(len(lines[x])) if lines[x][y] == "#")

history=[]

def printgrid(rocks,fixed):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if (x,y) in rocks:
                print("O",end="")
            elif (x,y) in fixed:
                print("#",end="")
            else:
                print(".",end="")
        print()

for cycle in tqdm.tqdm(range(1000000000)):
    # Move north
    # sort rocks by y, then x
    rocks.sort(key=lambda x: (x[1],x[0]))
    # move each rock up until it does not hit "." or the top
    for i in range(len(rocks)):
        x,y=rocks[i]
        m=False
        while y>0 and (x,y-1) not in rocks and (x,y-1) not in fixed:
            y-=1
            m=True
        if m:
            rocks[i]=(x,y)
    # Move west
    # sort rocks by x, then y
    rocks.sort(key=lambda x: (x[0],x[1]))
    # move each rock left until it does not hit "." or the left edge
    for i in range(len(rocks)):
        x,y=rocks[i]
        m=False
        while x>0 and (x-1,y) not in rocks and (x-1,y) not in fixed:
            x-=1
            m=True
        if m:
            rocks[i]=(x,y)
    # Move south
    # sort rocks by reverse y, then x
    rocks.sort(key=lambda x: (-x[1],x[0]))
    # move each rock down until it does not hit "." or the bottom
    for i in range(len(rocks)):
        x,y=rocks[i]
        m=False
        while y<len(lines)-1 and (x,y+1) not in rocks and (x,y+1) not in fixed:
            y+=1
            m=True
        if m:
            rocks[i]=(x,y)
    # Move east
    # sort rocks by reverse x, then y
    rocks.sort(key=lambda x: (-x[0],x[1]))
    # move each rock right until it does not hit "." or the right edge
    for i in range(len(rocks)):
        x,y=rocks[i]
        m=False
        while x<len(lines)-1 and (x+1,y) not in rocks and (x+1,y) not in fixed:
            x+=1
            m=True
        if m:
            rocks[i]=(x,y)

    #printgrid(rocks,fixed)


    # Check for history
    if rocks in history:
        print(f"Found history at cycle {cycle}")
        print(history)
        print(rocks)
        print(f"cyle happens every {(repeats:=(cycle-history.index(rocks)))} cycles")
        print(f"first occurence at cycle {history.index(rocks)}")

        # imagine that first occurence is at cycle 2 and repeats every 7 cycles
        # we want to find the state at cycle 50
        # we know it only starts repeating at cycle 2, so we can remove the first 2 cycles from the history
        # 48 cycles remain, and we know it repeats every 7 cycles, so we know that at 48%7=6th history state is the same as the 50th (so index 5)
        

        index_at_1billion=(1000000000-history.index(rocks))%repeats
        history_starting_from_repeat=history[history.index(rocks):]

        rocks = history_starting_from_repeat[index_at_1billion-1]



        break
    else:
        #print(rocks)
        history.append(rocks.copy())
            
        


total=0
for x,y in rocks:
    total+=(len(lines)-y)
print(total)
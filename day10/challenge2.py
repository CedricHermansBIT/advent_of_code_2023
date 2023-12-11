with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[line.strip() for line in ifile.readlines()]

allowed_dirs={"N":["|","7","F"],
              "E":["-","7","J"],
              "S":["|","J","L"],
              "W":["-","F","L"]}

directions={"|":["N","S"],
            "-":["E","W"],
            "7":["S","W"],
            "J":["N","W"],
            "F":["S","E"],
            "L":["E","N"]}

opposite={"N":"S",
          "E":"W",
          "S":"N",
          "W":"E"}

copy_of_map=[[0 for i in range(len(lines[0]))] for j in range(len(lines))]

# Find the starting point
for i in range(len(lines)):
    if "S" in lines[i]:
        start=[i,lines[i].index("S")]
        break

current=start.copy()

# Find the symbol at the starting point depending on the surrounding symbols
N,E,S,W= [lines[current[0]-1][current[1]],lines[current[0]][current[1]+1],lines[current[0]+1][current[1]],lines[current[0]][current[1]-1]]
if (N in allowed_dirs["N"] and S in allowed_dirs["S"]):
    copy_of_map[current[0]][current[1]]="|"
elif (E in allowed_dirs["E"] and W in allowed_dirs["W"]):
    copy_of_map[current[0]][current[1]]="-"
elif (N in allowed_dirs["N"] and E in allowed_dirs["E"]):
    copy_of_map[current[0]][current[1]]="L"
elif (N in allowed_dirs["N"] and W in allowed_dirs["W"]):
    copy_of_map[current[0]][current[1]]="J"
elif (S in allowed_dirs["S"] and E in allowed_dirs["E"]):
    copy_of_map[current[0]][current[1]]="F"
elif (S in allowed_dirs["S"] and W in allowed_dirs["W"]):
    copy_of_map[current[0]][current[1]]="7"


def find_valid_direction(current,lines):
    if current[0]>0 and lines[current[0]-1][current[1]] in allowed_dirs["N"]:
        return "N"
    elif current[1]<len(lines[0])-1 and lines[current[0]][current[1]+1] in allowed_dirs["E"]:
        return "E"
    elif current[0]<len(lines)-1 and lines[current[0]+1][current[1]] in allowed_dirs["S"]:
        return "S"
    elif current[1]>0 and lines[current[0]][current[1]-1] in allowed_dirs["W"]:
        return "W"
    else:
        return None

direction=find_valid_direction(current,lines)

def update_current(current,dir):
    match dir:
        case "N":
            current[0]-=1
        case "E":
            current[1]+=1
        case "S":
            current[0]+=1
        case "W":
            current[1]-=1
    return current

current=update_current(current,direction)

while current!=start:
    # set copy_of_map to symbol at current

    symbol=lines[current[0]][current[1]]
    copy_of_map[current[0]][current[1]]=symbol
    new_direction=directions[symbol]
    if opposite[direction] == new_direction[0]:
        direction=new_direction[1]
    else:
        direction=new_direction[0]
    #print(current,start, lines[current[0]][current[1]],direction)
    current=update_current(current,direction)


# To determine whether we are within a loop, the idea is quite simple (raycasting):
# for each vertical line, we need to flip the within_loop flag
# However, If we have FJ, L7, then they are basically the same vertical line

counter=0
symbol=None
within_loop=False
for y,l in enumerate(copy_of_map):
    assert within_loop==False
    for x,ch in enumerate(l):
        if ch !=0 and ch !="-":
            if symbol==None:
                if ch!="|":
                    symbol=ch
                within_loop=not within_loop
            else:
                #print(f"symbol={symbol}, x={x}, within_loop={within_loop}")
                match symbol:
                    case "F":
                        if ch=="J":
                            symbol=None
                        else:
                            within_loop=not within_loop
                            symbol=None
                    case "L":
                        if ch=="7":
                            symbol=None
                        else:
                            within_loop=not within_loop
                            symbol=None
        elif within_loop and ch==0:
            #print("yup")
            counter+=1    
            copy_of_map[y][x]="1"        
        else:
            # this should be the "-" case, so do nothing or when x==0 and not within_loop
            #print(x)
            pass

# print the map and color the enclosed area (just for fun, not necessary)
print("\n".join(["".join([str(ch).replace("F","┌").replace("L","└").replace("7","┐").replace("J","┘").replace("-","─").replace("|","│") if ch!="1" else "\033[91m1\033[0m" for ch in l]) for l in copy_of_map]))
print(counter)
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[line.strip() for line in ifile.readlines()]

print(lines)

# Find the starting point
for i in range(len(lines)):
    if "S" in lines[i]:
        start=[i,lines[i].index("S")]
        break

current=start.copy()

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

counter=0
while current!=start:
    symbol=lines[current[0]][current[1]]
    new_direction=directions[symbol]
    if opposite[direction] == new_direction[0]:
        direction=new_direction[1]
    else:
        direction=new_direction[0]
    print(current,start, lines[current[0]][current[1]],direction)
    current=update_current(current,direction)
    counter+=1

print(round(counter/2))

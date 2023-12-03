import re

def iterate_neighbours(xstart,ystart,len,maxx,maxy,lines):
    print("xstart: {}, ystart: {}, len: {}, maxx: {}, maxy: {}".format(xstart,ystart,len,maxx,maxy))
    for x in range(max(0,xstart-1),min(xstart+len+1,maxx)):
        for y in range(max(0,ystart-1),min(ystart+2,maxy)):
            if not(y==ystart and (xstart<=x<xstart+len)):
                if lines[y][x] != "." and not lines[y][x].isdigit():
                    return True
    return False

result=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[x.strip() for x in ifile.readlines()]
    maxx=len(lines[0])
    maxy=len(lines)
    for y,line in enumerate(lines):
        numbers=re.finditer(r"([0-9]+)",line)
        for number in numbers:
            if iterate_neighbours(number.start(),y,len(number.group()),maxx,maxy,lines):
                result+=int(number.group())
print(result)
        

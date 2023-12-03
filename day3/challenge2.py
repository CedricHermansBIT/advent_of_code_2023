import re

def iterate_neighbours(sx,sy,lines,maxx,maxy,allnumbers):
    ratios=[]
    for y in range(max(0,sy-1),min(sy+2,maxy)):
        same=False
        if y in allnumbers:
            for x in range(max(0,sx-1),min(sx+2,maxx)):
                if not lines[y][x].isdigit():
                    same=False
                if not same:
                    #print(f"Checking {x=},{y=} for {sx=},{sy=}")
                    n=grab_number(x,allnumbers[y])
                    if n:
                        ratios.append(int(n))
                        same=True
    if len(ratios)==2:
        #print(f"Found two ratios: {ratios}")
        result=ratios[0]*ratios[1]
        #print(f"{result=}")
        return result

def grab_number(x,numbers):
    for number in numbers:
        if number["start"]<=x<number["end"]:
            #print(f"Found number {number["group"]} at {x=},{y=}")
            return number["group"]
            

def find_all_numbers(lines):
    allnumbers={}
    for y,line in enumerate(lines):
        numbers=re.finditer(r"([0-9]+)",line)
        if y in allnumbers:
            allnumbers[y]+=numbers
        else:
            allnumbers[y]=[{"start":number.start(),"end":number.end(),"group":number.group()} for number in numbers]
    return allnumbers

result=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[x.strip() for x in ifile.readlines()]
    allnumbers=find_all_numbers(lines)
    #print(allnumbers)
    maxx=len(lines[0])
    maxy=len(lines)
    for y,line in enumerate(lines):
        for x,char in enumerate(line):
            if char == "*":
                r=iterate_neighbours(x,y,lines,maxx,maxy,allnumbers)
                if r:
                    result+=r
print(result)

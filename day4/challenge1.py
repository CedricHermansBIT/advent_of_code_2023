total=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        winning, mynumbers = line.split(":")[1].split("|")
        total+=2**(len([x for x in [int(x) for x in winning.strip().split()] if x in [int(x) for x in mynumbers.strip().split()]])-1)//1
print(total)

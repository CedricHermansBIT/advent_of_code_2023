#with open("testinput.txt","r") as ifile:
print(round(sum([2**(len([x for x in line.split(":")[1].split("|")[0].strip().split() if x in line.split(":")[1].split("|")[1].strip().split()])-1)//1 for line in open("challengeinput.txt","r")])))


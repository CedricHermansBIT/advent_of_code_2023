with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[list(lines.strip()) for lines in ifile]

print(lines)

for i in range(1,len(lines)):
    for j in range(0,len(lines[i])):
        if lines[i][j] == "O":
            print(f"found {i},{j}")
            moved=False
            pline=i-1
            while lines[pline][j] == "." and pline >= 0:
                pline-=1
                moved=True
            if moved:
                lines[pline+1][j]="O"
                lines[i][j]="."
                print(f"moving {i},{j} to {pline},{j}")
total=0
for i,line in enumerate(lines):
    total+=line.count("O")*(len(lines)-i)
print(total)
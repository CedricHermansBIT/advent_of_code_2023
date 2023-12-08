with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.readlines()
steps=[int(x) for x in list(lines[0].strip().replace("L","0").replace("R","1"))]
print(steps)

graph={}
for line in lines[2:]:
    graph[line[0:3]]=[line[7:10],line[12:15]]

k="AAA"
step_counter=0
while k!="ZZZ":
    print(k)
    k=graph[k][steps[step_counter%len(steps)]]
    step_counter+=1

print(step_counter)
with open("challengeinput2.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.readlines()
    times=[int(x) for x in lines[0].split(" ")[1:] if x!=""]
    distances=[int(x) for x in lines[1].split(" ")[1:] if x!=""]
    print(times)
    print(distances) 
       
winning=1
for i, t in enumerate(times):
    w=0
    d=distances[i]
    for j in range(1,t+1):
        if (j*(t-j)>d):
            w+=1
    winning*=w

print(winning)


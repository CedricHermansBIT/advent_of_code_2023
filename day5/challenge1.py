with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.read()

sections=lines.split("\n\n")
seeds=[int(x) for x in sections[0].split(" ")[1:]]
# note to self: dest,src,len
steps=[[[int(y) for y in x.split(" ")]  for x in sections[n].split("\n")[1:]] for n in range(1,len(sections))]
#for step in steps:
#    print(step)
locations=[]
for seed in seeds:
    for step in steps:
        for (dest,src,len) in step:
            if src<=seed<src+len:
                #print("seed",seed,"dest",dest,"src",src,"len",len, "diff",dest-src)
                seed+=(dest-src)
                break
    locations.append(seed)
print(min(locations))

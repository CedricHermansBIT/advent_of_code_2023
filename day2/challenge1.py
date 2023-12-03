maximum = {"red":12,"green":13,"blue":14}

solution=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        id,rest=line[5:].split(":")
        rest=rest.split(";")
        impossible=False
        for grab in rest:
            grab=grab.strip().split(",")
            for x in grab:
                num,col=x.strip().split(" ")
                if int(num)>maximum[col]:
                    impossible=True
        if impossible:
            continue
        solution+=int(id)

        print(id)
        
print(solution)

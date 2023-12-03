
solution=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        maximum = {"red":0,"green":0,"blue":0}
        id,rest=line[5:].split(":")
        rest=rest.split(";")
        impossible=False
        for grab in rest:
            grab=grab.strip().split(",")
            for x in grab:
                num,col=x.strip().split(" ")
                if int(num)>maximum[col]:
                    maximum[col]=int(num)
        power=1
        for v in maximum.values():
            power*=v
        solution+=power

        
print(solution)

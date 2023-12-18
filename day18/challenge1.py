edges=[]
directions={"U":(0,1),"D":(0,-1),"L":(-1,0),"R":(1,0)}

start=(0,0)
edges.append(start)
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        dir, dist, color = line.split()
        for i in range(int(dist)):
            edges.append((edges[-1][0]+directions[dir][0],edges[-1][1]+directions[dir][1]))
# we end at start, so pop the last one
edges.pop()

#print(edges)

minx=min(edges,key=lambda x:x[0])[0]
miny=min(edges,key=lambda x:x[1])[1]
maxx=max(edges,key=lambda x:x[0])[0]
maxy=max(edges,key=lambda x:x[1])[1]

# for y in range(maxy,miny-1,-1):
#     for x in range(minx,maxx+1):
#         if (x,y) in edges:
#             if (x,y)==(0,0):
#                 print("X",end="")
#             else:
#                 print("#",end="")
#         else:
#             print(".",end="")
#     print()

# find first hashtag in first row
firstline=[x for x in edges if x[1]==maxy]
# minimum x value of first row
firstline.sort(key=lambda x:x[0])
corner=firstline[0]
#print(corner)
first_internal=(corner[0]+1,corner[1]-1)

inside=set()
inside.add(first_internal)
to_check=set()
to_check.add(first_internal)
# find all internal points (flood fill)
# for each point in inside, check if it has a dot neighbour, if so add to inside and to_check (if not already in inside)
while len(to_check)>0:
    check=to_check.pop()
    for dir in directions.values():
        neighbour=(check[0]+dir[0],check[1]+dir[1])
        if neighbour in edges:
            continue
        if neighbour in inside:
            continue
        inside.add(neighbour)
        to_check.add(neighbour)
    #print(to_check)


for y in range(maxy,miny-1,-1):
    for x in range(minx,maxx+1):
        if (x,y) in edges or (x,y) in inside:
            if (x,y)==(0,0):
                print("X",end="")
            else:
                print("#",end="")
        else:
            print(".",end="")
    print()

print(f"Answer: {len(inside)+len(edges)}")
#print(len(edges))
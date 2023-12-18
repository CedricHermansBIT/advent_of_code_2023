edges=[]
# 0 is right, 1 is down, 2 is left, 3 is up
R=0
D=1
L=2
U=3
directions={3:(0,1),1:(0,-1),2:(-1,0),0:(1,0)}
# corners: 0 = 7, 1 = F, 2 = J, 3 = L
corner_type={R:{D:"7",U:"J"},
             D:{R:"L",L:"J"},
             L:{D:"F",U:"L"},
             U:{R:"F",L:"7"}}

# x,y,corner_type,dir
start=[0,0,0,0]
edges.append(start)
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    previous=start
    pdir=1
    for line in ifile:
        dir, dist, color = line.split()
        #dist=int(dist)
        #dir="RDLU".index(dir)
        dist=int(color[2:7],16)
        dir=int(color[7])
        # save the very first direction
        #print("dir: ",dir," dist: ",dist," color: ",color, " previous: ",previous, " pdir: ",pdir)
        # we only save the corners
        if dir==0:
            # right
            newedge=[previous[0]+dist,previous[1],corner_type[pdir][dir],dir]
            edges[-1][2]=corner_type[pdir][dir]
            edges.append(newedge)
            previous=newedge
            pdir=dir
        elif dir==1:
            # down
            newedge=[previous[0],previous[1]+dist,corner_type[pdir][dir],dir]
            edges[-1][2]=corner_type[pdir][dir]
            edges.append(newedge)
            previous=newedge
            pdir=dir
        elif dir==2:
            # left
            newedge=[previous[0]-dist,previous[1],corner_type[pdir][dir],dir]
            edges[-1][2]=corner_type[pdir][dir]
            edges.append(newedge)
            previous=newedge
            pdir=dir
        elif dir==3:
            # up
            newedge=[previous[0],previous[1]-dist,corner_type[pdir][dir],dir]
            edges[-1][2]=corner_type[pdir][dir]
            edges.append(newedge)
            previous=newedge
            pdir=dir
        else:
            print("error")
            exit(1)
        #print(newedge)
    # fix the first corner (since we looped around)
    edges[0][3] = 0 if edges[1][0]>edges[0][0] else 1 if edges[1][1]>edges[0][1] else 2 if edges[1][0]<edges[0][0] else 3 if edges[1][1]<edges[0][1] else None
    edges[0]=[edges[0][0],edges[0][1],corner_type[edges[-1][3]][edges[0][3]],edges[0][3]]
    print(edges[0])

minx=min([x[0] for x in edges])
miny=min([x[1] for x in edges])

# translate all coordinates to positive
for i in range(len(edges)):
    edges[i][0]+=abs(minx)
    edges[i][1]+=abs(miny)

#print("edges: ",edges)

# compress coordinates
# find the first corner
all_x=list(set([x[0] for x in edges]))
all_y=list(set([x[1] for x in edges]))
# sort them
all_x.sort()
all_y.sort()
# create a mapping from old to new
x_mapping={}
y_mapping={}
for i in range(len(all_x)):
    x_mapping[i]=all_x[i]
for i in range(len(all_y)):
    y_mapping[i]=all_y[i]

r_x_mapping={v: k for k, v in x_mapping.items()}
r_y_mapping={v: k for k, v in y_mapping.items()}
# create new edges
new_edges=[]
for edge in edges:
    new_edges.append([r_x_mapping[edge[0]],r_y_mapping[edge[1]],edge[2]])
#print("new edges: ",new_edges)

# Fill in "-" and "|" edges
# sort edges by y, then x
new_edges.sort(key=lambda x:(x[1],x[0]))

new_edges_pos=[x[:2] for x in new_edges]
new_new_edges=[]
for y in range(len(all_y)):
    inside=False
    for x in range(len(all_x)):
        if [x,y] in new_edges_pos:
            inside= not inside
            new_new_edges.append([x,y,new_edges[new_edges_pos.index([x,y])][2]])
            continue
        if inside:
            new_new_edges.append([x,y,"-"])

# sort edges by x, then y
new_new_edges.sort(key=lambda x:(x[0],x[1]))
for x in range(len(all_x)):
    inside=False
    for y in range(len(all_y)):
        if [x,y] in new_edges_pos:
            inside= not inside
            continue
        if inside:
            new_new_edges.append([x,y,"|"])


# sort edges by y, then x
new_new_edges.sort(key=lambda x:(x[0],x[1]))

# print the map
new_edges_pos=[x[:2] for x in new_new_edges]
copy_of_map=[["." for i in range(len(all_x))] for j in range(len(all_y))]
for y in range(len(all_y)):
    for x in range(len(all_x)):
        if [x,y] in new_edges_pos:
            ind=new_edges_pos.index([x,y])
            copy_of_map[y][x]=new_new_edges[ind][2]
            #print(new_new_edges[ind][2],end="")
        else:
            pass
            #print(".",end="")
    #print()

#print(copy_of_map)

# expand the map by one in each direction
expanded_map=[]
for y in range(len(all_y)):
    row1=[]
    for x in range(len(all_x)):
        row1.append(copy_of_map[y][x])
        row1.append(".") if copy_of_map[y][x] in [".","J","7","|"] else row1.append("-")
    expanded_map.append(row1)
    row2=[]
    for x in range(len(row1)):
        row2.append(".") if row1[x] in [".","-","J","L"] else row2.append("|")
    expanded_map.append(row2)
# adjust the y_mapping, x_mapping and all_y, all_x
y_mapping_new={}
x_mapping_new={}
all_y_new=[]
all_x_new=[]
for i in range(len(all_y)):
    y_mapping_new[i*2]=y_mapping[i]
    y_mapping_new[i*2+1]=y_mapping[i]
    all_y_new.append(y_mapping[i])
    all_y_new.append(y_mapping[i]+1)
for i in range(len(all_x)):
    x_mapping_new[i*2]=x_mapping[i]
    x_mapping_new[i*2+1]=x_mapping[i]
    all_x_new.append(x_mapping[i])
    all_x_new.append(x_mapping[i]+1)
y_mapping=y_mapping_new
x_mapping=x_mapping_new
all_y=all_y_new
all_x=all_x_new

copy_of_map=expanded_map


print(y_mapping)

# modified solution from day 10!

counter=0
symbol=None
within_loop=False
for y,l in enumerate(copy_of_map):
    print("".join(l))
    assert within_loop==False
    for x,ch in enumerate(l):
        if ch !="." and ch !="-":
            if symbol==None:
                if ch!="|":
                    symbol=ch
                within_loop=not within_loop
            else:
                #print(f"symbol={symbol}, x={x}, within_loop={within_loop}")
                match symbol:
                    case "F":
                        if ch=="J":
                            symbol=None
                        else:
                            within_loop=not within_loop
                            symbol=None
                    case "L":
                        if ch=="7":
                            symbol=None
                        else:
                            within_loop=not within_loop
                            symbol=None
        elif within_loop and ch==".":
            #print("yup")
            #counter+=1
            copy_of_map[y][x]="1"        
        else:
            # this should be the "-" case, so do nothing or when x==0 and not within_loop
            #print(x)
            pass

# print the map and color the enclosed area (just for fun, not necessary)
print("\n".join(["".join([str(ch).replace("F","┌").replace("L","└").replace("7","┐").replace("J","┘").replace("-","─").replace("|","│") if ch!="1" else "\033[91m1\033[0m" for ch in l]) for l in expanded_map]))

# add the differences between the coordinates (from x_mapping and y_mapping) if this and previous are both not "."

for y,l in enumerate(copy_of_map):
    for x,ch in enumerate(l):
        if ch!=".":
            if y< len(all_y) and x< len(all_x) and copy_of_map[y+1][x+1] !="." and copy_of_map[y+1][x]!="." and copy_of_map[y][x+1]!=".":
                counter+=(x_mapping[x+1]-x_mapping[x])*(y_mapping[y+1]-y_mapping[y])
            # horizontal edge
            # FJ
            # |.
            elif y< len(all_y) and x<len(all_x) and copy_of_map[y+1][x]=="." and copy_of_map[y][x+1]!=".":
                counter+=x_mapping[x+1]-x_mapping[x]
            # Vertical edge
            # 7.
            # L.
            elif y< len(all_y) and x<len(all_x) and copy_of_map[y+1][x]!="." and copy_of_map[y][x+1]==".":
                counter+=y_mapping[y+1]-y_mapping[y]



print(counter+1)
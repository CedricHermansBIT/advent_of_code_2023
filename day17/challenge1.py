with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[[int(x) for x in line.strip()] for line in ifile.readlines()]
        
#print(lines)

def get_neighbors(node):
    (x,y),pdir,psame=node
    neighbors=[]
    new=1 if pdir==0 else 0
    # pdir: N:1 E:2 S:3 W:4
    if x>0:
        if pdir==4:
            if psame<2: # don't allow more than 3 consecutive times the same direction
                neighbors.append(((x-1,y),4,psame+1))
        else:
            if pdir!=2: # don't go back
                neighbors.append(((x-1,y),4,new))
    if x<len(lines[0])-1:
        if pdir==2:
            if psame<2:
                neighbors.append(((x+1,y),2,psame+1))
        else:
            if pdir!=4:
                neighbors.append(((x+1,y),2,new))
    if y>0:
        if pdir==1:
            if psame<2:
                neighbors.append(((x,y-1),1,psame+1))
        else:
            if pdir!=3:
                neighbors.append(((x,y-1),1,new))
    if y<len(lines)-1:
        if pdir==3:
            if psame<2:
                neighbors.append(((x,y+1),3,psame+1))
        else:
            if pdir!=1:
                neighbors.append(((x,y+1),3,new))
    return neighbors

def A_star(start,goal):
    # To visit is a tuple containing ((x,y),previous_direction,count_of_same_direction)
    to_visit=set([(start,0,0)])
    visited={(start,0,0):None}

    #best_score={((x,y),pdir,prep):float("inf") for x in range(len(lines[0])) for y in range(len(lines)) for pdir in range(5) for prep in range(3)}
    best_score={}
    best_score[(start,0,0)]=0

    while to_visit:
        # get the node with the lowest score
        current=min(to_visit,key=lambda x: best_score[x])
        #print(f"Node: {current[0]}, pdir: {current[1]}, psame: {current[2]}, score: {best_score[current[0]]}")

        #input()
        to_visit.remove(current)
        #print(current)
        if current[0]==goal:
            print(best_score[current])
            #print(f"Currently best score: {best_score[goal]}")
            visited[current[0],0,0]=visited[current]
            return visited
        for neighbor in get_neighbors(current):
            if neighbor not in best_score or best_score[current]+lines[neighbor[0][1]][neighbor[0][0]]<best_score[neighbor]:
                #print(f"Found a better path to {neighbor[0]}, previous best: {best_score[neighbor[0]]}, new best: {best_score[current[0]]+lines[neighbor[0][1]][neighbor[0][0]]}")
                visited[neighbor]=current
                best_score[neighbor]=best_score[current]+lines[neighbor[0][1]][neighbor[0][0]]
                # we need to revisit the neighbor
                to_visit.add(neighbor)
    return visited

def get_path(visited,goal=(len(lines[0])-1,len(lines)-1)):
    path=[goal]
    current=visited[(goal,0,0)]
    path.append(current[0])
    while current!=None:
        print(current)
        current=visited[current]
        if current!=None:
            path.append(current[0])
    return path

#print(A_star((0,0),(len(lines[0])-1,len(lines)-1)))
visited=A_star((0,0),(len(lines[0])-1,len(lines)-1))
#print(visited[(12,11)])
# path=get_path(visited,(len(lines[0])-1,len(lines)-1))

# for y,line in enumerate(lines):
#     for x,point in enumerate(line):
#         if (x,y) in path:
#             print("O",end="")
#         else:
#             print(point,end="")
#     print()

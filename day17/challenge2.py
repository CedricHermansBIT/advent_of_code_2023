with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=[[int(x) for x in line.strip()] for line in ifile.readlines()]
        
#print(lines)
mindir=2
maxdir=9
from functools import lru_cache
@lru_cache(maxsize=None)
def get_neighbors(node):
    (x,y),pdir,psame=node
    neighbors=[]
    # pdir: N:1 E:2 S:3 W:4
    if x>0:
        if pdir==4 or pdir==0:
            if psame<maxdir: # don't allow more than 3 consecutive times the same direction
                neighbors.append(((x-1,y),4,psame+1))
        else:
            if pdir!=2 and psame>mindir: # don't go back
                #only add if there are at least mindir consecutive same directions
                if (x-mindir-1)>0:
                    neighbors.append(((x-1,y),4,0))
    if x<(len(lines[0])-1):
        if pdir==2 or pdir==0:
            if psame<maxdir:
                neighbors.append(((x+1,y),2,psame+1))
        else:
            if pdir!=4 and psame>mindir:
                if (x+mindir+1)<len(lines[0])-1:
                    neighbors.append(((x+1,y),2,0))
    if y>0:
        if pdir==1 or pdir==0:
            if psame<maxdir:
                neighbors.append(((x,y-1),1,psame+1))
        else:
            if pdir!=3 and psame>mindir:
                if (y-mindir-1)>0:
                    neighbors.append(((x,y-1),1,0))
    if y<(len(lines)-1):
        if pdir==3 or pdir==0:
            if psame<maxdir:
                neighbors.append(((x,y+1),3,psame+1))
        else:
            if pdir!=1 and psame>mindir:
                if (y+mindir+1)<len(lines)-1:
                    neighbors.append(((x,y+1),3,0))
    return neighbors

def manhattan_distance(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def A_star(start,goal):
    current_best=float("inf")
    # To visit is a tuple containing ((x,y),previous_direction,count_of_same_direction)
    to_visit=set([(start,0,-1)])
    visited={(start,0,-1):None}

    #best_score={((x,y),pdir,prep):float("inf") for x in range(len(lines[0])) for y in range(len(lines)) for pdir in range(5) for prep in range(3)}
    best_score={}
    best_score[(start,0,-1)]=0
    cbest=float("inf")

    #estimated_score={(y,x):manhattan_distance((x,y),goal) for x in range(len(lines[0])) for y in range(len(lines))}
    #print(estimated_score)

    while to_visit:
        # get the node with the lowest score
        current=min(to_visit,key=lambda x: best_score[(x[0],x[1],min(x[2],mindir+1))])#+estimated_score[x[0]])
        #print(f"Node: {current[0]}, pdir: {current[1]}, psame: {current[2]}, score: {best_score[current]}")

        #input()
        to_visit.remove(current)
        # if current score is worse than the current best, just skip it
        current_clamped=(current[0],current[1],min(current[2],mindir+1))
        if best_score[current_clamped]>current_best:
            continue
        if best_score[current_clamped]!=cbest:
            # sort to_visit by best_score
            cbest=best_score[current_clamped]
            print(cbest,len(to_visit))
        #print(current)
        if current[0]==goal and current[2]>mindir:
            print(best_score[current_clamped], len(to_visit))
            current_best=best_score[current_clamped]
            #print(f"Currently best score: {best_score[goal]}")
            visited[current[0],0,0]=visited[current]
            #return visited
        for neighbor in get_neighbors(current):
            neighbor_clamped=(neighbor[0],neighbor[1],min(neighbor[2],mindir+1))
            if neighbor not in best_score or best_score[current_clamped]+lines[neighbor[0][1]][neighbor[0][0]]<best_score[neighbor_clamped]:
                #print(f"Found a better path to {neighbor[0]}, previous best: {best_score[neighbor[0]]}, new best: {best_score[current[0]]+lines[neighbor[0][1]][neighbor[0][0]]}")
                visited[neighbor]=current
                best_score[neighbor_clamped]=best_score[current_clamped]+lines[neighbor[0][1]][neighbor[0][0]]
                # we need to revisit the neighbor
                to_visit.add(neighbor)
    return visited

def get_path(visited,goal=(len(lines[0])-1,len(lines)-1)):
    path=[goal]
    current=visited[(goal,0,0)]
    path.append(current[0])
    while current!=None:
        #print(current)
        current=visited[current]
        if current!=None:
            path.append(current[0])
    return path

#print(A_star((0,0),(len(lines[0])-1,len(lines)-1)))
visited=A_star((0,0),(len(lines[0])-1,len(lines)-1))
#print(visited[(12,11)])
path=get_path(visited,(len(lines[0])-1,len(lines)-1))

for y,line in enumerate(lines):
    for x,point in enumerate(line):
        if (x,y) in path:
            print("O",end="")
        else:
            print(point,end="")
    print()

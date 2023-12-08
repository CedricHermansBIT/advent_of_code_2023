with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.readlines()
steps=[int(x) for x in list(lines[0].strip().replace("L","0").replace("R","1"))]
print(steps)

graph={}
current_nodes=[]
final_nodes=[]
for line in lines[2:]:
    graph[k:=line[0:3]]=[line[7:10],line[12:15]]
    if k.endswith("A"):
        current_nodes.append(k)
    if k.endswith("Z"):
        final_nodes.append(k)

final_nodes = set(final_nodes)
current_nodes = set(current_nodes)
print(len(current_nodes))

intersecting_steps=[]

# let's check if a current_node always ends up at the same final_node
for current_node in current_nodes:
    k=current_node
    step_counter=0
    first=None
    first_step=None
    while k not in final_nodes:
        k=graph[k][steps[step_counter%len(steps)]]
        step_counter+=1
    first=k
    first_step=step_counter
    k=graph[k][steps[step_counter%len(steps)]]
    step_counter+=1
    while k not in final_nodes:
        k=graph[k][steps[step_counter%len(steps)]]
        step_counter+=1
    if k!=first:
        print("nope")
    else:
        print("yep")
    print(f"{current_node} -> {k}, first occurence at {first_step}, second occurence at {step_counter}, so a period of {step_counter-first_step}")
    intersecting_steps.append(first_step)
    # yes, they do, moreover, they start at the beginning of the period, so we can just take the first one, and we don't need to worry about the starting index

# now let's find the least common multiple of all these periods
from math import lcm
# we know we have 6 starting nodes, so we can hardcode this
current=intersecting_steps[0]
for i in range(len(intersecting_steps)-1):
    current=lcm(current,intersecting_steps[i+1])

print(current)


        

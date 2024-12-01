import itertools
import tqdm
total=0
borders={"x":[],"m":[],"a":[],"s":[]}
#with open("challengeinput.txt","r") as ifile:
with open("testinput.txt","r") as ifile:
    # px{a<2006:qkq,m>2090:A,rfg}
    # pv{a>1716:R,A}
    #
    # {x=787,m=2655,a=1222,s=2876}

    instructions=True
    for line in ifile:
        if line=="\n":
            instructions=False
            continue
        if instructions:
            # create dynamic functions based on input
            rulename = line.split("{")[0]
            if rulename=="in":
                rulename="in_"
            parts=line.split("{")[1].split("}")[0].split(",")
            custom_exec = "def {}(value):\n".format(rulename)
            #custom_exec += "    print(\"{}\")\n".format(rulename)
            for part in parts:
                if ":" in part:
                    spart=part.split(":")
                    borders[spart[0][0]].append((int(spart[0][2:]),spart[0][1]))
                    custom_exec += "    if value['{}']{}{}:\n".format(spart[0][0],spart[0][1],spart[0][2:])
                    if spart[1] not in ["A","R"]:
                        custom_exec += "        return {}(value)\n".format(spart[1])
                    else:
                        custom_exec += "        return '{}'\n".format(spart[1])
                else:
                    if part not in ["A","R"]:
                        custom_exec += "    return {}(value)\n".format(part)
                    else:
                        custom_exec += "    return '{}'\n".format(part)
            exec(custom_exec)

# test borders
#borders={"x":[(1416,"<"),(1716,"<")],"m":[(0,">"),(2090,">")],"a":[(0,">")],"s":[(0,">")]}

# sort the borders
for k in borders:
    borders[k].sort()
    if borders[k][-1][1]=="<" and borders[k][-1][0]!=4000:
        borders[k].append((4000,"<"))
    if borders[k][0][1]==">" and borders[k][0][0]!=0:
        borders[k].insert(0,(0,">"))
    borders[k].sort()

print(borders)

length_of_different_values=[len(borders["x"]),len(borders["m"]),len(borders["a"]),len(borders["s"])]
inds={0:"x",1:"m",2:"a",3:"s"}

def get_checks(ni,nv,i):
    print("i",i)
    check_list=[]
    # 0 case at start
    if ni == 0:
        if nv[1] == "<": # case for example (20,'<')
            d = nv[0] - 1
            print(f"0-{nv[0]}")
            check_list.append((nv[0] - 0.5, d))
        else: # case always example (0,'>')
            next=borders[inds[i]][ni + 1]
            d = next[0]
            if next[1] == "<":
                d -= 1
            print(f"0-{next[0]}")
            check_list.append((nv[0] + 0.5, d))
    # 4000 case at end
    elif ni == length_of_different_values[i] - 1:
        if nv[1] == ">":
            d = 4000 - nv[0]
            print(f"{nv[0]}-4000")
            check_list.append((nv[0] + 0.5, d))
        else: # case always (4000,'<')
            prev=borders[inds[i]][ni - 1]
            d = nv[0] - prev[0]
            if prev[1] == ">":
                d -= 1
            print(f"{prev[0]}-{nv[0]}")
            check_list.append((nv[0] - 0.5, d))
    # everything else
    else:
        if nv[1] == ">":
            next=borders[inds[i]][ni + 1]
            d = next[0] - nv[0]
            if next[1] == "<":
                d -= 1
            print(f"{nv[0]}-{next[0]}")
            check_list.append((nv[0] + 0.5, d))
            # if previous is <, we need to check the intermediate part
            prev=borders[inds[i]][ni - 1]
            print('yup')
            if prev[1] == "<":
                d = nv[0] - prev[0]
                if prev[1] == ">":
                    d -= 1
                print(f"{prev[0]}-{nv[0]}")
                check_list.append((nv[0] - 0.5, d))
        else: # case always <
            prev=borders[inds[i]][ni - 1]
            d = nv[0] - prev[0]
            if prev[1] == ">":
                d -= 1
            print(f"{prev[0]}-{nv[0]}")
            check_list.append((nv[0] - 0.5, d))
           
    return check_list

tsum=0
areas=set()
for xi,xv in enumerate(borders["x"]):
    to_check=[[],[],[],[]]
    to_check[0]=get_checks(xi,xv,0)
    for mi,mv in enumerate(borders["m"]):
        to_check[1]=get_checks(mi,mv,1)
        to_check[2:]=[[],[]]
        for ai,av in enumerate(borders["a"]):
            to_check[2]=get_checks(ai,av,2)
            to_check[3]=[]
            for si,sv in enumerate(borders["s"]):
                to_check[3]=get_checks(si,sv,3)

                # to check is the list of x, m, a and s values that need to be checked stored as tuples (value, length)
                # we increase or decrease the value by 0.5 to make sure it is smaller or larger than the border (don't need to worry about > or <)
                    
                #print("to_check",to_check)
                for combi in itertools.product(*to_check):
                    v={"x":combi[0][0],"m":combi[1][0],"a":combi[2][0],"s":combi[3][0]}
                    result=in_(v)
                    #print(v,result, combi[0][1],combi[1][1],combi[2][1],combi[3][1], combi[0][1]*combi[1][1]*combi[2][1]*combi[3][1])
                    # this is a hack to make sure we don't count the same area twice, because sometimes we do check from both sides because flawed logic on my end
                    if combi[0][1]*combi[1][1]*combi[2][1]*combi[3][1] not in areas:
                        areas.add(combi[0][1]*combi[1][1]*combi[2][1]*combi[3][1])
                    if result=="A":
                            total+=combi[0][1]*combi[1][1]*combi[2][1]*combi[3][1]
                    
                    tsum+=combi[0][1]*combi[1][1]*combi[2][1]*combi[3][1]
                    #print(v,result)
#for x,m,a,s in tqdm.tqdm(itertools.product(borders["x"],borders["m"],borders["a"],borders["s"])):
#    v={"x":x,"m":m,"a":a,"s":s}
#    result=in_(v)
     #if result=="A":
    #    total+=
print(total)
print(tsum)

        

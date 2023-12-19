import itertools
import tqdm
total=0
borders={"x":[],"m":[],"a":[],"s":[]}
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
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
            for part in parts:
                if ":" in part:
                    spart=part.split(":")
                    borders[spart[0][0]].append(int(spart[0][2:]))
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
print(borders)
for x,m,a,s in tqdm.tqdm(itertools.product(borders["x"],borders["m"],borders["a"],borders["s"])):
    v={"x":x,"m":m,"a":a,"s":s}
    result=in_(v)
    if result=="A":
        total+=
print(total)

            

        

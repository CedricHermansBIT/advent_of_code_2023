with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    content=ifile.read()

patterns=[lines.split("\n") for lines in content.split("\n\n")]

def difference_lines(line1,line2):
    return sum([1 for i in range(len(line1)) if line1[i]!=line2[i]])==1


# Note: very similar to the first challenge, but now we need to hava had 1 mismatch in the symmetry axis
# we don't need to fix the mismatch, just keep track if we had one or not
def check_pattern(pattern):
    for i in range(len(pattern)-1):
        #print(f"i={i}, pattern[i]={pattern[i]}, pattern[i+1]={pattern[i+1]}")
        smudge_fixed=False
        if pattern[i]==pattern[i+1] or (smudge_fixed:=difference_lines(pattern[i],pattern[i+1])==1):
            rows_till_start=i
            rows_till_end=len(pattern)-i-2
            maxtests=min(rows_till_start,rows_till_end)
            for j in range(maxtests):
                #print(f"i={i}, j={j}, pattern[i-j-1]={pattern[i-j-1]}, pattern[i+j+2]={pattern[i+j+2]}")
                if pattern[i-j-1]!=pattern[i+j+2]:
                    if difference_lines(pattern[i-j-1],pattern[i+j+2])==1:
                        smudge_fixed=True
                    else:
                    #print("row symmetry not found")
                        break
            else:
                # Only if we actually had a mismatch, we found a symmetry. Otherwise it's the old solution which is no longer valid
                if smudge_fixed:
                    return i+1 # the number of rows before the symmetry axis
                #print("row symmetry found")
    else:
        #print("row symmetry not found")
        return False

print(patterns)

total=0
for pattern in patterns:
    pfound=False
    # check symmetry in rows first
    total+=check_pattern(pattern)*100
    if check_pattern(pattern):
        pfound=True
    # check symmetry in columns
    # swap rows and columns
    pattern=["".join(x) for x in list(zip(*pattern))]
    total+=check_pattern(pattern)
    if check_pattern(pattern):
        pfound=True
    if not pfound:
        joined_pattern="\n".join(pattern)
        print("no symmetry found",f"pattern=\n{joined_pattern}")

print(total)
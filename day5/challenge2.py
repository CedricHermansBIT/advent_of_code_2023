with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.read()

sections=lines.split("\n\n")

# Testcases (uncomment one of the following lines with testinput.txt for easy debugging)
# Note: also the actual seeds need to be commented out, so we just have one single testcase

# first rule testcase: 50 98 2
# test no overlap:
#seeds=[(100,1)]
# test complete overlap:
#seeds=[(98,2)]
# test partial overlap (left side):
#seeds=[(97,2)]
# test partial overlap (right side):
#seeds=[(99,2)]
# test partial overlap (both sides):
#seeds=[(97,5)]


# seed, seedlen
seeds=[int(x) for x in sections[0].split(" ")[1:]]
seeds=[(seeds[n],seeds[n+1]) for n in range(0,len(seeds),2)]

# note to self: dest,src,len
steps=[[[int(y) for y in x.split(" ")]  for x in sections[n].split("\n")[1:]] for n in range(1,len(sections))]
#for step in steps:
#    print(step)
nextstep=[]
for step in steps:
    for seed,seedlen in seeds:
        max_seed=seed+seedlen
        for (nextstep_dest,step_left,step_len) in step:
            # if there is overlap, we will need to shift the overlapping part with "shift"
            shift=nextstep_dest-step_left

            # step_right is the rightmost position of the step
            step_right=step_left+step_len

            # check if there is no overlap
            if max_seed<=step_left or seed>=step_right:
                # no overlap, so seed is not changed, but we need to check all steps
                #print(f"seed {seed} is not in step {step_left} {step_len}, so it is not transformed")
                continue

            # if we get here, there is overlap
            # check if the seed is completely inside the step
            if seed>=step_left and max_seed<=step_right:
                # example: seed=3, seedlen=2, step_left=2, step_len=5 => max_seed=5, step_right=7
                # seed is completely inside the step, so it is transformed
                nextstep.append((seed+shift,seedlen))
                print(f"seed {seed} is completely inside step {step_left} {step_len}, so it is transformed to {seed+shift}")
                break

            # check if the seed is partially inside the step 
            # left side inside range, but right side outside range
            if seed>=step_left and max_seed>step_right:
                # example: seed=3, seedlen=5, step_left=2, step_len=5 => max_seed=8, step_right=7
                # split into two seeds
                # seed 1: seed, step_right-seed => 3,4
                # seed 2: step_right, max_seed-step_right => 7,1
                nextstep.append((seed+shift,step_right-seed))
                seeds.append((step_right,max_seed-step_right))
                print(f"seed {seed} is partially inside step {step_left} {step_len}, so it is split into {seed+shift} {step_right-seed} and {step_right} {max_seed-step_right}")
                break
            # right side inside range, but left side outside range
            elif seed<step_left and max_seed<=step_right:
                # example: seed=1, seedlen=5, step_left=2, step_len=5 => max_seed=6, step_right=7
                # split into two seeds
                # seed 1: seed, step_left-seed => 1,1
                # seed 2: step_left, max_seed-step_left => 2,4
                seeds.append((seed,step_left-seed))
                nextstep.append((step_left+shift,max_seed-step_left))
                print(f"seed {seed} is partially inside step {step_left} {step_len}, so it is split into {seed} {step_left-seed} and {nextstep_dest} {max_seed-step_left}")
                break
            # left side outside range, right side outside range (step completely inside seed)
            elif seed<step_left and max_seed>step_right:
                # example: seed=1, seedlen=10, step_left=2, step_len=5 => max_seed=11, step_right=7
                # split into three seeds
                # seed 1: seed, step_left-seed => 1,1
                # seed 2: step_left, step_right-step_left => 2,5
                # seed 3: step_right, max_seed-step_right => 7,4
                seeds.append((seed,step_left-seed))
                nextstep.append((nextstep_dest,step_right-step_left))
                seeds.append((step_right,max_seed-step_right))
                print(f"seed {seed} is partially inside step {step_left} {step_len}, so it is split into {seed} {step_left-seed} and {nextstep_dest} {step_right-step_left} and {step_right} {max_seed-step_right}")
                break
            else:
                assert False, "this should never happen"
        else:
            # if we never breaked, then the seed is not in any of the steps, and the seed is not transformed
            nextstep.append((seed,seedlen))
            print(f"seed {seed} is not in any of the steps, so it is not transformed")
    print(nextstep)
    seeds=nextstep
    nextstep=[]

print(min([seed for (seed,_) in seeds]))
import re,itertools

counter=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        springs,numbers=line.strip().split(" ")
        numbers=numbers.split(",")
        # make all combinations by replacing "?" with all combinations of "#" and "."
        combinations=[]
        # make all combinations of "#" and "." for the number of "?" in springs
        for i in itertools.product(["#","."],repeat=springs.count("?")):
            combinations.append(i)
        # replace the "?" with the combinations
        possibilities=[]
        for combination in combinations:
            possibility=springs
            for char in combination:
                possibility=possibility.replace("?",char,1)
            possibilities.append(possibility)
        #print(possibilities)
        regex=r"^\.*"
        for num in numbers:
            regex+=r"#{%s}"%num
            regex+=r"\.+"
        # remove the last "+"
        regex=regex[:-1]
        regex+=r"*$"
        print(regex)
        #check if the possibilities match the regex
        for possibility in set(possibilities):
            if re.match(regex,possibility):
                #print(possibility)
                counter+=1
        #exit()
print(counter)
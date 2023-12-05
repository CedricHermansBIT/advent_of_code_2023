cards=[]
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    lines=ifile.readlines()
    lines.reverse()
    totallines=len(lines)
    for i,line in enumerate(lines):
        winning, mynumbers= line.split(":")[1].split("|")
        winning=[x for x in winning.strip().split()]
        mynumbers=[x for x in mynumbers.strip().split()]
        amount_winning=sum([1 for x in winning if x in mynumbers])
        print(cards)
        if amount_winning==0:
            cards.append(0)
        else:
            card_val=0
            for j in range(amount_winning):
                card_val+=cards[-1-j]+1
            cards.append(card_val)

print(sum(cards)+totallines)


        

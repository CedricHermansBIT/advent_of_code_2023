cards={}
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt","r") as ifile:
    for line in ifile:
        c,v = line.strip().split(" ")
        # replace the letters in descending order of values (for sorting later on, kinda hacky)
        c=c.replace("A","Z")
        c=c.replace("K","Y")
        c=c.replace("Q","X")
        c=c.replace("J","0") # J is now lowest value! (could be one as well, but 0 to keep it clear and not confuse with A)
        c=c.replace("T","V")
        cards[c]=v

print(cards)
        
types={"fioak":[], "fooak":[], "fh":[],"troak":[],"tp":[],"pair":[],"high":[]} #five of a kind, four of a kind, full house, three of a kind, two pair, pair, high card
# types ordered from lowest to highest (to retrieve ranks at the end)
types_in_order_of_value = ["high","pair","tp","troak","fh","fooak","fioak"]

# sort cards into types
for card in cards:
    sets=set(list(card))
    counts={y:card.count(y) for y in sets}
    if "0" in sets and len(sets)>1:
        J_count=counts["0"]
        sets.remove("0")
        counts.pop("0")
        max_key=max(counts, key=counts.get)
        counts[max_key]+=J_count

    if len(sets)==1:
        types["fioak"].append(card)
    elif len(sets)==2:
        if 4 in counts.values():
            types["fooak"].append(card)
        else:
            types["fh"].append(card)
    elif len(sets)==3:
        if 3 in counts.values():
            types["troak"].append(card)
        else:
            types["tp"].append(card)
    elif len(sets)==4:
        types["pair"].append(card)
    else:
        types["high"].append(card)

# sort cards in each type based on the card
for t in types:
    types[t].sort()

result=0
counter=1
for t in types_in_order_of_value:
    for card in types[t]:
        result+=int(cards[card])*counter
        counter+=1

print(result)
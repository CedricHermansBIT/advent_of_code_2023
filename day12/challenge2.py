import re
import functools

def possible_placements(springs, length):
    # find all possible placements of the number
    # [^\.]{length}[^#] matches a number of non-dot characters, followed by a non-hash character
    # so basically, if the number would be 3, it would match ###, ?##, ??#, ???, ?#?, #??, #?#, #??, ##? but nothing with a . or # as fourth character
    for m in re.finditer(r"(?=([^\.]{" + str(length) + r"}[^#]))", springs):
        # get the index of the first character of the match
        i = m.span(1)[0]
        # if there is a hash before the match, then it's invalid
        if '#' in springs[:i]:
            break
        # return everything after the match
        yield springs[i + length + 1:]

@functools.lru_cache(maxsize=None)
def count_placements(springs, numbers):
    # if we run out of numbers, but there are still # left, then it's invalid
    if not numbers:
        return '#' not in springs # True if there are no # left, False if there are (so 1 and 0)
    # get the first number and the rest
    first_number, rest_numbers = numbers[0], numbers[1:]

    s=0
    # as long as there are possible placements, recurse
    for rest_condition in possible_placements(springs, first_number):
        s+=count_placements(rest_condition, rest_numbers)
    return s



counter=0
with open("challengeinput.txt","r") as ifile:
#with open("testinput.txt") as ifile:
    for line in ifile:
        springs, numbers = line.strip().split()
        nsprings=springs
        nnumbers=numbers
        # add 4 times the springs and numbers
        for _ in range(4):
            nsprings+="?"+springs
            nnumbers+=","+numbers
        # add a dot at the end (for easier regex matching)
        springs=nsprings+"."
        # convert the numbers to a tuple of ints, so it can be hashed
        numbers=tuple([int(x) for x in nnumbers.split(",")])
        counter+=count_placements(springs, numbers)
print(counter)
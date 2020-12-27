import string
test = ["abcd\nabcs", "cdef\ncder"]
file = open("input.txt").read()
text = file.split('\n\n')
def makegroups(inputs):
    groups = []
    for i in inputs:
        groups.append(i.replace("\n", ""))
    return(groups)

def parsegroups(inputs2):
    parsedgroups = []
    for i in inputs2:
        parsedgroups.append("".join(set(i)))
    return(parsedgroups)

def part1(inputs3):
    answer = 0
    for i in inputs3:
        answer = answer + len(i)
    return(answer)

def personlist(inputs4):
    indreslist = []
    for i in inputs4:
        temp1 = i.split("\n")
        indreslist.append(temp1)
    return(indreslist)

    
def part2(inputs5, part1list):
    answer2 = 0
    chars = string.ascii_lowercase
    for i, x in zip(inputs5, part1list):
        if len(i) == 1:
            answer2 = answer2 + len(i[0])
        else:
            countmatch = 0
            for ch in chars:
                match = x.count(ch)
                if match == len(i):
                    countmatch = countmatch + 1
                else:
                    pass
            answer2 = answer2 + countmatch
    return(answer2)
print(part2(personlist(text),makegroups(text)))
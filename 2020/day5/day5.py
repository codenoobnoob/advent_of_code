import operator
file = open("input.txt").read()
text = file.split('\n')
text.sort()
ops = {"+": operator.add, "-": operator.sub}
rows = 128
seats = 8
divr1 = rows/2
divr2 = divr1/2
divr3 = divr2/2
divr4 = divr3/2
divr5 = divr4/2
divr6 = divr5/2
divr7 = divr6/2
divr8 = divr7/2
divs1 = seats/2
divs2 = divs1/2
divs3 = divs2/2
divs4 = divs3/2

def part1(inputtext):
    listboard = []
    for i in inputtext:
        test = i.replace("F", "-")
        test2 = test.replace("B", "+")
        test3 = test2.replace("R", "+")
        test4 = test3.replace("L", "-")
        rowNum = ((ops[test2[6]]((ops[test2[5]]((ops[test2[4]]((ops[test2[3]]((ops[test2[2]]((ops[test2[1]]((ops[test2[0]](divr1,divr2)),divr3)),divr4)),divr5)),divr6)),divr7)),divr8))-0.5)
        seatNum =(((ops[test4[9]]((ops[test4[8]]((ops[test4[7]](divs1,divs2)),divs3)),divs4)))-0.5)
        boardingpass = int((rowNum*8)+seatNum)
        listboard.append(boardingpass)
        listboard.sort()
    return(listboard)

def rownumber(bincode):
    rep1 = bincode.replace("F", "-").replace("B", "+")
    rowNum = ((ops[rep1[6]]((ops[rep1[5]]((ops[rep1[4]]((ops[rep1[3]]((ops[rep1[2]]((ops[rep1[1]]((ops[rep1[0]](divr1,divr2)),divr3)),divr4)),divr5)),divr6)),divr7)),divr8))-0.5)
    return(int(rowNum))

def seatnumber(binseat):
    rep2 = binseat.replace("R", "+").replace("L", "-")
    seatNum =(((ops[rep2[9]]((ops[rep2[8]]((ops[rep2[7]](divs1,divs2)),divs3)),divs4)))-0.5)
    return(int(seatNum))

def rowlist(inputs):
    listbyrows = []
    inputs.sort()
    activerow = inputs[0][:-3]
    templist = [rownumber(inputs[0])]
    for i in inputs:
        if i[:-3] == activerow:
            #rowNo = rownumber(i)
            #if rowNo in templist:
            templist.append(seatnumber(i))
            #else:
            #    templist.extend([rowNo, seatnumber(i)])
        else:
            listbyrows.append(templist)
            templist = []
            activerow = i[:-3]
            templist.extend([rownumber(i), seatnumber(i)])
    return(listbyrows)

def checkrows(thelist):
    for i in range(min(thelist), max(thelist)):
        if i in thelist:
            pass
        else:
            print(i)
    print("finished")

checkrows(part1(text))
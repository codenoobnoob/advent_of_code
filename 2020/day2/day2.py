file = open("input.txt").read()

def parseInput(inputText):
    numlist = inputText.split('\n')
    result = []
    for i in numlist:
        x = i.split(':')
        itemset = tuple((x[0], x[1].strip()))
        result.append(itemset)
        
    return result

def pwCheck(thisList):
    result = 0
    for i in thisList:
        criteria = i[0].split(" ")
        nums = criteria[0].split("-")
        firstNum = nums[0]
        secondNum = nums[1]
        numOccurrance = i[1].count(criteria[1])
        if int(firstNum) <= numOccurrance <= int(secondNum):
            result = result + 1
        else:
            pass
    print(result)

def pwCheck2(thisList):
    result = 0
    for i in thisList:
        criteria = i[0].split(" ")
        nums = criteria[0].split("-")
        firstNum = int(nums[0])-1
        secondNum = int(nums[1])-1
        if criteria[1] == i[1][firstNum] and criteria[1] != i[1][secondNum]:
            result = result + 1
        elif criteria[1] != i[1][firstNum] and criteria[1] == i[1][secondNum]:
            result = result + 1
        else:
            pass
    print(result)


parsedFile = parseInput(file)
pwCheck2(parsedFile)
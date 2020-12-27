file = open("input.txt").read()
test = file.split(".\n")


def dicbags(inputs):
    test2 = {}
    for i in inputs:
        b = i.strip(".")
        x = b.replace(" bags", "").replace(" bag", "").replace(
            " no ", " 0 ").split(" contain ")
        inside = x[1].split(", ")
        test4 = {}
        for ch in inside:
            test4[ch[1:].strip(" ")] = int(ch[0])
        test2[x[0]] = test4
    for x in test2.values():
        if "other" in x.keys():
            x.pop("other")
    return(test2)


def recursion(bag2check, inputm, array):
    for i, x in inputm[bag2check].items():
        if inputm[i] != {}:
            global counter 
            counter += x*array
            recursion(i, inputm, (x*array))
        else:
            counter += array*x
    return()

counter = 0
print(recursion("shiny gold", dicbags(test), 1))
print(counter)

def start(inputd):
    print(inputd)
    insidebags=inputd["shiny gold"]
    counter=0
    tempbags={}
    while insidebags != {}:
        tempbags={}
        counter2=0
        for x in insidebags.values():
            counter2 += x
        for i, num in insidebags.items():
            counter3=0
            for x, num2 in inputd[i].items():
                counter3 += counter2 + num*num2
                tempbags.update(inputd[x])
        counter += counter3
        insidebags=tempbags
    return(counter)



answer=[]


def checks(inputs3, bagcheck):
    bags=list(inputs3.keys())
    insides=list(inputs3.values())
    for i in insides:
        if bagcheck in i:
            answer.append(bags[insides.index(i)])
    return(inputs3)


def checks2(inputs4, bagcheck2):
    bags=list(inputs4.keys())
    insides=list(inputs4.values())
    for x in bagcheck2:
        for i in insides:
            templist=[]
            if x in i:
                templist.append(bags[insides.index(i)])
            else:
                pass
            answer.extend(templist)
    return(inputs4)

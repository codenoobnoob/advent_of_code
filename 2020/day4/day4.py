import re

file = open("input.txt").read()
text = file.split('\n\n')

def listparse(textToParse):
    newText = []
    tempdict = {}
    for i in textToParse:
        tempdict = re.split(r'\s|\n', i)
        newText.append(tempdict)
    return(newText)
#listan listoissa on oikeat muodot mutta "pid:89320842" pitää saada muotoon "pid":89320842, jne ja setit kirjastoiksi 
def parse2(testlist):
    newlist = []
    for y in testlist:
        tempdict ={}
        for i in y:
            keyvalue = i.split(":")
            tempdict[keyvalue[0]] = keyvalue[1]
        newlist.append(tempdict)
    return(newlist)

def byrcheck(byrdict):
    validbyr = 0
    try:
        if 1920 <= int(byrdict["byr"]) <= 2002:
            validbyr = 1
        else:
            pass
    except:
        pass
    return(validbyr)

def iyrcheck(iyrdict):
    validiyr = 0
    try:
        if 2010 <= int(iyrdict["iyr"]) <= 2020:
            validiyr = 1
    except:
        pass 
    return(validiyr)

def eyrcheck(eyrdict):
    valideyr = 0
    try:
        if 2020 <= int(eyrdict["eyr"]) <= 2030:
            valideyr = 1
    except:
        pass 
    return(valideyr)

def hgtcheck(hgtdict):
    validhgt = 0
    try:
        if hgtdict["hgt"][-2:] == "cm":
            if 150 <= int(hgtdict["hgt"][:-2]) <= 193:
                validhgt = 1
            else: pass
        elif hgtdict["hgt"][-2:] == "in":
            if 59 <= int(hgtdict["hgt"][:-2]) <= 76:
                validhgt = 1
            else: pass
    except:
        pass 
    return(validhgt)

def hclcheck(hcldict):
    validhcl = 0
    try:
        p = re.compile("#[a-f0-9]{6,6}")
        if (p.match(hcldict["hcl"]).span())[1] == 7 and len(hcldict["hcl"]) == 7:
            validhcl = 1
    except:
        pass
    return(validhcl)

def eclcheck(ecldict):
    validecl = 0
    eyecolor = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    try:
        if ecldict["ecl"] in eyecolor:
            validecl = 1 
        else: 
            pass
    except:
        pass
    return(validecl)

def pidcheck(piddict):
    validpid = 0
    r = re.compile("[0-9]{9}")
    try:
        if (r.match(piddict["pid"]).span())[1] == 9 and len(piddict["pid"]) == 9:
            validpid = 1
    except:
        pass
    return(validpid)

def part1(inputs):
    validcount = 0
    for i in inputs:
        keylist = i.keys()
        if "byr" in keylist:
            if "iyr" in keylist:
                if "eyr" in keylist:
                    if "hgt" in keylist:
                        if "hcl" in keylist:
                            if "ecl" in keylist:
                                if "pid" in keylist:
                                    validcount = validcount + 1
                                else: pass
                            else: pass
                        else: pass
                    else: pass
                else: pass
            else: pass
        else: pass
    return(validcount)

def part2(inputs2):
    validcount2 = 0
    for i in inputs2:
        if (byrcheck(i)*iyrcheck(i)*eyrcheck(i)*hgtcheck(i)*hclcheck(i)*eclcheck(i)*pidcheck(i)) == 1:
            validcount2 = validcount2 + 1
        else: 
            pass
    return(validcount2)

print(part2(parse2(listparse(text))))
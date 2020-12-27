file = open("input.txt").read()
test = file.split("\n")
puzzle = list(list((i[:3], int(i[4:].strip("+")))) for i in test)
#for i in test:
#    tupling = tuple(i[:3], int(i[4:].strip("+")))
accumulator = 0
index = 0
indexlist = []
def program(data, move):
    global indexlist
    global accumulator
    global index
    if move in indexlist:
        return(False)
        #return(f"Program interupted with {accumulator} in accu. The index is {move-1} and the operator is {data[move-1][0]}")
    else: 
        indexlist.append(move)
    if index <= (len(data)-1):
        if data[move][0] == "acc":
            accumulator += data[index][1]
            index += 1
            return(program(data, index))
        elif data[move][0] == "jmp":
            index += data[index][1]
            return(program(data, index))
        else:
            index += 1
            return(program(data, index))
    else:
        return(True)

def programfix(data):
    global accumulator
    global index
    global indexlist
    backup = data
    modified_data = data
    for indx, i in enumerate(data):
        accumulator = 0
        index = 0
        indexlist = []
        if i[0] == "acc":
            continue
        else:
            if i[0] == "jmp":
                modified_data[indx][0] = "nop"
                if program(modified_data, index):
                    return(accumulator)
                else:
                   modified_data[indx][0] = "jmp" 
            elif i[0] == "nop":
                modified_data[indx][0] = "jmp"
                if program(modified_data, index):
                    return(accumulator)
                else:
                   modified_data[indx][0] = "nop" 
        
print(programfix(puzzle))
file = open("input.txt").read()
line_list = file.split("\n")
puzzle = [int(i) for i in line_list]
puzzle.append((max(puzzle)+3))
puzzle.append(0)
puzzle.sort()

def part1(data):
    ones = 0
    threes = 0
    part_two_list = []
    for indx, i in enumerate(data):
        try:
            if (data[indx+1]) - i == 1:
                part_two_list.append(1)
                ones = ones + 1
            elif (data[indx+1]) - i == 3:
                part_two_list.append(3)
                threes = threes + 1
            elif (data[indx+1]) - i == 2:
                part_two_list.append(2)
            else:
                continue
        except:
            pass
    return((ones * threes), part_two_list)

def part2(data):
    count_ones_list = []
    counter = 0
    for i in data:
        if i == 1:
            counter = counter + 1
        elif i == 3:
            if counter >= 1:
                count_ones_list.append(counter)
                counter = 0
            else:
                counter = 0
    possibilities = 1 
    for i in count_ones_list:
        if i <= 3:
            possibilities = possibilities * (2 ** (i-1))
        elif i > 3:
            possibilities = possibilities * ((2 ** 2)+((i-3)*3))
    return(possibilities)


print(part2(part1(puzzle)[1]))

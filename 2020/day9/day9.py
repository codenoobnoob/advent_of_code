file = open("input.txt").read()
line_list = file.split("\n")
puzzle = [int(i) for i in line_list]

def parser(num_to_check, list_to_check):
    for i in list_to_check:
        for x in list_to_check:
            if i + x == num_to_check:
                return(True)
    return(False)

def part1(data, preamble):
    for indx, i in enumerate(data[(preamble):]):
        preamble_list = data[indx:(indx+preamble)]
        if parser(i, preamble_list) == False:
            return(i, (indx+preamble))


def parser2(start_index, data, num_to_add):
    calc = 0
    match_list = []
    for i in data[(start_index-len(data)):]:
        calc = calc + i 
        match_list.append(i)
        if calc < num_to_add:
            continue
        elif calc > num_to_add:
            return(False, 0)
        elif calc == num_to_add:
            return(True, (min(match_list)+max(match_list)))


def part2(data, preamble):
    start_num = part1(data, preamble)[0]
    start_index = (part1(data, preamble)[1])
    print(start_num)
    for i in range(len(data[0:(start_index)])):
        new_index = start_index - (i+1)
        if parser2(new_index, data, start_num)[0]:
            return(parser2(new_index, data, start_num)[1])
        else:
            pass
    return(False)

print(part2(puzzle, 25))


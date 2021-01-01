my_file = open("input.txt")
content = my_file.read()
content_split = content.split("\n")
global same_counter
global main_counter
global puzzle
same_counter = 0
main_counter = 0
puzzle = {}


def content_parse(content):
    for indx, i in enumerate(content):
        for indx2, x in enumerate(i):
            puzzle[tuple((indx, indx2))] = x
    return(puzzle)


content_parse(content_split)


def seat_check(loc, seat):
    global same_counter
    if seat == "L" or seat == "#":
        return(surrounding_check(loc, seat))
    else:
        same_counter += 1
        return((loc, seat))


def surrounding_check(loc, seat):
    global same_counter
    global puzzle
    occupied_counter = 0
    vacant_counter = 0
    for i in [-1, 0, 1]:
        for x in [-1, 0, 1]:
            if i == 0 and x == 0:
                continue
            else:
                try:
                    checksum = directional_check(i, x, loc)
                    if checksum == "#":
                        occupied_counter += 1
                    elif checksum == "L":
                        vacant_counter = vacant_counter + 1
                    else:
                        continue
                except:
                    continue
    if seat == "#" and occupied_counter >= 5:
        return((loc, "L"))
    elif seat == "L" and occupied_counter == 0:
        return((loc, "#"))
    else:
        same_counter += 1
        return((loc, seat))

def directional_check(dirx, diry, startloc):
    global puzzle
    locx = startloc[1]
    locy = startloc[0]
    i = 0
    while i != 1: 
        try:
            if puzzle[((locy + diry), (locx + dirx))] == "#":
                return("#")
            elif puzzle[((locy + diry), (locx + dirx))] == "L":
                return("L")
            else:
                locx = locx + dirx
                locy = locy + diry
        except:
            i = 1
            return(".")


def main_loop(content):
    global main_counter   
    global same_counter
    global puzzle
    new_puzzle = {}
    for i, x in content.items():
        new_seat = seat_check(i, x)[1]
        if new_seat == "#":
            main_counter += 1
        if new_seat != x:
            new_puzzle[i] = new_seat
        elif new_seat == x:
            new_puzzle[i] = x
        else:
            return(print("There is a slimey bug in the seat_check code!"))
    if same_counter == len(content.keys()):
        return(print(f"Loop finished with {main_counter} occupied seats!"))
    elif same_counter < len(content.keys()):
        main_counter = 0
        same_counter = 0
        puzzle = new_puzzle
        return(main_loop(puzzle))
    elif same_counter > len(content.keys()):
        return(print(f"There is a slimey bug in the code! too many same values in 1 loop! {same_counter} > {len(content.keys())}"))
    else:
        return(print("There is a slimey bug in the code! unknown error!"))


main_loop(puzzle)
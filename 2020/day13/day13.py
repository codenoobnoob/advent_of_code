from datetime import datetime as dt
my_file = open("input.txt")
puzzle = my_file.readlines()
departure = int(puzzle[0])
buslist = puzzle[1].split(",")
buslist = [int(i) if i != "x" else 1 for i in buslist]
buslist_enum = list(enumerate(buslist))
buslist_enum.sort(key = lambda x: x[1])
biggest_num = buslist_enum[-1]

def part1(buslist, departure):
    wait_list = []
    for indx, i in enumerate(buslist):
        x = (int((departure / i)+1)*i) - departure
        wait_list.append(tuple((indx, x)))
    wait_list.sort(key = lambda x: x[1])
    print(wait_list)
    result = buslist[wait_list[0][0]] * wait_list[0][1]
    print(buslist[wait_list[0][0]],wait_list[0][1])
    return(result)


def check_next(indx, target_index, target_value, buslist):
    if indx + target_index == len(buslist):
        return(True)
    if buslist[target_index + indx] == 1:
        return(check_next(indx+1, target_index, target_value, buslist))
    elif (target_value + indx) % buslist[target_index + indx] == 0:
        return(check_next(indx+1, target_index, target_value, buslist))
    else:
        return(False)

def main_loop(buslist, biggest_num, add_try):
    global dt
    for i in range(add_try, add_try+1000000000):
        x = i * biggest_num[1]
        if check_next(-(biggest_num[0]), biggest_num[0], x, buslist):
            return(x-biggest_num[0])
        else:
            pass
    print(f"loop ended with {(add_try+1000000000)*biggest_num[1]} as the highest number at {dt.now()}")
    return(main_loop(buslist, biggest_num, add_try+1000000000))

print(main_loop(buslist, biggest_num, int(100000000000000 / biggest_num[1])))
 

    
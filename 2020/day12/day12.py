import math
my_file = open("input.txt")
puzzle = my_file.readlines()
cordinates = [tuple((i[0], int(i[1:]))) for i in puzzle]
global ship_possition
global ship_direction
global ship_course
ship_possition = (0, 0)
ship_direction = 90
ship_course = "E"
way_pointer = (10, 1)

#function checks if degrees are less than zero and adjusts or more than or equal to 360 and adjusts
def degree_check(degrees):
    if degrees < 0:
        return(degree_check(degrees + 360))
    elif degrees >= 360:
        return(degrees % 360)
    else:
        return(degrees)
# function takes in L or R and the degrees and return noting. ship_course is set "N", "E", "S" or "W"
def turn_ship(direction, degrees):
    global ship_direction
    global ship_course
    if direction == "L":
        new_direction = degree_check(ship_direction - degrees)
    elif direction == "R":
        new_direction = degree_check(ship_direction + degrees)
    else:
        return(print("Fault in ship direction calculation"))
    ship_direction = new_direction
    if degrees in [0, 90, 180, 270]:
        for i, x in [(0, "N"), (90, "E"), (180, "S"), (270, "W")]:
            if new_direction == i:
                ship_course = x
                return()
    else:
        return(print("turn_ship function fault: Degrees not devidable by 90!"))

#funtion moves ship to next position
def move_ship(direction, steps):
    global ship_possition
    if direction == "N":
        ship_possition = (ship_possition[0], ship_possition[1] + steps)
    elif direction == "E":
        ship_possition = (ship_possition[0] + steps, ship_possition[1])
    elif direction == "S":
        ship_possition = (ship_possition[0], ship_possition[1] - steps)
    elif direction == "W":
        ship_possition = (ship_possition[0] - steps, ship_possition[1])
    else:
        return(print("there is a problem in the move function."))
    return()

#funtion loops through the instructions
def main_loop(instructions):
    for i, x in instructions:
        if i in ["N", "E", "S", "W"]:
            move_ship(i, x)
        elif i == "F":
            move_ship(ship_course, x)
        elif i in ["R", "L"]:
            turn_ship(i, x)
        else:
            return(print("Main loop: instruction does not fit the criteria!"))
    return(print(f"instructions ended with position {ship_possition}"))

#part 1 solution:
#main_loop(cordinates)
#print(abs(ship_possition[0]) + abs(ship_possition[1]))

# part 2 starts here:

def main_loop2(instructions):
    global way_pointer
    for i, x in instructions:
        if i in ["N", "E", "S", "W"]:
            move_waypointer(i, x)
        elif i == "F":
            move_ship2(way_pointer, x)
        elif i in ["R", "L"]:
            shift_waypointer(i, x)
        else:
            return(print("Main loop: instruction does not fit the criteria!"))
    return(print(f"instructions ended with position {ship_possition}"))

def move_ship2(way_pointer, steps):
    global ship_possition
    ship_possition = (ship_possition[0] + (way_pointer[0] * steps), ship_possition[1] + (way_pointer[1] * steps))

def move_waypointer(direction, steps):
    global way_pointer
    if direction == "N":
        way_pointer = (way_pointer[0], way_pointer[1] + steps)
    elif direction == "E":
        way_pointer = (way_pointer[0] + steps, way_pointer[1])
    elif direction == "S":
        way_pointer = (way_pointer[0], way_pointer[1] - steps)
    elif direction == "W":
        way_pointer = (way_pointer[0] - steps, way_pointer[1])
    else:
        return(print("there is a problem in the move function."))
    return()

def way_pointer_degrees(way_pointer):
    if way_pointer[0] == 0 and way_pointer[1] != 0:
        degree = 90.0 * (way_pointer[1]/abs(way_pointer[1]))
        return(degree, abs(way_pointer[1]))
    elif way_pointer[1] == 0 and way_pointer[0] > 0:
        degree = 0.0
        return(degree, abs(way_pointer[0]))
    elif way_pointer[1] == 0 and way_pointer[0] < 0:
        degree = 180.0
        return(degree, abs(way_pointer[0]))
    elif way_pointer[1] == 0 and way_pointer[0] == 0:
        return(0.0, 0)
    else:
        hypotenusa = math.sqrt(way_pointer[0]**2 + way_pointer[1]**2)
        degree = math.degrees(math.atan(way_pointer[1]/way_pointer[0]))
        if way_pointer[0] < 0:
            degree = degree + 180 
        else:
            pass
        if way_pointer == (round(hypotenusa * math.cos(math.radians(degree))), round(hypotenusa * math.sin(math.radians(degree)))):
            return(degree, hypotenusa)
        else:
            return(print("There is a problem with the degree calculation"))

        


def shift_waypointer(direction, degrees):
    global way_pointer
    degrees_hypotenusa = way_pointer_degrees(way_pointer)
    way_pointer_deg = degrees_hypotenusa[0]
    hypotenusa =degrees_hypotenusa[1]
    if direction == "L":
        new_degree = way_pointer_deg + degrees
    elif direction == "R":
        new_degree = way_pointer_deg - degrees
    else:
        return(print("Fault in ship direction calculation"))
    way_pointer = (round(hypotenusa * math.cos(math.radians(new_degree))), round(hypotenusa * math.sin(math.radians(new_degree))))
    return()

main_loop2(cordinates)
print(abs(ship_possition[0]) + abs(ship_possition[1]))
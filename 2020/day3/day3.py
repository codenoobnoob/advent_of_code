testText = [".........#.#.#.........#.#.....", "...#......#...#.....#.....#...."]

file = open("input.txt").read()
text = file.split('\n')

lines = len(text)
chars = len(text[0])
postitions = 30

def test(inputfile, character, right, start, skip):
#    ycor = []
    result = 0
    planeposx = start[0]
    for i in inputfile[skip::start[1]]:
        planeposx = planeposx + right
        for (x, letter) in enumerate(i):
            if letter == character:
                tree = x
                if planeposx > postitions:
                    if tree == (planeposx % chars):
                        result = result + 1    
                    else:
                        pass
                elif planeposx <= postitions:
                    if tree == planeposx:
                        result = result + 1
                    else:
                        pass
                else:
                    pass
            else:
                pass
    return(result)

#        if len(i) < planeposx:
#            flightmap.append(i * (planeposx//len(i) + 1))
#       elif len(i) > planeposx:
#           flightmap.append(i)

#        for (x, letter) in enumerate(inputfile):
#            if letter == character:
#                ycor.append(x)
#                xcor = xcor + 1

first = (test(text, "#", 1, (0, 1), 1))
second = (test(text, "#", 3, (0, 1), 1))
third = (test(text, "#", 5, (0, 1), 1)) 
fourth = (test(text, "#", 7, (0, 1), 1)) 
fifth = (test(text, "#", 1, (0, 2), 2))
#win = (test(text, "#", 3, [0, 1]))
print(first*second*third*fourth*fifth)
file = open("Cred.txt").read()
numlist = file.split('\n')

for x in numlist:
    for i in numlist:
        for f in numlist:
            if int(x) + int(i) + int(f) == 2020:
                print(x, i, f)
                response = (int(x) * int(i) * int(f))
            else:
                pass

print(response)

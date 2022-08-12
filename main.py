from pyraminx import Pyraminx

current = []
moves = {
    0: "U ",
    1: "R ",
    2: "L ",
    3: "B ",
    4: "U' ",
    5: "R' ",
    6: "L' ",
    7: "B' "
}


def solve(string, done, upper):
    if done != upper:
        if done == 0:
            for j in range(0, 8):
                g = Pyraminx(string)
                g.move(j)
                current.append(j)
                solve(g.stickers, done + 1, upper)
                current.pop()
        else:
            for j in range(0, 8):
                if j % 4 == current[-1] % 4:
                    continue
                g = Pyraminx(string)
                g.move(j)
                current.append(j)
                solve(g.stickers, done + 1, upper)
                current.pop()
    else:
        if Pyraminx(string).isSolved():
            s = ""
            for m in current:
                s += moves[m]
            s = s[:-1]
            print(s)
            exit(0)


cubestring = input("Enter your pyraminx sticker colors: ")
cubestring = [k for k in cubestring.lower()]
for i in range(1, 12):
    solve(cubestring, 0, i)
    print("Completed all solutions of length " + str(i) + (" moves." if i > 1 else " move."))

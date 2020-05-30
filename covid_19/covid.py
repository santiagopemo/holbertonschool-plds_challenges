#!/usr/bin/python3
def print_matrix(matrix=[], closeness = 0):
    print(len(matrix)*"+---", end="")
    print("+")
    for row in matrix:
        for col in row:
            if col == 1:
                text = "\u001b[31m{}\033[0m".format(col)
            if col == 0:
                text = ' '
            if col == 'X':
                text = "\u001b[34m{}\033[0m".format(col)
            if col == 'A':
                text = "\u001b[32m{}\033[0m".format(col)
            print("| {} ".format(text), end="")
        print("|")
        print(len(matrix)*"+---", end="")
        print("+")
    # print("0: Empty    \u001b[31m1\033[0m: Person\n\u001b[34mX\033[0m: You      \u001b[32mP\033[0m: Posible")
    print("\u001b[31m1\033[0m: Person    \u001b[34mX\033[0m: You      \n\u001b[32mA\033[0m: Allowed   Closeness:", closeness)

def make_matrix(size, persons):
    import random
    matrix = []
    for i in range(size):
        row = []
        for j in range (size):
            # row.append(int(random.randint(0, size)/size))
            # row.append(int(random.randint(0, 1)/1))
            row.append(0)
        matrix.append(row)
    if persons > size:
        persons += 1
    for i in range(persons):        
        x = int(random.randint(0, size - 1))
        y = int(random.randint(0, size - 1))
        if matrix[x][y]:
            i -= 1
        else:
            matrix[x][y] = 1
    return matrix


def eval_point(x, y, closeness, matrix, size):
    c = closeness + 1
    for i in range(c):
        d = 0 if closeness == 0 else 1
        if matrix[x][(y - i) if (y - i) >= 0 else 0]                \
            or matrix[x][(y + i) if (y + i) < size else size - 1]   \
            or matrix[(x + i) if (x + i) < size else size - 1][y]   \
            or matrix[(x - i) if (x - i) >= 0 else 0][y]            \
            or matrix[(x - d) if (x - d) >= 0 else 0][
                (y - d) if (y - d) >= 0 else 0]                     \
            or matrix[(x + d) if (x + d) < size else (size - 1)][
                (y + d) if (y + d) < size else (size - 1)]          \
            or matrix[(x - d) if (x - d) >= 0 else 0][
                (y + d) if (y + d) < size else (size - 1)]          \
            or matrix[(x + d) if (x + d) < size else (size - 1)][
                (y - d) if (y - d) >= 0 else 0]:
            # print("Punto Invalido")
            return False
    else:
        # print("Punto Valido")
        return True


def move(origin, dest, matrix):
    
    if origin['x'] > dest['x']:
        #arriba
        o = origin['x']
        d = dest['x']
        fixed = origin['y']
        w_fixed = 'col'
        step = -1
    elif origin['x'] < dest['x']:
        #abajo
        o = origin['x']
        d = dest['x']
        fixed = origin['y']
        w_fixed = 'col'
        step = 1
    elif origin['y'] > dest['y']:
        #izquierda
        o = origin['y']
        d = dest['y']
        fixed = origin['x']
        w_fixed = 'row'
        step = -1
    elif origin['y'] < dest['y']:
        #derecha
        o = origin['y']
        d = dest['y']
        fixed = origin['x']
        w_fixed = 'row'
        step = 1
    elif  origin['x'] == dest['x'] and origin['y'] == dest['y']:
        o = origin['x']
        d = dest['x']
        fixed = origin['y']
        w_fixed = 'row'
        step = 1
    for i in range(o, d, step):
        if w_fixed == 'col':
            if matrix[i][fixed]:
                return False
        else:
            if matrix[fixed][i]:                
                return False
    else:
        return True


def search(origin, closeness, matrix, size):
    x = origin['x']
    y = origin['y']
    evalp = False
    can_move = False
    new_matrix = matrix.copy()
    up = []
    down = []
    left = []
    rigth = []
    tup = ()
    #up
    for r in range(x - 1, -1, -1):
        if matrix[r][y]:
            break
        evalp = eval_point(r, y, closeness, matrix, size)
        tup = (evalp, r, y)
        up.append(tup)
    tup = ()
    #down
    for r in range(x + 1, size):
        if matrix[r][y]:
            break
        evalp = eval_point(r, y, closeness, matrix, size)
        tup = (evalp, r, y)
        down.append(tup)
    tup = ()
    #left
    for r in range(y - 1, -1, -1):
        if matrix[x][r]:
            break
        evalp = eval_point(x, r, closeness, matrix, size)
        tup = (evalp, x, r)
        left.append(tup)
    tup = ()
    #rigth
    for r in range(y + 1, size):
        if matrix[x][r]:
            break
        evalp = eval_point(x, r, closeness, matrix, size)
        tup = (evalp, x, r)
        rigth.append(tup)
    dirs = (up, down, left, rigth)
    #eval rutes    
    for d in dirs:
        if d and len(d) != 0:
            for i in d:
                if i[0]:
                    can_move = True
                    new_matrix[i[1]][i[2]] = 'A'
    if can_move:
        print("\n\u001b[33mYou can't move there!, these \nare the allowed positions: \033[0m")
        new_matrix[x][y] = 'X'
        print_matrix(new_matrix, closeness)
        new_matrix[x][y] = 0
        for d in dirs:
            if d and len(d) != 0:
                for i in d:
                    if i[0]:
                        # print("({},{}) ".format(i[1],i[2]))
                        new_matrix[i[1]][i[2]] = 0
    else:
        print("\n", "\u001b[31mYou can't move anywhere!\033[0m")


def main():
    from sys import argv
    size = 6
    matrix = [
        [1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1]
    ]
    closeness = 2
    print("\n ---- WELCOME ---- \n")
    while 1:
        option = input("\n What do yout want to do?\n1: start      2: new matrix\n3: closeness  4: exit\n>> ")
        if option == '2':
            size = int(input("\nEnter matrix size \n>> "))
            # persons = int(input("Enter number of persons \n>> "))
            persons = size
            if size < 2:
                print("\n\u001b[33m",argv[0],": Size can't be less than 2\033[0m")
                continue
            matrix = make_matrix(size, persons)
            print("\nDone! new matrix of size {:d} created\n".format(size))
            continue
        if option == '3':
            closeness = abs(int(input("Enter Closeness \n>> ")))
            print("\nDone! closeness {:d} set!\n".format(closeness))
            continue
        if option != '1' and option != '2' and option != '3':
            break
        
        print_matrix(matrix, closeness)
        # closeness = abs(int(input("Enter Closeness: ")))
        x_origin, y_origin = input("Where are you? x y \n>> ").split()
        x_origin = int(x_origin)
        y_origin = int(y_origin)
        # x_origin = int(input("Enter x position: "))
        # y_origin = int(input("Enter y position: "))
        if 0 > x_origin or x_origin >= size or 0 > y_origin or y_origin >= size:
            print("\n\u001b[33m", argv[0],": Wrong coordinates!\033[0m")
            continue
        if matrix[x_origin][y_origin]:
            print("\n\u001b[33m", argv[0], ": Yo can not start at this position\033[0m")
            continue
        else:
            matrix[x_origin][y_origin] = 'X'
            print_matrix(matrix, closeness)
        matrix[x_origin][y_origin] = 0

        x_dest, y_dest = input("Where do you want to go? x y \n>> ").split()
        x_dest = int(x_dest)
        y_dest = int(y_dest)
        if 0 > x_dest or x_dest >= size or 0 > y_dest or y_dest >= size or (x_dest != x_origin and y_dest != y_origin):
            print("\n\u001b[33m", argv[0],": Wrong movement!\033[0m")
            continue
        # x_dest = 0
        # y_dest = 2
        origin = {'x': x_origin, 'y': y_origin}
        dest = {'x': x_dest, 'y': y_dest}
        if move(origin, dest, matrix):
            if eval_point(x_dest, y_dest, closeness, matrix, size):
                matrix[x_origin][y_origin] = 0
                matrix[x_dest][y_dest] = 'X'
                print_matrix(matrix, closeness)
                matrix[x_dest][y_dest] = 0
                continue
        # print("Can not take this way")       
        search(origin, closeness, matrix, size)
    print("\n -- BYE ;) -- \n")

main()

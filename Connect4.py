# Connect 4
import random
print("\nPlayer 1: " + u'\u2B24' + "  Player 2: " + u'\u2B25')

matrice = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [
    " ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]


def drawBoard(matrice):
    for i in range(6):
        print("--|---|---|---|---|---|---|")
        for j in range(7):
            print(matrice[i][j] + " | ", end="")
        print("")
    print("--|---|---|---|---|---|---|")


# daca pe prima linie si pe coloana introdusa sunt piese puse pana sus
def insertPiece(row, col, player, matrice):
    # e full                     e deja o piesa
    if matrice[0][col] != " " or matrice[row][col] != " ":
        print("The column is full/ there already is a piece at that location")
        return -1
    else:
        if player == 1:
            # parcurg in cazul in care pe ultima linie si pe coloana col am deja ceva introdus
            for i in range(5):
                if(matrice[i][col] == " " and matrice[i+1][col] != " "):
                    matrice[i][col] = u'\u2B24'
                    return 1
            # daca nu este pe ultima linie nimic
            matrice[5][col] = u'\u2B24'
            return 1
        else:
            for i in range(5):
                if(matrice[i][col] == " " and matrice[i+1][col] != " "):
                    matrice[i][col] = u'\u2B25'
                    return 2
            matrice[5][col] = u'\u2B25'
            return 2


def checkComplete(matrice):
    ok = 0
    for i in range(6):
        for j in range(7):
            if matrice[i][j] == " ":
                ok = 1
    if ok == 0:
        return 0
    else:
        return 1


def checkWinnerLeftTop(player, matrice):
    ok1 = 0
    ok2 = 0
    ok3 = 0
    for i in range(3):
        for j in range(4):
            ok1 = 0
            ok2 = 0
            ok3 = 0
            if(matrice[i][j] != " "):
                # linie orizontala
                for k in range(j+1, j+4, 1):
                    if matrice[i][k] != matrice[i][j]:
                        ok1 = 1
                        break
                # linie verticala
                for k in range(i+1, i+4, 1):
                    if matrice[k][j] != matrice[i][j]:
                        ok2 = 1
                        break
                # diagonala
                for k in range(1, 4, 1):
                    if matrice[i+k][j+k] != matrice[i][j]:
                        ok3 = 1
                        break
            else:
                break
            if(ok1 == 0 or ok2 == 0 or ok3 == 0):
                print("Player " + str(player) + " won")
                return 0
    return 1


def chechWinnerRightTop(player, matrice):
    ok1 = 0
    ok2 = 0
    ok3 = 0
    for i in range(3):
        for j in range(6, 3, -1):
            ok1 = 0
            ok2 = 0
            ok3 = 0
            if(matrice[i][j] != " "):
                # linie orizontala
                for k in range(j-1, j-4, -1):
                    if matrice[i][k] != matrice[i][j]:
                        ok1 = 1
                        break
                # linie verticala
                for k in range(i+1, i+4, 1):
                    if matrice[k][j] != matrice[i][j]:
                        ok2 = 1
                        break
                # diagonala
                for k in range(1, 4, 1):
                    if matrice[i+k][j-k] != matrice[i][j]:
                        ok3 = 1
                        break
            else:
                break
            if(ok1 == 0 or ok2 == 0 or ok3 == 0):
                print("Player " + str(player) + " won")
                return 0
    return 1


def checkWinnerLeftBottom(player, matrice):
    ok1 = 0
    ok2 = 0
    ok3 = 0
    for i in range(5, 1, -1):
        for j in range(4):
            ok1 = 0
            ok2 = 0
            ok3 = 0
            if(matrice[i][j] != " "):
                # linie orizontala
                for k in range(j+1, j+4, 1):
                    if matrice[i][k] != matrice[i][j]:
                        ok1 = 1
                        break
                # linie verticala
                for k in range(i-1, i-4, -1):
                    if matrice[k][j] != matrice[i][j]:
                        ok2 = 1
                        break
                # diagonala
                for k in range(1, 4, 1):
                    if matrice[i-k][j+k] != matrice[i][j]:
                        ok3 = 1
                        break
            else:
                break
            if(ok1 == 0 or ok2 == 0 or ok3 == 0):
                print("Player " + str(player) + " won")
                return 0
    return 1


def checkWinnerRightBottom(player, matrice):
    ok1 = 0
    ok2 = 0
    ok3 = 0
    for i in range(5, 1, -1):
        for j in range(6, 3, -1):
            ok1 = 0
            ok2 = 0
            ok3 = 0
            if(matrice[i][j] != " "):
                # linie orizontala
                for k in range(j-1, j-4, -1):
                    if matrice[i][k] != matrice[i][j]:
                        ok1 = 1
                        break
                # linie verticala
                for k in range(i-1, i-4, -1):
                    if matrice[k][j] != matrice[i][j]:
                        ok2 = 1
                        break
                # diagonala
                for k in range(1, 4, 1):
                    if matrice[i-k][j-k] != matrice[i][j]:
                        ok3 = 1
                        break
            else:
                break
            if(ok1 == 0 or ok2 == 0 or ok3 == 0):
                print("Player " + str(player) + " won")
                return 0
    return 1


drawBoard(matrice)
player = random.randint(1, 2)
while True:
    print("It's player's " + str(player) + " turn")
    row = int(input("The row you want to insert: "))
    col = int(input("The column you want to insert: "))
    insertPiece(row, col, player, matrice)
    drawBoard(matrice)
    if checkComplete(matrice) == 0:
        print("No one won")
        break
    if checkWinnerLeftBottom(player, matrice) == 0 or checkWinnerRightBottom(player, matrice) == 0 or checkWinnerLeftTop(player, matrice) == 0 or chechWinnerRightTop(player, matrice) == 0:
        break
    if(player == 1):
        player = 2
    else:
        player = 1

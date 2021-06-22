# Connect-4
Connect 4 in python

Acesta este jocul Connect 4. Atasez un link cu regulile jocului: https://www.youtube.com/watch?v=utXzIFEVPjA

Explicare cod:

Tabla pentru acest joc este sub forma unei matrici de 6x7 (lista ce are 6 liste si 7 elemente per lista)

1) Metoda drawBoard(matrice):

In aceasta metoda se face afisarea tablii.

2) Metoda insertPiece(row, col, player, matrice):

In aceasta metoda se insereaza piesa la pozitia [row][col]. 
Prima oara se verifica daca pe prima linie si coloana col este deja o piesa (adica a fost umpluta acea coloana pana sus) sau daca pe pozitia [row][col] este deja o piesa inserata. Daca una dintre aceste conditii este adevarata atunci se returneaza -1.
Daca nu este adevarata nicio conditie din cele 2 prezentate anterior, se intra pe ramura de else unde se verifica ce fel de player este.
Dupa acestea, se parcurg liniile matricii (cu contorul i) si se verifica daca la pozitia [i][col] este liber, iar pe urmatoarea linie si aceeasi coloana este ocupat (e ca si cum ar cadea piesa). Daca asa este se adauga cerc pentru player 1 si romb pentru player 2 dupa care se returneaza o valoarea (1 pentru player 1 si 2 pentru player 2)
Daca nu s-a facut returnarea atunci inseamna ca pe acea coloana nu este nimic introdus rezultand introducerea pe ultima linie si coloana col

3) Metoda checkComplete(matrice):

In aceasta metoda se verifica daca s-au introdus pe toate pozitiile o piesa.
Daca se gaseste un spatiu liber atunci variabila ok se face 1
La final se verifica daca variabila ok este 1 (daca se mai pot introduce piese) sau daca este 0 (atunci tabla e full)

4) Metodele checkWinnerLeftTop(player, matrice), chechWinnerRightTop(player, matrice), checkWinnerLeftBottom(player, matrice), checkWinnerRightBottom(player, matrice):

In aceste 4 metode se verifica conditiile de castigare (daca sunt 4 piese de acelasi fel pe linia orizontala, verticala sau diagonala).
Se pleaca de la pozitiile sugestive numelor metodelor si se parcurg cu 3 bucle for liniile orizontale, verticale si diagonalele pentru verificarea conditiei de castig. Cele 3 contoare (ok1, ok2, ok3) raman pe 0 daca conditia este indeplinita (se verifica la finalul fiecarei metode daca una dintre ele este 0, iar in caz afirmativ se returneaza 0 si se afiseaza care player a castigat). Daca conditia nu este indeplinita atunci se returneaza 0

De la linia 187:
Se deseneaza tabla de joc
Se genereaza random un jucator (numar generat in intervalul [1, 2])
In bucla infinita:
- Se citesc de la tastatura linia si coloana unde se doreste sa fie introdusa urmatoarea piesa
- Se apeleaza metoda de inserare a unei piese
- Se redeseneaza tabla de joc
- Se verifica daca tabla este plina (daca da atunci se afiseaza mesajul "No one won" si se da break)
- Se verifica cele 4 metode pentru conditia de castig (daca una dintre ele returneaza 0 atunci se da break)
- Se schimba numarul player-ului

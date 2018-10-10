koteł = "=^_^="

ilośćKotełów = input("Ile chcesz kotów :O : ")
try:
    ilośćKotełów = int( ilośćKotełów )
except ValeError as owcaError:
    print( "Nie wpisałeś liczby" )
    ilośćKotełów = 7

#zadanie domowe
"""

napisać program, który generuje dowolną piramidę z kotełów.
Założenia:
Jeśli użytkownik wpisze liczę ujemną, to powinno go okrzyczeć i wypisać do konsoli =^!^=
Przykład:
dla ilośćKotełów = 3

Wynik:
"=^_^="
"=^_^=""=^_^="
Hint: Pętle i if-y
"""
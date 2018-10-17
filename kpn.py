import random

def rps () :
    wybor_komputera = random.randit(1,3)
    if wybor_komputera == 1:
        wybor_komputera_kamien()
    elif wybor_komputera == 2:
        wybor_komputera_papier()
    else: 
        wybor_komputera_nozyce()

def wybor_komputera_kamien():
    wybor_gracza = raw_input("1 for Kamien, 2 for Papier, 3 for Nozyce ")
    if wybor_gracza == "1":
        print "Remis. I ty i komputer wybraliście kamień."
        sproboj_ponownie()
    if wybor_gracza == "2":
        print "Wygrałeś. Wybrałeś papier, a komputer kamień."
        sproboj_ponownie()
    if wybor_gracza == "3":
        print "Przegrałeś. Wybrałeś nożyce, a komputer kamień."
        sproboj_ponownie()
    else:
        print "Spróbuj ponownie"
        wybor_komputera_kamien()
#tutaj przerwa
def wybor_komputera_papier():
    wybor_gracza = raw_input("1 for Kamien, 2 for Papier, 3 for Nozyce ")
    if wybor_gracza == "1":
        print "Przegrałeś. Wybrałeś kamień, a komputer papier."
        sproboj_ponownie()
    if wybor_gracza == "2":
        print "Remis. Ty i komputer wybraliście papier."
        sproboj_ponownie()
    if wybor_gracza == "3":
        print "Wygrałeś. Wybrałeś nożyce, a komputer papier."
        sproboj_ponownie()
    else:
        print "Spróbuj ponownie"
        wybor_komputera_papier()
#tutaj przerwa
def wybor_komputera_nozyce():
    wybor_gracza = raw_input("1 for Kamien, 2 for Papier, 3 for Nozyce ")
    if wybor_gracza == "1":
        print "Wygrałeś. Wybrałeś kamień, a komputer nożyce."
        sproboj_ponownie()
    if wybor_gracza == "2":
        print "Przegrałeś. Wybrałeś papier, a komputer nożyce."
        sproboj_ponownie()
    if wybor_gracza == "3":
        print "Remis. Wybrałeś nożyce, tak jak komputer."
        sproboj_ponownie()
    else:
        print "Spróbuj ponownie"
        wybor_komputera_nozyce()

def sproboj_ponownie():
    wybor = raw_input("Czy chciałbyś zagrać ponownie?  t/n")
    if wybor == "t" or wybor == "tak" or choice == "T":
        rps()
    elif choice == "n":
        print "Dziękuję za grę"
        quit()
    else:
        print "Spróbój ponownie"
        sproboj_ponownie()

rps()
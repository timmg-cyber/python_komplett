
##1 module test w/o main

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False


def contains_sequence(text, sequence):
    if sequence in text:
        return True
    else:
        return False


##1 Test in interaktiver Python-Shell
#is_even(2)
#is_even(7)
#contains_sequence("Hallo mein Name ist Timm", "Timm")
#contains_sequence("Hallo mein Name ist Timm", "Tom")

#2 Tests in Modul schreiben
#if is_even(2) == True and is_even(7) == False \
#and contains_sequence("Hallo mein Name ist Timm","Timm") == True \
#and contains_sequence("Hallo mein Name ist Timm","Tom") == False:
#    print("Test für my_module ist erfolgreich")
#else:
#   print("Fehler beim Testen von my_module")

#3 Fehler in Tests einbauen

##4 Modul versuchen zu importieren

##5 Main-Methode --> kein automatisches ausführen
if __name__ == "__main__":
    #hier werden die Modultests reingeschrieben, da dies nur dann ausgeführt wird wenn das Modul selbst ausgeführt wird
    if is_even(2) == True and is_even(7) == False \
            and contains_sequence("Hallo mein Name ist Timm", "Timm") == True \
            and contains_sequence("Hallo mein Name ist Timm", "Tom") == False:
        print("Test für my_module ist erfolgreich")
    else:
        print("Fehler beim Testen von my_module")
# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.

#1
def print_name(vorname:str , nachname:str):   ##Keyword-Arguments
    print(f"Die Person heißt {vorname} {nachname}")

#2
def print_name2(**kwargs): #beliebige Anzahl von keyword args
    print(f"Die Person heißt {kwargs['vorname']} {kwargs['nachname']}")

#3
def print_name3(*args): #Beliebige Anzahl positional args
    print(f"Die Person heißt {args[0]} {args[1]}")

#4
def print_name4(vorname,nachname,**kwargs):
    print(f"Die Person heißt {vorname} {nachname} \n weitere Argumente: {kwargs}")

#5
def return_höchste_zahl(zahlen:list):
    hoechste_zahl = 0
    for zahl in zahlen:
        if zahl > hoechste_zahl:
            hoechste_zahl = zahl
    return hoechste_zahl

#6
def void_function():
    pass        ##wirft keinen Fehler

#7 Rekursion
def tri_recursion(k):  #In Debug Mode öffnen
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ## Basic Syntax
    #print_hi('PyCharm')
    #print_name(vorname=1,nachname=2)
    #print_name(vorname="Timm", nachname="Gieger")
    #print_name2(vorname = "Timm", nachname= "Gieger", zweitname=None) #nicht jeder Parameter muss gecallt werden
    #print_name3("Timm","Gieger")
    #print_name4(vorname="Timm",nachname="Gieger",weiteres_argument = "argument")

    ##return statements
    #number = return_höchste_zahl([5,10,20,15,35,1,11,27])
    #print(number)

    ##void function
    #void_function()

    print("\n\nRecursion Example Results")
    tri_recursion(6)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

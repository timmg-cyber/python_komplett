import logging
# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def except_function(zahl):
    try:
        zahl+= 5
        print(zahl)
    except:
        print("Mathematische Operation fehlgeschlagen")
    pass

def except_function2(zahl):
    try:
        print(a)
    except NameError:
        print("Das ist wohl ein Name Error")
    except:
        print("oder doch nicht?")

    pass

def except_function3(zahl):
    try:
        zahl = int(zahl)
        zahl+=zahl
        print(zahl)
    except:
        print("Something went wrong")
    else:
        print("Nothing went wrong")

def except_function4(zahl):
    try:
        zahl = int(zahl)
        zahl += zahl
        print(zahl)
    except:
        print("Something went wrong")
    finally:
        print("This blocks runs whether there is an error or not")


def except_function5(zahl):
    try:
        if isinstance(zahl,int):
            zahl += 3
            print(zahl)
        else:
            raise TypeError("Only Integers are allowed")
    except:
        logging.exception("Got exception on main handler")
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #x = input("Zahl:")

    #except_function(x)

    #except_function2(x) ## Name Error

    #except_function3(x) ## einmal mit 10 und zehn

    #except_function4(x)

    x = "10"
    except_function5(x)## raise Exception





# See PyCharm help at https://www.jetbrains.com/help/pycharm/

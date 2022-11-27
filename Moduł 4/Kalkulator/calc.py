import sys
import logging
logging.basicConfig(level=logging.INFO)

#dodawanie
def add(x, y): 
    return x + y
#odejmowanie
def subtract(x, y):
    return x - y
#mnożenie
def multiply(x, y):
    return x * y
#dzielenie
def divide(x, y):
    return x / y

if __name__ == '__main__':
    choise = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    
    if choise in ('1', '2', '3', '4'):
        val1 = float(input("Podaj składnik 1: "))
        val2 = float(input("Podaj składnik 2: "))
        
        if choise == '1':
            logging.info("Dodaję %s i %s" % (val1, val2))
            print("Wynik to:", add(val1, val2))
            
        elif choise == '2':
            logging.info("Odejmuję %s od %s" %(val1, val2))
            print("Wynik to: ", subtract(val1, val2))
            
        elif choise == '3':
            logging.info("Mnożę %s przez %s" % (val1, val2))
            print("Wynik to: ", multiply(val1, val2))
            
        elif choise == '4':
            logging.info("Dzielę %s przez %s" % (val1, val2))
            print("Wynik to: ", divide(val1, val2))
            
    else:
        print("Ups, zepsułeś kalkulator :)")

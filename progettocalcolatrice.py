#programma calcolatrice BY RIUGXSS
import time
tool = """
                                                                                \033[1;31m[\033[1;37m!\033[0m\033[1;31m]\033[0mRiugxss
                                                                                \033[1;31m[\033[1;37m!\033[0m\033[1;31m]\033[0mVersion 0.1

"""
print(tool)
import sys
print("\033[1;31m[""\033[1;37m!\033[0m""\033[1;31m]\033[0m","\033[1;37mCalcolatrice\033[0m")
is_vero = True
print("\nBenvenuto! \033[1;37mIo sono riugxss\033[0m spero possa servirti il mio programma!")
ak = """\033[1;31m
>---------------<
>---------------<
\033[0m"""
print(ak)
while is_vero:
    try:
        num1 = int(input("Inserisci il primo numero per il calcolo: "))
        num2 = int(input("Inserisci un secondo numero: "))
        op = input("Scegli l'operatore \033[1;37m(+,-,*,/)\033[0m ")
        if op == "+":
            time.sleep(0.5)
            print(f"Il risultato è \033[1;31m{num1 +num2}\033[0m")
            is_vero = False
        elif op == "-":
            time.sleep(0.5)
            print(f"Il risultato è \033[1;31m{num1-num2}\033[0m")
            is_vero = False
        elif op == "*":
            time.sleep(0.5)
            print(f"Il risultato è \033[1;31m{num1*num2}\033[0m")
            is_vero = False            
        elif op == "/":
            time.sleep(0.5)
            print(f"Il risultato è \033[1;31m{num1 / num2}\033[0m")
            is_vero = False
        else:
            print("\033[1;31m[""\033[1;37m!\033[0m""\033[1;31m]\033[0m","\033[1;37mInserisci un operatore (+, - , * , /) valido.\033[0m")
            #Decorazione
        akk = """\033[1;31m
>---------------<
>---------------<
        \033[0m"""
        is_vero = True
        print(akk)
            # Chiedi all'utente se vuole continuare
        continua = input("Vuoi eseguire un \033[1;31maltro calcolo?\033[0m (si/no): ").strip().lower()
        if continua != "s":
            print("\033[1;37mRiugxss ti ringrazia\033[0m, torna presto caro amico!")
            break
            
    except ZeroDivisionError:
        print("\033[1;31m[""\033[1;37m!\033[0m""\033[1;31m]\033[0m","\033[1;37mNon puoi dividere con il numero 0.\033[0m")
    except ValueError:
        print("\033[1;31m[""\033[1;37m!\033[0m""\033[1;31m]\033[0m","\033[1;37mDevi inserire una Value valida.\033[0m")
    except KeyboardInterrupt:
        print("\n\033[1;31m[""\033[1;37m!\033[0m""\033[1;31m]\033[0m","\033[1;37mL'utente ha cliccato il tasto di uscita (Ctrl+C), uscendo dal programma\033[0m")
        sys.exit()
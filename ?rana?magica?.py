#CODICE FATTO DA RIUGXSS PER IL GIOCO DELLA RANA MAGICA.

import sys
from random import choice
import time
# 1) GREETINGS
print("\033[3;33mBenvenuto giocatore! Questo è il gioco delle monete.\033[0m")

# 2) ISTRUZIONI DI GIOCO
print("")
istruzioni = """\033[1;31mQueste sono le istruzioni di gioco\033[0m: 
Ci sono 8 monete, una delle quali è falsa e pesa di più rispetto alle altre. 
Usa una bilancia per individuare la moneta falsa!
"""
print(istruzioni)
time.sleep(3)
# 3) NOME
nome = input("Inserisci il tuo nome: \n").title()
print(f"{nome}, mmh.. Bel nome!!")
time.sleep(1)
print("\n🎉🎉🎉🎉")
# 4) DIVISIONE DELLE MONETE IN 3 GRUPPI
time.sleep(2)
print("Decidi di dividere le 8 monete in 3 gruppi...")
time.sleep(2)
# Simuliamo la pesatura
# Assumiamo che 'pesogrup1', 'pesogrup2', 'pesogrup3' siano i pesi totali dei tre gruppi
# Poiché si tratta di una simulazione, useremo 'choice' per determinare casualmente la pesantezza

# Dichiarazione dei gruppi
grp1 = "gruppo 1"
grp2 = "gruppo 2"
grp3 = "gruppo 3"

# Uso dei colori (ROSSO)
st = "\033[3;31m"
ts = "\033[0m"

pesogrup1 = choice([1, 1, 2])  # 1 = normale, 2 = falso
pesogrup2 = choice([1, 1, 2])
#pesogrup3 = choice([1, 1, 2])

# Funzione per simulare le pesate
def gruppi():
    pesogrup1 = choice([1, 1, 2])  # 1 = normale, 2 = falso
    pesogrup2 = choice([1, 1, 2])
    #pesogrup3 = choice([1, 1, 2])

    if pesogrup1 == pesogrup2:
        print(f"Il giocatore decide di pesare...")
        time.sleep(2)
        print(f"Il {grp1} e {grp2} sono uguali,{st}la moneta falsa sarà nel {grp3}.{ts}")
        time.sleep(2)
        moneta_falsa = choice(["moneta 1", "moneta 2"])
        print(f"La moneta {st}falsa si trova nel {grp3} ed è la {moneta_falsa}.{ts}\n")
    elif pesogrup1 > pesogrup2:
        print(f"Il giocatore decide di pesare...")
        time.sleep(2)
        print(f"Il {grp1} è più pesante, {st}quindi contiene la moneta falsa.{ts}")
        time.sleep(2)
        moneta_falsa = choice(["moneta 1", "moneta 2", "moneta 3"])
        print(f"La moneta {st}falsa è la {moneta_falsa}.{ts}\n")
    else:
        print(f"Il giocatore decide di pesare...")
        time.sleep(2)
        print(f"Il {grp2} è più pesante, {st}quindi contiene la moneta falsa.{ts}")
        time.sleep(2)
        moneta_falsa = choice(["moneta 1", "moneta 2", "moneta 3"])
        print(f"La moneta falsa è la {moneta_falsa}.\n")

    #CREAZIONE DI UNA FUNZIONA APPOSITA PER RIGIOCARE.
    def rest():
        while True: #uso di un loop per far si che l'input funzioni in modo corretto
            restart = input(f"{nome} Vuoi giocare di nuovo? \033[3;33mclicca Y per rigiocare o Q per uscire.\033[0m \n").lower()
            if restart not in ["y", "q"]:
                continue
            else:
                break
        if restart == "y":
            return gruppi()  
        else:
            sys.exit(f"{nome}, grazie per aver giocato,\033[3m torna presto!\033[0m")
            print("\n🎉🎉🎉🎉")
    rest()
# Inizio del gioco

gruppi()

#COMMENTI FINALI:

#IN QUESTO PROGETTO FATTO DA RIUGXSS C'è UN USO DI: uso di librerie/moduli come sys, random e time.

#random: spiegazione generica genera numeri casuali in base alle nostre esigenze tramite le variabili.
#time: l'uso di time può essere usato con sleep per dare tempo ai codici e farli partire in ordine
#sys = ci dà l'accesso a variabili o funzioni per far si che sia possibile la manipolazione

#uso di print, uso variabili, uso di 2 funzioni per gestire meglio il flusso e le situazioni
#infine uso di while con la sua funzione per far si che il gioco finisca o rinizi a seconda della scelta dell'utente

#SPERO CHE IL GIOCO SIA PIACIUTO.

import sys
from time import sleep

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(0.05)

class Pokemon(object):
    sleep(0.5)
    name = input("De si be trenerče. Kako te zovu?\n")
    def __init__(self, name, alone=True, choice=0):
        self.name = name
        self.alone = alone
        self.choice = choice
        
    @classmethod
    def select(cls):
        sleep(1)
        return cls(
            print(f"Aaa, da be čuo sam za tebe, zovu te {Pokemon.name}. Oćes da si izabereš neko pokemonče?"),
            sleep(1)
        )
    @classmethod
    def answer(cls):
        sleep(1)
        pokemon = False
                
        while True:
            sleep(0.5)
            answer = int(input("1. Моže\n2. Ne bih, stvarno, hvala\n> "))
            if answer == 1 and not pokemon:
                sleep(1)
                pokemon = True
                Select.pitanje()
                break
            elif answer == 2 and not pokemon:
                sleep(1)
                print("Nema brines, aj da gledamo u nebo onda, Laza me samo tolko naučio trenutno.")
                sleep(3)
                nebo = "DEBILE SLEDECI PUT IZABERI NESTO"
                for letter in nebo:
                    print(letter)
                    sleep(0.2)
                pokemon = False
                p1.alone = True
                sleep(1)
                wild()
                break
            else:
                sleep(0.5)
                print('Samo brojevi 1 i 2, zamolite gospodina da Vam pruzi jos jednu sansu.')
                
    @classmethod
    def choice(cls):
        choice = 0
        
    @classmethod
    def alone(cls):
        if p1.alone == False:
            print("Sva sreca imas si pokemonce")
        else:
            sleep(1)
            print("Eee jebaga, voleo bi ti da smo poneli neko pokemonce")
            sleep(3)
            print("Nista bate, ce se gledamo neki drugi put, ispusio si ga...")
            sleep(2)
            print("Hvala sto ste igrali sa nama! o/ ")
            sleep(5)
            quit()        
                
class Room():
    def __init__(self):
        pass

    def enter(self):
        print(Room.wild)
        
def wild():
    sleep(2)
    print("Ukoči se od stajanje, ae malo da se promajemo. Vidis li onaj dzbun? Obicno si tamo sediv pokemoni.")
    sleep(3)
    print("*odlazite do visoke trave i cujete kako nesto suska*")
    sleep(2)
    print("Aha, naletemo na Pikacua. Gle ga pacovce na baterije ahahah.")
    sleep(2)
    Pokemon.alone()
    sleep(1)
    if p1.choice == 1:
        print("Bulb")
    elif p1.choice == 2:
        print("Charm")
    elif p1.choice == 3:
        print("Squir")
      
        
class Select(Room):
    def pitanje():
        sleep(2)
        print("Pa al ae.")
        sleep(2)
        print("Koe bi voleo, imam si neki tamo pored kantu za đubre.")
        sleep(3)
        print("Nisam uzeo da gi bacim nemoj da mi se penješ tu po živci.")
        sleep(2)
        delay_print("Mogu da te ponudim sa: \n1. Bulbasaura\n2. Čarmandera\n3. Skvirtla")
        choice = int(input("\nBiram broj: "))
        sleep(0.5)
        if choice == 1:
            sleep(1)
            print("Dobro, uzeo si ovu biljku mesozderku, pacova ovog sa ove lijane. Lih samo nam Tarzan fali.")
            p1.choice += 1
            p1.alone = False
            sleep(1)
            wild()
            
        elif choice == 2:
            sleep(1)
            print("Aha, izabrao si ovo gusterce sa njega da potpaljujes sporet a?")
            p1.choice += 2
            p1.alone = False
            sleep(1)
            wild()
        elif choice == 3:
            sleep(1)
            print("Lele be lele uzeo si ovu vevericu sto obukla nindza kornjaca odelo smoking, normalan li si?")
            p1.choice += 3
            p1.alone = False
            sleep(1)
            wild()
        else:
            print("A be, 1, 2 ili 3, nemoj da te udarim da se vratis u vreme kad rumenko bio 10 dinara.")
            sleep(1)
            Select.pitanje()
            choice()
    
p1 = Pokemon.select()
p1 = Pokemon.answer()
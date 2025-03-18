import random

a = random.randint(1,6)                                    #1. dice
b = random.randint(1,6)                                    #2. dice
c = random.randint(1,6)                                    #3. dice
d = a+b+c
print("                        -- 🎲NUR HEUTE🎲 --                                 ",d +2 )
print("Das Schätzchenspiel: 3 D6-Würfel in einem Becher. "        #Titel
      "Schätze einfach die Summe der Augen =) viel Glück.")
i = int(0)                                      # Das ist die Bedingung, damit sich das Spiel nicht wiederholt wenn man gewonnen hat(also zu gewinnen ist die Bedingung)

def new_func():
    return 1
while i < 1:                                    #die Schleife wiederholt sich immer wieder auch wenn man die zahl errät!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 v=int(3)
 print(v,"Versuche insgesamt")
 z = int(input("Dein Tipp?:"))                                     #first try
 if z is d:
    print(z,"ist richtig! Du bekommst den Hauptgewinn!! ")
    i += 1
    r: int = int(input("Deine nächste Runde kostet nur einen Euro:"))
    if r is e:
        print("Neuer Versuch, neues Glück!")
    else:
        print("genau 1 Euro bitte")
        r: int = int(input("Hier bezahlen:"))
        if r is e:
            print("vielen Danke für die Bezahlung=)Neuer Versuch, neues Glück!")
            i -= 1
 else:
    print(z,"ist leider falsch, das Ergebnis")
    print("ist übrigens mehr als",a,)
    (v) = v-1
    print(v,"Versuche übrig")
    if z != d:
     z: int = int(input("Dein nächster Tipp?:"))                  #second try
     if z is d:
         print(z, "ist richtig!! Du hast gewonnen! ")
         i += 1
         r: int = int(input("Deine nächste Runde kostet nur einen Euro:"))
         if r is e:
             print("Neuer Versuch, neues Glück!")
         else:
             print("genau 1 Euro bitte")
             r: int = int(input("Hier bezahlen:"))
             if r is e:
                 print("vielen Danke für die Bezahlung=)Neuer Versuch, neues Glück!")
                 i -= 1
     else:
         print(z, "ist nicht korrekt. Schade Banane, knapp daben ist vorbei )=")
         print("das Ergebnis ist ca.:", a + b, )
         (v) = v - 1
         print("nur noch", v, "Versuch übrig.")
         z: int = int(input("Wie lautet dein finaler Tipp?:"))     #third try
         if z is d:
             print(z, "ist die richtige Antwort!! Herzlichen Glückwunsch <3")
             i += 1
             r: int = int(input("Deine nächste Runde kostet nur einen Euro:"))
             if r is e:
                 print("Neuer Versuch, neues Glück!")
             else:
                 print("genau 1 Euro bitte")
                 r: int = int(input("Hier bezahlen:"))
                 if r is e:
                     print("vielen Danke für die Bezahlung=)Neuer Versuch, neues Glück!")
                     i -= 1
         else:
             print(z, "ist es auch nicht...das war deine letzte Chance.")
             print("Es war natürlich", d, "hätte man sich ja auch denken können")
             (v) = v - 1
             print(v, "Versuche übrig, aber nächstes mal schaffst du es bestimmt :3")

             e= int(1)
             r: int = int(input("Deine nächste Runde kostet nur einen Euro:"))

             if r is e:
                 print ("Neuer Versuch, neues Glück!")
             else:
                 print("genau 1 Euro bitte")
                 r: int = int(input("Hier bezahlen:"))
                 if r is e:
                     print("vielen Danke für die Bezahlung=)Neuer Versuch, neues Glück!")




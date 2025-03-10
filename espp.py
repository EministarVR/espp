import sys
import math

variablen = {}

def run_espp_code(code):
    zeilen = code.split("\n")
    
    for zeile in zeilen:
        zeile = zeile.strip()
        
        if not zeile or zeile.startswith("</>"):  
            continue 
        
        if ";" in zeile:
            for teil in zeile.split(";"):
                run_espp_code(teil.strip())
            continue

        if zeile.startswith('ausgabe("') and zeile.endswith('")'):
            inhalt = zeile[len('ausgabe("'):-2]
            print(inhalt)

        elif zeile.startswith("leer: linie"):
            print()
        
        elif zeile.startswith("leer: zeichen"):
            print(" ", end="")

        elif "=" in zeile:
            teile = zeile.split("=")
            var_name = teile[0].strip()
            wert = teile[1].strip()

            try:
                variablen[var_name] = eval(wert, {"math": math}, variablen)
            except:
                variablen[var_name] = wert  
        
        elif zeile.startswith("wenn "):
            teile = zeile[5:].split(" dann ")
            if len(teile) == 2:
                bedingung, aktion = teile
                try:
                    if eval(bedingung, {}, variablen):
                        run_espp_code(aktion)
                except:
                    print("❌ Fehler in der Bedingung!")

        elif " sonst " in zeile:
            teile = zeile.split(" sonst ")
            run_espp_code(teile[1])

        elif zeile.startswith("summe("):
            zahlen = list(map(float, zeile[6:-1].split(",")))
            print(sum(zahlen))

        elif zeile.startswith("produkt("):
            zahlen = list(map(float, zeile[8:-1].split(",")))
            ergebnis = 1
            for zahl in zahlen:
                ergebnis *= zahl
            print(ergebnis)

        elif zeile.startswith("quotient("):
            zahlen = list(map(float, zeile[9:-1].split(",")))
            if zahlen[1] == 0:
                print("❌ Fehler: Division durch 0!")
            else:
                print(zahlen[0] / zahlen[1])

        elif zeile.startswith("modulo("):
            zahlen = list(map(int, zeile[7:-1].split(",")))
            print(zahlen[0] % zahlen[1])

        elif zeile.startswith("sinus("):
            zahl = float(zeile[6:-1])
            print(math.sin(math.radians(zahl)))

        elif zeile.startswith("cosinus("):
            zahl = float(zeile[8:-1])
            print(math.cos(math.radians(zahl)))

        elif zeile.startswith("tangens("):
            zahl = float(zeile[8:-1])
            print(math.tan(math.radians(zahl)))

        elif zeile.startswith("wurzel("):
            zahl = float(zeile[7:-1])
            print(math.sqrt(zahl))

        elif zeile.startswith("potenz("):
            zahlen = list(map(float, zeile[7:-1].split(",")))
            print(math.pow(zahlen[0], zahlen[1]))

        elif zeile.startswith("log("):
            zahl = float(zeile[4:-1])
            print(math.log(zahl))

        elif zeile.startswith("absolut("):
            zahl = float(zeile[8:-1])
            print(abs(zahl))

        elif zeile.startswith("runden("):
            zahlen = list(map(float, zeile[7:-1].split(",")))
            print(round(zahlen[0], int(zahlen[1])))

        elif zeile.startswith("fakultät("):
            zahl = int(zeile[9:-1])
            print(math.factorial(zahl))

        elif zeile.startswith("minimum("):
            zahlen = list(map(float, zeile[8:-1].split(",")))
            print(min(zahlen))

        elif zeile.startswith("maximum("):
            zahlen = list(map(float, zeile[8:-1].split(",")))
            print(max(zahlen))

        elif zeile.startswith("text("):
            print(zeile[5:-1])

        elif zeile.startswith("wiederhole "):
            teile = zeile.split(" mal ")
            if len(teile) == 2:
                try:
                    anzahl = int(eval(teile[0], {}, variablen))
                    for _ in range(anzahl):
                        run_espp_code(teile[1])
                except:
                    print("❌ Fehler in der Schleife!")

        elif zeile.startswith("solange "):
            teile = zeile.split(" tue ")
            if len(teile) == 2:
                try:
                    while eval(teile[0], {}, variablen):
                        run_espp_code(teile[1])
                except:
                    print("❌ Fehler in der While-Schleife!")

        elif zeile.startswith("zähle "):
            teile = zeile.split(" bis ")
            if len(teile) == 2:
                try:
                    start, ende = map(int, teile)
                    for i in range(start, ende + 1):
                        print(i)
                except:
                    print("❌ Fehler in der For-Schleife!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Gib eine .espp-Datei an!")
        sys.exit(1)

    dateipfad = sys.argv[1]
    with open(dateipfad, "r", encoding="utf-8") as file:
        code = file.read()

    run_espp_code(code)

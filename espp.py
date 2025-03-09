import sys
import math

variablen = {}

def run_espp_code(code):
    zeilen = code.split("\n")
    
    for zeile in zeilen:
        zeile = zeile.strip()
        
        
        if zeile.startswith("</>"):
            continue 
        
        
        elif zeile.startswith('ausgabe("') and zeile.endswith('")'):
            inhalt = zeile[len('ausgabe("'):-2]
            print(inhalt)
        
        
        elif "=" in zeile and "eingabe" in zeile:
            var_name = zeile.split("=")[0].strip()
            wert = input(f"{var_name}: ")
            variablen[var_name] = wert
        
       
        elif "=" in zeile:
            teile = zeile.split("=")
            var_name = teile[0].strip()
            wert = teile[1].strip()
            
            
            if wert.isdigit():
                variablen[var_name] = int(wert)
            elif wert.replace(".", "", 1).isdigit():
                variablen[var_name] = float(wert)
            else:
                variablen[var_name] = wert  
        
       
        elif zeile.startswith("wenn "):
            bedingung = zeile[5:].split(" dann ")
            if len(bedingung) == 2:
                ausdruck, aktion = bedingung
                try:
                    if eval(ausdruck, {}, variablen):
                        run_espp_code(aktion)
                except:
                    print("Fehler in der Bedingung!")

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
                print("Fehler: Division durch 0!")
            else:
                print(zahlen[0] / zahlen[1])

        elif zeile.startswith("sinus("):
            zahl = float(zeile[6:-1])
            print(math.sin(math.radians(zahl)))

        elif zeile.startswith("cosinus("):
            zahl = float(zeile[8:-1])
            print(math.cos(math.radians(zahl)))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gib eine .espp-Datei an!")
        sys.exit(1)

    dateipfad = sys.argv[1]
    with open(dateipfad, "r", encoding="utf-8") as file:
        code = file.read()

    run_espp_code(code)

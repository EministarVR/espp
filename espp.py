import sys

def run_espp_code(code):
    if 'ausgabe("' in code:
        print(code.replace('ausgabe("', "").replace('")', ""))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gib eine .espp-Datei an!")
        sys.exit(1)

    dateipfad = sys.argv[1]
    with open(dateipfad, "r", encoding="utf-8") as file:
        code = file.read()

    run_espp_code(code)

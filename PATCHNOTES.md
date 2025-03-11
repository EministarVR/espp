# Patchnotes - Build 1.0.2 Alpha

## Was ist neu?

- **Leerzeilen (Abstände):**  
  Es gibt jetzt eine Möglichkeit, Leerzeilen hinzuzufügen, um Platz im Code zu schaffen. Verwende `leer: linie;`, um eine leere Zeile zu erzeugen, die die Lesbarkeit des Codes verbessert.

- **Neue mathematische Funktionen:**
  - `wurzel(x)` – Berechnet die Quadratwurzel einer Zahl.
  - `potenz(x, y)` – Berechnet die Potenz von `x` hoch `y`.
  - `log(x)` – Berechnet den natürlichen Logarithmus von `x`.

- **Erweiterte Schleifen:**   - leider macht dies immernoch kleine Probleme :(
  - **`wiederhole x mal`** – Ermöglicht das wiederholte Ausführen eines Codeblocks für eine angegebene Anzahl von Iterationen.

- **Verbesserte Bedingungen:**  
  - Bedingungen können jetzt komplexer formuliert werden, um dynamische Berechnungen und Vergleiche durchzuführen.
  - Verwende `wenn ... dann` und `sonst`, um Alternativen hinzuzufügen.

- **Verbesserte Berechnungen mit Variablen:**  
  Variablen können jetzt direkt mit mathematischen Operationen und Funktionen genutzt werden, um dynamische Werte zu berechnen.

---

## Beispiel-Code:

### 1. **Berechnungen mit Variablen**
```
ausgabe("Berechnung von 3 + 5")
a = 3 + 5
ausgabe(a)  </> Ausgabe: 8
```
---

## 2. Verwendung von Wurzel und Potenz

```
ausgabe("Wurzel von 16")
wurzelErgebnis = wurzel(16)
ausgabe(wurzelErgebnis)  </> Ausgabe: 4.0

ausgabe("Potenz von 2 hoch 3")
potenzErgebnis = potenz(2, 3)
ausgabe(potenzErgebnis)  </> Ausgabe: 8.0
```

---

## 3. Logarithmus Berechnung
```
ausgabe("Logarithmus von 10")
logErgebnis = log(10)
ausgabe(logErgebnis)  </> Ausgabe: 2.302585092994046
```
---

## 4. Bedingung und Variablen
```
a = 10
b = 5
wenn a > b dann
    ausgabe("a ist größer als b!")
sonst
    ausgabe("a ist nicht größer als b!")
```

---
## 5. Berechnungen mit Variablen

```
ausgabe("Berechnung von a + b")
summeErgebnis = summe(a, b)
ausgabe(summeErgebnis)  // Ausgabe: 15
```

---

## Bugfixes:

### Fehlerbehebung bei Eingabeaufforderungen:
Leichtere Fehler Angaben

### Stabilitätsverbesserungen:
Verbesserte Codeausführung und Reduzierung von möglichen Abstürzen bei komplexeren Berechnungen.

## Hinweis:
Die Version 1.0.2 Alpha enthält mehrere neue Funktionen, die die Lesbarkeit des Codes verbessern und erweiterte mathematische Berechnungen ermöglichen. Teste die neuen Features und gebe uns Feedback!


--- 

# Mit Liebe gemacht!

```
  ______           _       _     _          __      _______  
 |  ____|         (_)     (_)   | |         \ \    / /  __ \ 
 | |__   _ __ ___  _ _ __  _ ___| |_ __ _ _ _\ \  / /| |__) |
 |  __| | '_ ` _ \| | '_ \| / __| __/ _` | '__\ \/ / |  _  / 
 | |____| | | | | | | | | | \__ \ || (_| | |   \  /  | | \ \ 
 |______|_| |_| |_|_|_| |_|_|___/\__\__,_|_|    \/   |_|  \_\
                                                             
                                                             
```

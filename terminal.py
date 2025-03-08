import tkinter as tk
import subprocess
import sys

class ESPPTerminal(tk.Tk):
    def __init__(self, dateipfad):
        super().__init__()
        self.title("Es++ Terminal")
        self.geometry("600x400")
        self.configure(bg="black")

        self.text = tk.Text(self, bg="black", fg="lime", insertbackground="white", font=("Consolas", 12))
        self.text.pack(expand=True, fill="both")

        self.run_espp(dateipfad)

    def run_espp(self, dateipfad):
        process = subprocess.Popen(["python", "espp.py", dateipfad], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        self.text.insert("end", stdout)
        if stderr:
            self.text.insert("end", "\nFEHLER:\n" + stderr, "error")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Espp-Datei fehlt!")
        sys.exit(1)

    app = ESPPTerminal(sys.argv[1])
    app.mainloop()

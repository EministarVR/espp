import tkinter as tk
from tkinter import PhotoImage
import subprocess
import sys
import time
import webbrowser
from threading import Thread

class ESPPTerminal(tk.Tk):
    def __init__(self, dateipfad):
        super().__init__()
        self.title("Es++ Terminal")
        self.geometry("700x500")
        self.configure(bg="black")
        self.dateipfad = dateipfad

       
        self.icon_frame = tk.Frame(self, bg="black")
        self.icon_frame.pack(side="top", anchor="ne", padx=10, pady=5)

        try:
            self.github_icon = PhotoImage(file="github.png").subsample(15, 15)
            self.github_button = tk.Label(self.icon_frame, image=self.github_icon, bg="black", cursor="hand2")
            self.github_button.pack(side="right", padx=5)
            self.github_button.bind("<Enter>", lambda e: self.show_tooltip("Dieses Tool ist Open Source"))
            self.github_button.bind("<Leave>", self.hide_tooltip)
            self.github_button.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/EministarVR/espp"))
        except:
            pass

        try:
            self.discord_icon = PhotoImage(file="discord.png").subsample(15, 15)
            self.discord_button = tk.Label(self.icon_frame, image=self.discord_icon, bg="black", cursor="hand2")
            self.discord_button.pack(side="right", padx=5)
            self.discord_button.bind("<Enter>", lambda e: self.show_tooltip("Join unserer Community"))
            self.discord_button.bind("<Leave>", self.hide_tooltip)
            self.discord_button.bind("<Button-1>", lambda e: webbrowser.open("https://discord.gg/fkDM9U7Wdc"))
        except:
            pass

        
        self.logo_label = tk.Label(self, bg="black")
        self.logo_label.pack(expand=True)

        self.loading_label = tk.Label(self, text="💫 Es++ wird geladen...", font=("Consolas", 16), fg="lime", bg="black")
        self.loading_label.pack()

        
        self.after(100, self.show_start_animation)

    def show_start_animation(self):
        try:
            logo = PhotoImage(file="logo.png")
            self.logo_label.config(image=logo)
            self.logo_label.image = logo 
        except:
            self.logo_label.config(text="Es++", font=("Consolas", 32), fg="lime")

        self.update()
        time.sleep(5)  

        self.init_terminal()

    def init_terminal(self):
       
        self.logo_label.pack_forget()
        self.loading_label.pack_forget()

       
        self.text = tk.Text(self, bg="black", fg="lime", insertbackground="white", font=("Consolas", 12), wrap="word")
        self.text.pack(expand=True, fill="both", padx=10, pady=10)

       
        self.button_frame = tk.Frame(self, bg="black")
        self.button_frame.pack(fill="x", padx=10, pady=5)

        self.run_button = tk.Button(self.button_frame, text="🔄 Neu ausführen", command=self.restart_espp, font=("Consolas", 12), bg="gray20", fg="white", relief="flat")
        self.run_button.pack(fill="x")

        
        self.text.insert("end", "💫 Es++ Terminal gestartet...\n\n")
        self.text.config(state="disabled")
        Thread(target=self.run_espp, daemon=True).start()

        
        self.tooltip = tk.Label(self, text="", font=("Consolas", 10), fg="white", bg="gray20", padx=5, pady=2)
        self.tooltip.place_forget()

    def show_tooltip(self, text):
        self.tooltip.config(text=text)
        self.tooltip.place(relx=0.98, rely=0.03, anchor="ne")

    def hide_tooltip(self, event=None):
        self.tooltip.place_forget()

    def run_espp(self):
        self.insert_text("⚡ Starte Skript...\n")
        process = subprocess.Popen(["python", "espp.py", self.dateipfad], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in iter(process.stdout.readline, ""):
            self.insert_text(line)
        
        stderr_output = process.stderr.read()
        if stderr_output:
            self.insert_text("\n❌ FEHLER:\n" + stderr_output, "error")

    def restart_espp(self):
        self.text.config(state="normal")
        self.text.delete("1.0", "end")  
        self.text.insert("end", "🔄 Skript wird neu gestartet...\n\n")
        self.text.config(state="disabled")

        Thread(target=self.run_espp, daemon=True).start()

    def insert_text(self, text, tag=None):
        self.text.config(state="normal")
        self.text.insert("end", text, tag)
        self.text.see("end")
        self.text.config(state="disabled")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Espp-Datei fehlt!")
        sys.exit(1)

    app = ESPPTerminal(sys.argv[1])
    app.mainloop()
import os
import shutil
import subprocess

INSTALL_PATH = "C:\\Programme\\Espp"

def install():
    if not os.path.exists(INSTALL_PATH):
        os.makedirs(INSTALL_PATH)

    shutil.copy("dist/espp.exe", INSTALL_PATH)
    shutil.copy("dist/terminal.exe", INSTALL_PATH)

    reg_command = f'reg add "HKEY_CLASSES_ROOT\\.espp" /ve /d "EsppFile" /f'
    subprocess.run(reg_command, shell=True)

    reg_command = f'reg add "HKEY_CLASSES_ROOT\\EsppFile\\shell\\open\\command" /ve /d "{INSTALL_PATH}\\terminal.exe %1" /f'
    subprocess.run(reg_command, shell=True)

    print("Es++ wurde erfolgreich installiert!")

if __name__ == "__main__":
    install()

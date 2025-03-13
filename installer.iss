[Setup]
AppName=Es++ Terminal
AppVersion=1.0
AppPublisher=Eministar Dev Group n.e.V.
AppPublisherURL=https://github.com/EministarVR
AppSupportURL=https://discord.gg/ErFRp9eSrj
AppUpdatesURL=https://github.com/EministarVR/espp/releases
DefaultDirName={pf}\EsppTerminal
DefaultGroupName=EsppTerminal
UninstallDisplayIcon={app}\terminal.exe
OutputDir=.
OutputBaseFilename=EsppInstaller
Compression=lzma2
SolidCompression=yes
WizardImageFile=logo.bmp
WizardSmallImageFile=logo_small.bmp

[Files]
Source: "dist\terminal.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "espp.py"; DestDir: "{app}"; Flags: ignoreversion
Source: "logo.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "Eministar.cer"; DestDir: "{tmp}"; Flags: deleteafterinstall

[Icons]
Name: "{group}\Es++ Terminal"; Filename: "{app}\terminal.exe"

[Registry]
Root: HKCR; Subkey: ".espp"; ValueType: string; ValueData: "ESPPScript"; Flags: uninsdeletekey
Root: HKCR; Subkey: "ESPPScript\shell\open\command"; ValueType: string; ValueData: """{app}\terminal.exe"" ""%1"""

[Run]
Filename: "{cmd}"; Parameters: "/C certutil -addstore Root {tmp}\Eministar.cer"; Flags: runhidden

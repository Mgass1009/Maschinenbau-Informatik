druck = int(input(" Aktueller Systemdruck (bar): "))

if(druck <= 50):
    print(f" FEHLER: Druck zu niedrig {druck} bar")
else:
    print(F" Druck OK {druck} bar. System betriebsbereit.")
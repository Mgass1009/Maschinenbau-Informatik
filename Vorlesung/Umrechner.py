print ("Willkommen zum Kilometer-Umrechner!")
print ("Möchten Sie von Kilomnetern zu Metern (km zu m) oder andersrum umrechnen?")
umrechnung = input("Geben Sie 'km zu m' oder 'm zu km' ein: ")
if umrechnung == "km zu m":
    km = float(input("Geben Sie die Strecke in Kilometern ein: "))
    m = km * 1000
    print(f"{km} Kilometer sind {m} Meter.")
elif umrechnung == "m zu km":
    m = float(input("Geben Sie die Strecke in Metern ein: "))
    km = m / 1000
    print(f"{m} Meter sind {km} Kilometer.")
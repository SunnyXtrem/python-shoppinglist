shoppinglist = []  # Initialisierung der Einkaufsliste

def show_shoppinglist():
    if shoppinglist:  # Überprüfen, ob die Einkaufsliste nicht leer ist
        print("Deine Einkaufsliste:")
        for item in shoppinglist:  # Jedes Element in der Einkaufsliste ausgeben
            print(f"- {item}")
    else:
        print("Deine Einkaufsliste ist leer")  # Ausgabe, wenn die Liste leer ist

def main():
    while True:  # Endlosschleife für das Menü
        print("\n----- Einkaufsliste -----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")
        
        choice = input("Bitte wähle eine Option (1, 2 oder 3): ")

        if choice == '1':
            item = input("Gib den Artikel ein, den du hinzufügen möchtest: ")
            shoppinglist.append(item)  # Artikel zur Liste hinzufügen
        elif choice == '2':
            show_shoppinglist()  # Einkaufsliste anzeigen
        elif choice == '3':
            print("Programm wird beendet! Auf Wiedersehen")
            break  # Schleife beenden
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")  # Fehlerausgabe

            if __name__ == "__main__":
    main()  # Hauptprogramm starten
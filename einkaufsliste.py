shoppinglist = []  # Initialisierung der Einkaufsliste

def show_shoppinglist():
    if shoppinglist:  # Überprüfen, ob die Einkaufsliste nicht leer ist
        print("Deine Einkaufsliste:")
        for item in shoppinglist:  # Jedes Element in der Einkaufsliste ausgeben
            print(f"- {item}")
    else:
        print("Deine Einkaufsliste ist leer")  # Ausgabe, wenn die Liste leer ist

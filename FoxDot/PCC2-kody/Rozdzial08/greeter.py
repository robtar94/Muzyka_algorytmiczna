def get_formatted_name(first_name, last_name):
    """Zwraca elegancko sformatowane pełne imię i nazwisko."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# To jest pętla działająca w nieskończoność!
while True:
    print("\nProszę podać imię i nazwisko:")
    print("(wpisz 'q', aby zakończyć pracę w dowolnym momencie)")
    
    f_name = input("Imię: ")
    if f_name == 'q':
        break
        
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nWitaj, {formatted_name}!")

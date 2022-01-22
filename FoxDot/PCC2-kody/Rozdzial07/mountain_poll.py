responses = {}

# Ustawienie flagi wskazującej, czy ankieta jest aktywna.
polling_active = True

while polling_active:
    # Prośba o podanie imienia uczestnika ankiety oraz odpowiedzi na pytanie.
    name = input("\nJak masz na imię? ")
    response = input("Na który szczyt chciałbyś się wspiąć pewnego dnia? ")

    # Umieszczenie odpowiedzi w słowniku:
    responses[name] = response

    # Ustalenie, czy ktokolwiek jeszcze chce wziąć udział w ankiecie.
    repeat = input("Czy ktokolwiek inny chce wziąć udział w ankiecie? (tak / nie) ")  
    if repeat == 'nie':
        polling_active = False

# Ankieta została zakończona i wyświetlamy jej wyniki.
print("\n--- Wyniki ankiety ---")
for name, response in responses.items():
    print(f"{name} chciałby się wspiąć na {response}.")

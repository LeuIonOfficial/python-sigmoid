# Aceeasta este prima sarcină a aceestei lecții și este legată de dicționare.

# Creați un dicțioar gol

# CODUL TĂU VINE MAI JOS:
obj = {}
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "name" și valoarea fiind "John"

# CODUL TĂU VINE MAI JOS:
obj['name'] = "Jhon"
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "age" și valoarea fiind 30

# CODUL TĂU VINE MAI JOS:
obj['age'] = 30
# CODUL TĂU VINE MAI SUS:

# Acum afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(obj)
# CODUL TĂU VINE MAI SUS:

# Acum ștergeți cheia "name" din dicționar

# CODUL TĂU VINE MAI JOS:
del obj['name']
# CODUL TĂU VINE MAI SUS:

# Acum afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(obj)
# CODUL TĂU VINE MAI SUS:

# Acum adăugați o pereche de cheie-valoare în dicționar, cheia fiind "city" și valoarea fiind "New York" folosind metoda setdefault()

# CODUL TĂU VINE MAI JOS:
obj.setdefault('city', 'New York')
# CODUL TĂU VINE MAI SUS:

# Afișați toate cheile din dicționar 

# CODUL TĂU VINE MAI JOS:
print(obj.keys())
# CODUL TĂU VINE MAI SUS:

# Afișați toate valorile din dicționar

# CODUL TĂU VINE MAI JOS:
print(obj.values())
# CODUL TĂU VINE MAI SUS:

# Afișați toate perechile de cheie-valoare din dicționar folosind metoda items()

# CODUL TĂU VINE MAI JOS:
print(obj.items())
# CODUL TĂU VINE MAI SUS:

# Afișați numărul de perechi de cheie-valoare din dicționar

# CODUL TĂU VINE MAI JOS:
print(len(obj.items()))
# CODUL TĂU VINE MAI SUS:

# Extrageți valoarea unei chei inexistente fără a genera o eroare

# CODUL TĂU VINE MAI JOS:
print(obj.get('inexistent')) 
# CODUL TĂU VINE MAI SUS:

# Acum actualizați dicționarul cu un alt dicționar, folosind metoda update()

# CODUL TĂU VINE MAI JOS:
obj.update({'country': "Moldova"})
# CODUL TĂU VINE MAI SUS:

# Setați valoarea cheii "pizza" la 10 folosind metoda setdefault()

# CODUL TĂU VINE MAI JOS:
obj.setdefault("pizza", 10)
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(obj)
# CODUL TĂU VINE MAI SUS:

# Ștergeți cheia "pizza" din dicționar folosind metoda pop()

# CODUL TĂU VINE MAI JOS:
obj.pop("pizza")
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(obj)
# CODUL TĂU VINE MAI SUS:

# Ștergeți toate perechile de cheie-valoare din dicționar

# CODUL TĂU VINE MAI JOS:
obj.clear()
# CODUL TĂU VINE MAI SUS:

# Afișați dicționarul

# CODUL TĂU VINE MAI JOS:
print(obj)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de dicționare

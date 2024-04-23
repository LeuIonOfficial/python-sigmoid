# Aceasta este tema pentru lecția 8 legată de loops
import random

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
my_list = [i for i in range(1, 11)]
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
print([i for i in my_list if i % 2 == 0])
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print(i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {
    'name': "Ion",
    'age': 22,
    'city': "Chisinau"
}

for attr, value in person.items():
    print(f"{attr} - {value}")
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
data = [
    [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ],
    [
        [2, 3, 4],
        [2, 3, 4],
        [2, 3, 4]
    ],
    [
        [3, 4, 5],
        [3, 4, 5],
        [3, 4, 5]
    ],
    [
        [4, 5, 6],
        [4, 5, 6],
        [4, 5, 6]
    ],
]

for arr in data:
    for numbers in arr:
        for number in numbers:
            print(number)
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
numere = [num for num in range(50)]
for num in numere:
    print(num)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
enum_numbers = enumerate(numere)
for attr, value in enum_numbers:
    print(attr)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
zipped_list = zip(numere, my_list)
print(list(zipped_list))
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
list_of_numbers = [num for num in range(1,11)]
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
while list_of_numbers[0] <= 50:
    for index, element in enumerate(list_of_numbers):
        list_of_numbers[index] = element * 2
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
print([num for num in range(1, 100) if (num ** 0.5).is_integer()])
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
print([num*7 for num in range(1,10)])
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
random_list = []

while len(random_list) < 10:
    i = random.randint(1,5)
    j = random.randint(1,5)
    random_list.append([i, j])

print(random_list)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
print([element for element in random_list if element[0] < element[1]])
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
new_random_list = [random.randint(0, 12) for _ in range(10)]
is_greater = False
another_number = new_random_list[0]
loop = 0

while loop < len(new_random_list):
    print(loop)
    if another_number > 10:
        is_greater = True
        break
    another_number = new_random_list[loop]
    loop = loop + 1

if not is_greater:
    print("Nu există valori mai mari decât 10")
else:
    print(another_number)
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
dimensiune_patrat = int(input("Indica dimensiunea patratului:"))
for i in range(dimensiune_patrat):
    print("*" * dimensiune_patrat)
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(1,7):
    for j in range(1,i+1):
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(5,0, -1):
    for j in range(1, i+1, 1):
        print(j, end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
list_of_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(len(list_of_words)):
    print("".join(list_of_words))
    list_of_words.pop()
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
starts_with = '+-'

for i in range(1, 9):
    print(starts_with * 16)
    if starts_with == "+-":
        starts_with = "-+"
    else:
        starts_with = "+-"

# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
lista_de_numere = [3 ** i for i in range(1,6)]
print(lista_de_numere)

for i in range(len(lista_de_numere)):
    for j in range(0, i+1):
        print(lista_de_numere[j], end=" ")
    print()

while lista_de_numere:
    print(" ".join([str(num) for num in lista_de_numere]))
    lista_de_numere.pop(0)

# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.

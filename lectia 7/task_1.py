# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number = 100
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number > 0:
    print("Numarul este pozitiv")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number%2== 0:
    print("Numarul este par")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number%2 != 0:
    print("Numarul este impar")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = "alabala"
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if text.rfind("Python") != -1:
    print("Textul contine cuvantul 'Python'")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if text.rfind("Java") != -1:
    print("Textul contine cuvantul 'Java'")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if text.rfind("Python") != -1:
    if text.rfind("Java") != -1:
        print("Textul contine cuvantul 'Python' și 'Java'")
    else:
        print("Textul contine cuvantul 'Python'")
else:
    print("Textul nu contine niciunul din cuvinte")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if text.rfind("Python") != -1 and text.rfind("Java") != -1:
    print("Textul contine cuvantul 'Python' și 'Java'")
elif text.rfind("Python") == -1 and text.rfind("Java") != -1:
    print("Textul contine doar cuvantul 'Java'")
elif text.rfind("Python") != -1 and text.rfind("Java") == -1:
    print("Textul contine doar cuvantul 'Python'")
else:
    print("Textul nu contine niciunul din cuvinte")
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
numar = int(input("Un numar intre 1 si 5\n"))
if numar == 1:
    print("Unu")
elif numar == 2:
    print("Doi")
elif numar == 3:
    print("Trei")
elif numar == 4:
    print("Patru")
elif numar == 5:
    print("Cinci")
# CODUL TĂU VINE MAI SUS:



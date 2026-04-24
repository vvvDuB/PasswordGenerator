import secrets
import string

def custom() -> (int, bool, bool, bool, bool, bool, str):
    maiuscole = False if input("Maiuscole? (y/n) [y]:") == "n" else True
    minuscole = False if input("Minuscole? (y/n) [y]:") == "n" else True
    cifre = False if input("Cifre (y/n) [y]:") == "n" else True
    simboli = False if input("Simboli (y/n) [y]:") == "n" else True
    lunghezza = False if input("Lunghezza [12]:") == "n" else True
    ambigui = False if input("Evitare caratteri ambigui? (y/n) [n]:") == "n" else True
    file = False if input("Salvare su file? (y/n) [n]:") == "n" else True
    
    if file:
        path = input("Path del file: ")
    
    if lunghezza == "":
        lunghezza = 12

    return ([maiuscole, minuscole, cifre, simboli, lunghezza, ambigui, file], path)

def generate_password(
    length: int = 12,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
    avoid_ambiguous: bool = False,
) -> str:
    password = []
    dataset = []
    if use_upper:
        dataset.append(list(string.ascii_uppercase))

    if use_lower:
        dataset.append(list(string.ascii_lowercase))

    if use_digits:
        dataset.append(list(string.digits))

    if use_symbols:
        dataset.append(list(string.punctuation))
    
    if avoid_ambiguous:
        ambiguous = ['I', 'l', '1', 'O', '0']
        for dt in dataset:
            for amb in ambiguous:
                if amb in dt:
                    dt.remove(amb)
     
    flags = [(use_upper, string.ascii_uppercase), 
             (use_lower, string.ascii_lowercase), 
             (use_digits, string.digits),
             (use_symbols, string.punctuation)]
   
    if not use_upper and not use_lower and not use_digits and not use_symbols:
        raise ValueError("Errore")

    if length < 4:
        raise ValueError("Lunghezza della password minima: 4")

    for c in range(length):
        p = secrets.choice(dataset[c % len(dataset)])
        password.append(p)
    
    secrets.SystemRandom().shuffle(password)
    return "".join(password)

def main():
    print("=== Password generator ===")
    print("1) Profilo default (12 caratteri, tutti i set, visualizza a schermo)")
    print("2) Profilo custom")
    choise = int(input())
    
    path = ""
    password = ""
    cus = None
    data = None
    if choise == 2:
        print(f"Hai scelto: {choise}")
        data, path = custom()
    
    if cus:
        password = generate_password(data)
    else:
        password = generate_password()
    
    print(password)
    if path:
        with open(path, "w") as file:
            file.write(password)
            print(f"Saved to: {path}")

if __name__ == "__main__":
    main()

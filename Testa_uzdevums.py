# Ielasīt datnes nosaukumu no ievades un atvērt datni
filename = input("Ievadiet datnes nosaukumu: ")
try:
    with open(filename, 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("Kļūda: datne nav atrasta.")
    exit()

# Izvadīt simbolu skaitu datnē
print(f"Datnes simbolu skaits: {len(data)}")

# Izvadīt pirmos 10 simbolus
print(f"Pirmie 10 simboli: {data[:10]}")

# Izvadīt pirmo un pēdējo simbolu
print(f"Pirmais simbols: {data[0]}, pēdējais simbols: {data[-1]}")

# Ielasīt un pārbaudīt ievadīto garumu, izvadīt simbolus līdz tam
garums = input("Ievadiet garumu: ")
if not garums.isdigit():
    print("Kļūda: ievadīts nekorekts garums.")
    exit()
garums = int(garums)
if garums > len(data):
    print("Kļūda: ievadītais garums ir lielāks par datnes garumu.")
    exit()
print(f"Pirmais {garums} simboli: {data[:garums]}")


# Funkcija, kas izvada pirmo rindiņu no datnes
def print_first_line(filename):
    try:
        with open(filename, 'r') as file:
            first_line = file.readline()
            print(first_line)
    except FileNotFoundError:
        print("Kļūda: datne nav atrasta.")


# Izsaukt funkciju, lai izvadītu pirmo rindiņu no datnes
print_first_line(filename)
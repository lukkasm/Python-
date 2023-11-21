import os

script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

try:
    f = open('veci.txt', 'r')
    weights = []
    current_weight = 0
    for line in f:
        line = line.strip()
        if line:
            weight = int(line)
            weights.append(weight)
            current_weight += weight
        else:
            f2 = open('baliky.txt', 'a')
            f2.write(str(current_weight) + '\n')
            f2.close()
            current_weight = 0
    f2 = open('baliky.txt', 'a')
    f2.write(str(current_weight) + '\n')
    f2.close()

    f = open('baliky.txt', 'r')
    max_weight = -1
    max_weight_index = -1
    for i, line in enumerate(f):
        weight = int(line.strip())
        if weight > max_weight:
            max_weight = weight
            max_weight_index = i + 1

    print(f"Největší hmotnost má balík číslo {max_weight_index} a to {max_weight} kg.")

    f.close()
except FileNotFoundError:
    print("Soubor veci.txt nebyl nalezen.")
except Exception:
    print("Chyba při práci se souborem.")


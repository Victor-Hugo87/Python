import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False

def is_number(val):
    return is_int(val) or is_float(val)

hora = input("Digite a hora atual: ")

if is_number(hora):
    hora = float(hora)

    if hora <= 11.59:
        print("Bom dia!")
    elif hora <= 17.59:
        print("Boa tarde!")
    elif hora <= 23.59:
        print("Boa noite!")
else:
    print("Digite a hora atual nesse fomato (HH.MM): ")

#D1 Adam Mikolajczak 481890
import time
def set_deepness():
    try:
        value = input("Podaj głębokość równania rekurencyjnego: ")
        n = int(value)
        if n >= 1 and n <= 3:
            return n
        else: 
            print("Dostępne głębokości: 1,2,3")
            return -1
    except ValueError:
        print("Dostępne głębokości: 1,2,3")
        return -1
    
def set_coefficients(deepness):
    coefficients = []
    if deepness == 1:
        print("Twoje równanie jest postaci:")
        print("a_n = A*a_n-1")
        A = float(input("A = "))
        coefficients.append(A)
        print("Równanie:")
        print(f"a_n = {A}*a_n-1")
    if deepness == 2:
        print("Twoje równanie jest postaci:")
        print("a_n = A*a_n-1 + B*a_n-2")
        A = float(input("A = "))
        coefficients.append(A)
        B = float(input("B = "))
        coefficients.append(B)
        print("Równanie:")
        print(f"a_n = {A}*a_n-1 + {B}*a_n-2")
    if deepness == 3:
        print("Twoje równanie jest postaci:")
        print("a_n = A*a_n-1 + B*a_n-2 + C*a_n-3")
        A = float(input("A = "))
        coefficients.append(A)
        B = float(input("B = "))
        coefficients.append(B)
        C = float(input("C = "))
        coefficients.append(C)
        print("Równanie:")
        print(f"a_n = {A}*a_n-1 + {B}*a_n-2 + {C}*a_n-3")
    return coefficients

def set_base_cases(deepness):
    base_cases = []
    for i in range(deepness):
        case = float(input(f"a_{i} = "))
        base_cases.append(case)
    return base_cases

def recurrence(deepness, base_cases, coefficients, n):
    if n < deepness:
        return(base_cases[n])
    else:
        value = 0
        for j in range(deepness):
            value += coefficients[j]*recurrence(deepness, base_cases, coefficients, n-j-1)
        return value

if __name__ == '__main__':
    while True:
        deepness = set_deepness()
        if deepness != -1 : break
    coefficients = set_coefficients(deepness)
    base_cases = set_base_cases(deepness)
    print("Liczenie pierwszych 30 wyrazów zapomocą rekurencji...")
    start_time = time.time()
    for i in range(30):
        value = recurrence(deepness, base_cases, coefficients, i)
    reccursive_time = time.time() - start_time
    print(f"a_30 = {value}")
    print(f"Czas działania algorytmu rekurencyjnego dla pierwszych 30 wyrazów zadanego ciągu wynosi {reccursive_time} sekund")
    start_time = time.time()
    sequence = []
    i=0
    while i < 30:
        if i < deepness:
            sequence.append(base_cases[i])
        else:
            value = 0
            for j in range(deepness):
                value += coefficients[j]*sequence[i-j-1]
            sequence.append(value)
        i+=1
    itterative_time = time.time() - start_time
    print(f"a_30 = {value}")
    if itterative_time < 1:
        print("Czas działania algorytmu iteracyjnego dla pierwszych 30 wyrazów zadanego ciągu wynosi poniżej 1 sekundy")
    else:
        print(f"Czas działania algorytmu iteracyjnego dla pierwszych 30 wyrazów zadanego ciągu wynosi {itterative_time} sekund")
    
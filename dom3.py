#ZADANIE D3, ADAM MIKOLAJCZAK
def set_n():
    while True:
        try:
            value = input()
            n = int(value)
            return n
        except ValueError:
            print("Podaj liczbę naturalną")

def set_sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(int(input()))
    return sequence

def  is_graphic(sequence: list):
    if sum(sequence) % 2 != 0:
        print("Suma stopni w podanym ciągu nie jest parzysta.")
        return False
    elif max(sequence) > len(sequence):
        print("Co najmniej jeden ze stopni jest większy niż długość ciągu -1")
        return False
    else:
        if all(deg == 2 for deg in sequence) : return True
        for i in range(n):
            current = sequence.pop(0)
            for j in range(current):
                sequence[j] -= 1
            sequence.sort(reverse=True)
            for num in sequence:
                if num < 0:
                    return False
            if sum(sequence) == 0:
                return True
            print("Zastosowanie algorytmu nie powiodło się - końcowy stan ciągu nie jest złożony z samych zer.")
            return False
    
def create_matrix(sequence: list):
    n = len(sequence)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    is_cycle = all(deg == 2 for deg in sequence)
    if is_cycle:
        for i in range(n):
            matrix[i][(i + 1) % n] = 1
            matrix[(i + 1) % n][i] = 1
        return matrix

    for i in range(n):
        for j in range(i+1, n):
            if sequence[i] > 0 and sequence[j] > 0:
                sequence[i] -= 1
                sequence[j] -= 1
                matrix[i][j] = 1
                matrix[j][i] = 1
    return matrix

def print_matrix(matrix):
    print()
    print("Macierz przyległości ciągu: ")
    for r in matrix:
        for c in r:
            print(c,end = " ")
        print()


if __name__ == '__main__':
    print("Podaj długość ciągu")
    n = set_n()
    print("Wpisz po kolei wyrazy ciągu:")
    sequence = set_sequence(n)
    sequence.sort(reverse=True)
    given_sequence = sequence.copy()  
    if is_graphic(sequence):
        print(f"Ciąg {given_sequence} jest graficzny.")
        matrix = create_matrix(given_sequence)
        print_matrix(matrix)
    else:
        print(f"Ciąg {given_sequence} nie jest graficzny.")



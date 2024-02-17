def set_int():
    while True:
        try:
            value = input()
            n = int(value)
            return n
        except ValueError:
            print("Podaj liczbę naturalną")

def set_city(cities: list):
    while True:
        value = input()
        if value in cities: 
            return value
        else: 
            print("Podaj nazwę jednego z miast:")
            print(cities)

def print_matrix(matrix):
    print()
    for r in matrix:
        for c in r:
            print(c,end = " ")
        print()

def sorted_roads(matrix):
    roads = []
    for row in matrix:
        for element in row:
            roads.append(element)
    return roads[::2]

def kruskal_mst(matrix, cities):
    edges = []
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix[i])):
            if matrix[i][j] > 0:
                edges.append((matrix[i][j], cities[i], cities[j]))
    
    edges.sort() 
    
    mst_edges = []
    mst_cost = 0
    roots = [i for i in range(len(cities))]
    
    def find_root(roots, i):
        if roots[i] == i:
            return i
        else:
            return find_root(roots, roots[i])
    
    def union(roots, i, j):
        root_i = find_root(roots, i)
        root_j = find_root(roots, j)
        roots[root_i] = root_j
    
    for edge in edges:
        weight, city1, city2 = edge
        city1_index = cities.index(city1)
        city2_index = cities.index(city2)
        
        if find_root(roots, city1_index) != find_root(roots, city2_index):
            mst_edges.append(edge)
            mst_cost += weight
            union(roots, city1_index, city2_index)
    
    return mst_edges, mst_cost


if __name__ == "__main__":
    print("Podaj n (liczba miast):")
    n = set_int()
    print("Podaj m (liczba dróg pomiędzy miastami):")
    m = set_int()
    print("Podaj b (budzet inwestycji w miliardach CZK):")
    b = set_int()
    cities = []
    cities.append("Kralovec")
    print("Pierwszym miastem jest Kralovec.")
    for i in range(n - 1):
        print("Podaj nazwę kolejnego miasta:")
        miasto = input()
        cities.append(miasto)
    print(cities)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        print(f"Droga nr {i+1}")
        print("Wpisz nazwę pierwszego miasta:")
        city1 = set_city(cities)
        city1index = cities.index(city1)
        print("Wpisz nazwę drugiego miasta.")
        city2 = set_city(cities)
        city2index = cities.index(city2)
        print("Podaj koszt budowy drogi w miliardach CZK:")
        cost = set_int()
        matrix[city1index][city2index] = cost
        matrix[city2index][city1index] = cost
    print("Macierz przyległości grafu reprezentującego połączenia drogowe:")
    print_matrix(matrix)
    mst_edges, mst_cost = kruskal_mst(matrix, cities)
    print("Najtańszy wariant połączenia wszystkich podaych miast:")
    for edge in mst_edges:
        weight, city1, city2 = edge
        print(f"{city1} -- {city2} : {weight} mld CZK")
    print(f"Całkowity koszt budowy Piwociągu: {mst_cost} mld CZK")
    if mst_cost <= b:
        print("Koszt inwestycji zawiera się w podanych załozeniach.")
    else:
        print("Koszt inwestycji jest drozszy niz przewidziany budzet.")
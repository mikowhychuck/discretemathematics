#zadanie D.1, Adam Mikołajczak s481890
letters = ["U", "V", "W", "X", "Y", "Z"]

def set_n():
    try:
        value = input("n = ")
        n = int(value) + 1
        if n >= 0 and n <= 10:
            return n
        else: 
            print("Podaj liczbę naturalną z zakresu [0;9]")
            return -1
    except ValueError:
        print("Podaj liczbę naturalną z zakresu [0;9]")
        return -1
    
def subpoint_a(numbers):
    codes = set()
    i=0
    for letter in letters:
        code1 = '0' + letter
        for number in numbers:
            code2 = code1 + str(number)
            for letter in letters:
                code3 = code2 + letter
                codes.add(code3)
                i+=1    
    for letter in letters:
        code1 = '0' + letter
        for letter in letters:
            code2 = code1 + letter
            for number in numbers:
                code3 = code2 + str(number)
                codes.add(code3)
                i+=1
    for number in numbers:
        code1 = '0' + str(number)
        for letter in letters:
            code2 = code1 + letter
            for letter in letters:
                code3 = code2 + letter
                codes.add(code3)
                i+=1
    print("\tWygenerowane kody:")
    print(codes)
    return i

def subpoint_b(numbers):
    i=0
    codes = set()
    for letter in letters:
        code1 = letter
        for letter in letters:
            code2 = code1 + letter
            for number in numbers:
                code3 = code2 + str(number)
                for number in numbers:
                    code4 = code3 + str(number)
                    codes.add(code4)
                    i+=1
    for number in numbers:
        code1 = str(number)
        for letter in letters:
            code2 = code1 + letter
            for letter in letters:
                code3 = code2 + letter
                for number in numbers:
                    code4 = code3 + str(number)
                    codes.add(code4)
                    i+=1
    for number in numbers:
        code1 = str(number)
        for letter in letters:
            code2 = code1 + letter
            for number in numbers:
                code3 = code2 + str(number)
                for letter in letters:
                    code4 = code3 + letter
                    codes.add(code4)
                    i+=1
    print("\tWygenerowane kody:")
    print(codes)
    return i

def subpoint_c(numbers):
    i=0
    codes = set()
    for number in numbers:
        code1 = str(number)
        for letter in letters:
            code2 = code1 + letter
            for number in numbers:
                code3 = code2 + str(number)
                for letter in letters:
                    code4 = code3 + letter
                    codes.add(code4)
                    i+=1
    for number in numbers:
        code1 = str(number)
        for letter in letters:
            code2 = code1 + letter
            for letter in letters:
                code3 = code2 + letter
                for number in numbers:
                    code4 = code3 + str(number)
                    codes.add(code4)
                    i+=1
    print("\tWygenerowane kody:")
    print(codes)
    return i

def subpoint_d(numbers):
    codes = set()
    i=0
    for letter in letters:
        code1 = letter
        for letter in letters:
            code2 = code1 + letter
            for number in numbers:
                code3 = code2 + str(number)
                for number in numbers:
                    code4 = code3 + str(number)
                    codes.add(code4)
                    i+=1
        for number in numbers:
            code2 = code1 + str(number)
            for letter in letters:
                code3 = code2 + letter
                for number in numbers:
                    code4 = code3 + str(number)
                    codes.add(code4)
                    i+=1
            for number in numbers:
                code3 = code2 + str(number)
                for letter in letters:
                    code4 = code3 + letter
                    codes.add(code4)
                    i+=1
    for number in numbers:
        code1 = str(number)
        for letter in letters:
            code2 = code1 + letter
            for letter in letters:
                code3 = code2 + letter
                for number in numbers:
                    code4 = code3 + str(number)
                    codes.add(code4)
                    i+=1
            for number in numbers:
                code3 = code2 + str(number)
                for letter in letters:
                    code4 = code3 + letter
                    codes.add(code4)
                    i+=1
    print("\tWygenerowane kody:")
    print(codes)
    return i



if __name__ == '__main__':
    print("Zadanie D1 - Adam Mikołajczak 481890")
    print("W pewnej firmie każdemu produktowi przypisywany jest 4-znakowy kod stanowiący ciąg składający się")
    print("z dwóch liter ze zbioru {U, V,W,X, Y,Z} oraz dwóch cyfr ze zbioru {0, 1, 2, . . . , n}, gdzie n jest pewną liczbą naturalną.")
    while True:
        n = set_n()
        if n != -1 : break

    numbers = []
    for i in range(n):
        numbers.append(i)

    print("a)\tPierwszy znak kodu to 0: ")
    print(f"\tw sumie {subpoint_a(numbers)} możliwości")
    print("b)\tDrugi znak kodu to litera")
    print(f"\tw sumie {subpoint_b(numbers)} możliwości")
    print("c)\tPierwszy znak kodu to cyfra, a drugi to litera")
    print(f"\tw sumie {subpoint_c(numbers)} możliwości")
    print("d)\tPierwszy lub drugi znak kodu to litera")
    print(f"\tw sumie {subpoint_d(numbers)} możliwości")

    input()
    
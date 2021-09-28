# Author : Arya Fakhruddin Chandra
# Tujuan -> Referensi untuk bantu mentee
import random as r
robust = True

print("Welcome to MathBot")
print()

def modeOption():
    global robust
    while robust:
        print("""Pilih Mode:
        1. Penjumlahan
        2. Pengurangan
        3. Campur
        4. Akhiri program""")
        print()

        mode_input = input("Masukkan perintah: ")

        if mode_input.isnumeric() == True:
            if int(mode_input) in [1, 2, 3, 4]:
                if int(mode_input) == 4:
                    return "Thanks"

                else:
                    operationMode(int(mode_input)) 
            else:
                print("Perintah tidak dikenali")
                print()
        else:
            print("Perintah tidak dikenali")
            print()

def operationMode(typeOfOperation):
    global robust
    if typeOfOperation == 1:
        print("\noke operasinya penambahan\n")
    
    elif typeOfOperation == 2:
        print("oke operasinya pengurangan")
    
    elif typeOfOperation == 3:
        print("oke operasinya campuran")

    while True:
        print("""Pilih Mode:
        1. Kuis Lepas
        2. Kuis 5
        3. Ganti mode
        4. Akhiri program""")
        print()

        mode_input = input("Masukkan perintah: ")

        if mode_input.isnumeric() == True:
            if int(mode_input) in [1, 2, 3, 4]:
                if int(mode_input) == 3:
                    modeOption()

                elif int(mode_input) == 4:
                    print("Thanks")
                    robust = False
                    break

                else:
                    quizMode(int(mode_input), typeOfOperation)
            else:
                print("Perintah tidak dikenali")
                print()
        else:
            print("Perintah tidak dikenali")
            print()

def quizMode(quizType, typeOfOperation):
    if quizType == 1:
        kuisLepas(typeOfOperation)
    else:
        kuis5(typeOfOperation)

def kuisLepas(typeOfOperation):
    while True:
        a = r.randint(0, 10)
        b = r.randint(0, 10)
        
        if typeOfOperation == 2:
            ops = operation2(a, b)
            print(f"Berapa {ops[1]} - {ops[2]}?")
            key = ops[0]
        
        elif typeOfOperation == 3:
            ops = operation3(a, b)
            if ops[3] == "-":
                print(f"Berapa {ops[1]} - {ops[2]}?")
                key = ops[0]
                
            else:
                print(f"Berapa {ops[1]} + {ops[2]}?")
                key = ops[0]
        
        else:
            ops = operation1(a,b)
            key = ops[0]
            print(f"Berapa {ops[1]} + {ops[2]}?")

        ans = input("Jawab: ")

        if ans.isnumeric() and int(ans) == key:
            print("anjas bener")
        else:
            if ans.lower() == "akhiri kuis":
                operationMode(0)
            elif int(ans) != key:
                print(f"masih salah broo, jawabannya {key}")
            else:
                print("Ga valid")

def kuis5(typeOfOperation):
    numOfPoint = 0
    for i in range(5):
        a = r.randint(0, 10)
        b = r.randint(0, 10)
        
        if typeOfOperation == 2:
            ops = operation2(a, b)
            print(f"Berapa {ops[1]} - {ops[2]}?")
            key = ops[0]
        
        elif typeOfOperation == 3:
            ops = operation3(a, b)
            if ops[3] == "-":
                print(f"Berapa {ops[1]} - {ops[2]}?")
                key = ops[0]

            else:
                print(f"Berapa {ops[1]} + {ops[2]}?")
                key = ops[0]
        
        else:
            ops = operation1(a,b)
            key = ops[0]
            print(f"Berapa {ops[1]} + {ops[2]}?")

        ans = input("Jawab: ")

        if ans.isnumeric() and int(ans) == key:
            print("anjas bener")
            numOfPoint += 20
        else:
            if ans.lower() == "akhiri kuis":
                print(f"Score kamu: {numOfPoint}")
                operationMode(0)

            elif int(ans) != key:
                print(f"masih salah broo, jawabannya {key}")

            else:
                print("Ga valid")
    print(f"Score kamu: {numOfPoint}")

def operation1(a, b):
    return a+b, a, b

def operation2(a, b):
    while b > a:
        a = r.randint(0, 10)
        b = r.randint(0, 10)
    return a-b, a, b

def operation3(a, b):
    operation = ["-", "+"]
    operationType = operation[r.randint(0,1)]
    
    if operationType == "-":
        while b > a:
            a = r.randint(0, 10)
            b = r.randint(0, 10)
        return a-b, a, b, operationType

    else:
        return a+b, a, b, operationType

if __name__ == "__main__" :
    modeOption()
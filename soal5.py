#Soal 5:
#Buatlah sebuah fungsi untuk menghitung nilai faktorial dari sebuah bilangan bulat.
#Contoh parameter: n = 5
#Contoh output: 120

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
nilai = 5
result = factorial(nilai)
print(result)
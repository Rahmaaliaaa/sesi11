#Soal 5:
#Buatlah sebuah fungsi untuk menghitung nilai faktorial dari sebuah bilangan bulat.
#Contoh parameter: n = 5
#Contoh output: 120

#menggunakan metode rekursif
#karena rekursif adalah fungsi yang menghitung faktorial dari bilangan bulat 'n'
# faktorial_rekursif(1) = 1 * 1 = 1
# faktorial_rekursif(2) = 2 * 1 = 2   
# faktorial_rekursif(3) = 3 * 2 = 6   
# faktorial_rekursif(4) = 4 * 6 = 24   
# faktorial_rekursif(5) = 5 * 24 = 120      

def faktorial_rekursif(n):
    if n == 0:
        return 1
    else:
        return n * faktorial_rekursif(n - 1)
    
n = 5
hasil = faktorial_rekursif(n)
print(hasil)    
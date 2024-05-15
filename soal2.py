#Soal 2:
#Buatlah sebuah fungsi untuk menambahkan semua angka dalam sebuah list dan mengembalikan hasilnya.
#Contoh parameter: my_list = [1, 2, 3, 4, 5]
#Contoh output: 15

def hitung(my_list):
    total = 0
    for i in my_list:
        total += i
    return total

my_list = [1,2,3,4,5]
hasil = hitung(my_list)
print(hasil)    
         
  

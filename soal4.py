#Soal 4:
#Tuliskan sebuah fungsi untuk menghitung jumlah elemen unik dalam sebuah daftar (list).
#Contoh parameter: my_list = [1, 2, 3, 3, 4, 4, 5]
#Contoh output: 5

my_list = [1,2,3,3,4,4,5]

def elemen_unik(list_int:list):
    list_int =  set(list_int)
    list_int = list(list_int)
    print(list_int)
    return len(list_int)

print(elemen_unik(my_list))
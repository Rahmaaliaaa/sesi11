#Soal 3:
#Buatlah sebuah fungsi untuk menghitung keliling dan luas persegi panjang dengan menerima input panjang dan lebar.
#Contoh parameter: panjang = 5, lebar = 3
#Contoh output:
#luas 15, keliling 16

def hitungKeliling_dan_hitungLuas(panjang, lebar):
    luas =  panjang * lebar
    kelliling = 2 * (panjang + lebar)
    return [luas, kelliling]

panjang = 5
lebar = 3

hasil = hitungKeliling_dan_hitungLuas(panjang, lebar)
print(hasil)
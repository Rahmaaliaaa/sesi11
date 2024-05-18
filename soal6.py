#Soal 6:
#Tuliskan sebuah fungsi untuk menghitung jumlah kata dalam sebuah kalimat.
#Contoh parameter: kalimat = "Ini adalah contoh kalimat"
#Contoh output: 4

def hitungKalimat(kalimat):
    cek_kalimat = kalimat.split()
    return len(cek_kalimat)
print(hitungKalimat("ini adalah contoh kalimat"))
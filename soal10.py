#Soal 10:
#Buatlah sebuah fungsi untuk menentukan apakah suatu kata adalah anagram atau tidak.
#Contoh parameter: kata1 = "listen", kata2 = "silent"
#Contoh output: True

def anagram(kata1, kata2):
    if sorted(kata1) == sorted(kata2):
        print("Ini adalah Anagram")
    else:
        print("Bukan Anagram")
        
anagram("listen", "silent")
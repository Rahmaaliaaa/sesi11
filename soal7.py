#Soal 7:
#Buatlah sebuah fungsi untuk mengecek apakah sebuah string adalah palindrom atau tidak.
#Contoh parameter: kata = "level"
#Contoh output: "level adalah palindrom"

def palindrome(kata):
    if kata == kata[::-1].lower():
        print(f"{kata} adalah palindrome")
    else:
        print(f"{kata} bukan adalah palindrome")

palindrome("level")
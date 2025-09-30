#Mode Skrip
#Menghitung Luas Segitiga

#Mendeklarasi Variabel
alas = int(input("Masukkan alas:   "))
tinggi = int(input("Masukkan tinggi:  "))

#Membuat fungsi
def hitung():
	luas = 0.5 * alas * tinggi
	return luas

#Program utama
def main():
	print("Luas Segitiga:", hitung())
main()

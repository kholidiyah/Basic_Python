#Paradigma Pemrograman:
#Paradigma Imperatif
#Paradigma Prosedural
#Paradigma Fungsional
#Paradigma Terstruktur
#Paradigma Deklaratif(Prediktif)
#Paradigma Berorientasi Objek
#Paradigma Konkruen

##Paradigma Sekuensial
##Proses 1 --> Proses 2 --> Proses 3

#Mendeklarasi variabel
nim = str(input("Masukkan NIM \t:   "))
nama = str(input("Masukkan Nama \t:   "))
uts  = int(input("Masukkan UTS \t:   "))
tugas = int(input("Masukkan Tugas \t:   "))
uas = int(input("Masukkan UAS \t:   "))

#hitung total nilai
total = (uts/100*30) + (tugas/100*20)  + (uas/100*50)

#tampikan hasil
print("Total Nilai \t:"   ,total)

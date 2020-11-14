'''INTRO TO PYTHON'''

# # Fungsi print adalah mencetak sesuatu
print('Hello world') #Hello world



nama = "Sarah" 
umur = 25 
pekerjaan = "karyawan"
tinggi = 160
jomblo = False 

print(nama) #Sarah
print(umur) #25
print(pekerjaan) #karyawan
print(tinggi) #160 #tapi boong
print(jomblo) #False

print(type(nama)) #<class 'str'>
print(type(umur)) #<class 'int'>
print(type(pekerjaan)) #<class 'str'>
print(type(jomblo)) #<class 'bool'> #hanya False dan True (F dan T harus kapital)

nama = input('what is your name: ') #Input from user: rahe

###Jika menggunakan + jangan lupa menambah spasi dalam string (type data harus sama)
print('Hello my name is ' + nama + '.' +' I am ' + str(25) + ' years old.')
#Hello my name is rahe. I am 25 years old.

#Jika menggunakan , tidak perlu ditambah spasi
print('Hello my name is', nama,'.', 'I am', 25, 'years old.') 
#Hello my name is rahe . I am 25 years old.

nama = 25
print(nama) #25




'''Flow code itu WATER FLOW, mengcompile dari atas ke bawah secara berurutan.'''


'''ARITHMETIC OPERATOR'''
print(2+1) #3 #penjumlahan
print(2-1) #1 #pengurangan
print(3*2) #6 #perkalian
print(4/2) #2.0 #pembagian dengan hasil=>float
print(5/2) #2.5
print(4//2) #2 #pembagian dengan hasil=> integer
print(5//2) #2 #pembagian pembulatan ke bawah
print(5%2) #1 #modulo => hasil sisa pembagian
print (2 ** 3) #8 #pangkat/power

'''PYTHON TYPE CONVERSION'''
x = '10' #masih str
print(type(x)) #<class 'str'>
y = int(x) #diubah menjadi intr
print(type(y)) #<class 'int'>

#bisa dimasukkan ke dalam variabel
a = 23
a_str=str(a)
print(type(a_str)) #<class 'str'>

#bisa langsung diprint
b = 1.5
print(str(b)) #1.5

#float + int = float (implicit type conversion)
c = '2' 
print(float(c)+10) #12.0


'''INPUT'''
#ketika menggunakan input, datatypes yang  kita terima selalu dalam bentuk string
nama = input('What is your name: ') #input nama rahe. What is your name: rahe
umur = input('Input your age: ') #input umur 25. Input your age: 25
print ('Halo nama saya', nama, 'umur saya lima tahun kedepan adalah', int(umur)+5)
#Halo nama saya rahe umur saya lima tahun kedepan adalah 30

'''IMPORT LIBRARY'''
import math #cara1
#import math as m #untuk mempersingkat kedepannya (jadi nulisnya nanti m.sqrt)

print(math.pi) #3.141592653589793 #pi
print(math.fabs(-4.7)) #4.7 #nilai absolut dan return float
print(math.pow(2,4)) #16.0 #mencari pangkat dari suatu bilangan
print(math.sqrt(16)) #4.0 #akar
print(math.ceil(2.5)) #3 #membulatkan float ke atas
print(math.floor(2.5)) #2 #membulatkan float ke bawah
print(round(2.12545, 2)) #2.13 #membulatkan keatas float 2angka dibelakang koma

from math import pi, fabs, pow, sqrt, ceil, floor #cara 2 panggil library dan memanggil bbrp function yg dibutuhkan saja
print(pi) #3.141592653589793


'''STRING'''
x = "Halo dunia lain"
print(x) #Halo dunia lain #memprint
print(type(x)) #<class 'str'> #mengetahui tipe data
print(len(x)) #15 #mengetahui banyak elemen
print(x.index('a')) #1 #mengetahui keberadaan/index, index dimulai dari 0. Tapi diliatnya hanya yg paling pertama doang
print(x.split()) #['Halo', 'dunia', 'lain'] #memisah tiap kata berdasarkan sesuatu yg didalam kurung (spasi) dan dijadikan ke dalam list
print(x.split('d')) #['Halo ', 'unia lain'] #memisah tiap kata berdasarkan huruf d
print(x.lower()) #halo dunia lain #mengubah menjadi huruf kecil
print(x.upper()) #HALO DUNIA LAIN #mengubah menjadi huruf besar
print(x.capitalize()) #Halo dunia lain #kapital awal kalimat
print("halo dunia lain" .capitalize()) 
print(x.replace('dunia', 'apa')) #Halo apa lain #mereplace 


'''INDEXING & SLICING'''
#Indexing and slicing dari Halo dunia lain, error ketika jika nulis jumlah x lebih dari huruf
print(x[0]) #H
print(x[4]) #  #ada spasi di index ke empat
print(x[-1]) #untuk mencari secara cepat huruf paling terakhir

#slicing mengambil subset atau irisan (perlu x+1)
#format(X[start:stop])
print(x[0:4]) #Halo #mengambil kata halo, kenapa lima karena slicing itu x+1
print(x[5:]) #dunia lain #mengambil kata dari kelima sampai habis
print(x[x.index('d'):]) #dunia lain
print(x[:11]) #Halo dunia #kalo titik duanya dikiri, berarti diartikan huruf dari awal
print(x[:-4]) #Halo dunia

# (x[start:stop:step]) #step itu buat lompat dan reverse/gaknya
print(x[0:15:2]) #Hl ui an
print(x[::-1]) #nial ainud olaH #semuanya keambil tapi reverse
print(x[-1:-5:-5]) #n 


##HW1
x=4
y=3
z=2
w=(((x+y*z)/(x*y))**z)
print(w) #0.6944444444444445

##HW2
'''Silahkan masukkan angka berapapun :4
kuadrat dari 4 = 16'''

angka = input('Silahkan masukkan angka berapapun: ')
print(angka)
kuadrat = int(angka)**2
print('kuadrat dari ', angka, '=', int(kuadrat))

# Silahkan masukkan angka berapapun: 4
# 4
# kuadrat dari  4 = 16


##HW3
x= 485
y= 30
z=360
tahun=(x//z)
bulan=((x%z)//y)
hari=(x%y)
print('485 hari =', tahun, 'tahun', bulan, 'bulan', hari, 'hari')
#

##HW4
'''Saat ini jumlah usia andi dan budi = 49tahun
rasio usia andi dan budi = 0.4
berapa usia andi dan budi 2 tahun lagi?'''
Budi=(49/1.4)
Andi= 49 - Budi
print('usia andi dua tahun lagi', int(Andi)+2, 'usia budi dua tahun lagi', int(Budi)+2)
#usia andi dua tahun lagi 16 usia budi dua tahun lagi 37

#HW5
'''Buatlah algoritma untuk menghitung karakter dalam string
Halo Dunia memiliki huruf 'a' sebanyak 2.'''
x = 'Halo Dunia'
print(x.count('a')) #2

##HW5
word = input('Masukkan kata / kalimat:').lower()
cari = input(f"Input huruf yang ingin dicari jumlahnya dari '{word}': ").lower()
word2 = word.replace(cari, '')
print(f'huruf {cari} ada {len(word)-len(word2)} buah')

# Masukkan kata / kalimat:RAHETINGGI
# Input huruf yang ingin dicari jumlahnya dari 'rahetinggi': G
# huruf g ada 2 buah


#HW6
'''Jarak mobil A & B =120km.
A berjalan 60km/h dari timur.
B berjalan 40km/h dari barat.
A&B start pukul 9 wib.
Jam berapa A&B bertabrakan?'''

import math

S = 120
va = 60
vb = 40
t = S/(va+vb)
m = int((t*60)%60)
pukul= 9+math.floor(t)
print('Mobil A dan B bertabrakan pada pukul ', pukul, 'lewat', m, 'menit')

#Mobil A dan B bertabrakan pada pukul  10 lewat 12 menit
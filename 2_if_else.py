'''IF ELSE'''

x = 5 #int
y ='5' #str
z = 6 #int

# conditional statement
print(x == float(y)) #sama dengan
print(x == z)
print(x != z) #tidak sama dengan
print(x > z) #lebih besar
print(x < z) #lebih kecil / small than
print(x >= int(y)) #lebih besar sama dengan
print(x <= z) #lebih kecil sama dengan


#menggabungkan dua atau lebih conditional
# pake and atau or

# false and true = false
print(x==z and x < z)

#     false or true = true
print(x==z or x < z)


## rules AND
# T and T = T
# T and F = F
# F and T = F
# F and F = F

##Rules OR
# T or T = T
# T or F = T
# F or T = T
# F or F = F

# not untuk mereverse kondisi
print(not(5>6)) #false harusnya, tapi ditambah not jadi true

nilai = int(input('Masukkan nilai siswa: '))
# nilai 60 karena 60 >= 80 false, jadi lgsg ke else
if nilai >= 80:
    print('Murid Lulus')
else:
    print('Murid harus remedi')

nilai = int(input('Masukkan nilai siswa: ')) #75
#75 >= 80 false and 75<= 100 true = false
if nilai >=80 and nilai <=100:
    print('A')
#karena diatas false, pindah ke elif
# 75 >= 70 true and 75<80 true = true
elif nilai >= 70 and nilai < 80:
    print('B')
else:
    print('C')

# Masukkan nilai siswa: 65
# Murid harus remedi

# buatlah sebuah program sederhana untuk menentukan angka tsb genap atau ganjil
angka = int(input('Masukkan angka: '))
if angka % 2 == 0:
    print('Bilangan', angka, 'adalah bilangan genap')
else:
    print('Bilangan', angka, 'adalah bilangan ganjil')

##Buatlah indeks masa tubuh
berat = int(input('Berat badan anda dalam kg:'))
tinggi = int(input('Tinggi anda dalam cm:'))
imt = ((berat / tinggi) / tinggi)*10000
print(f"Massa anda {berat} kg dan tinggi anda {tinggi} cm")

if imt < 18.5:
    print('Berat badan anda kurang')
elif imt >= 18.5 and imt <= 24.9:
    print('Berat badan anda ideal')
elif imt >= 25 and imt <= 29.9:
    print('Berat badan anda berlebih')
elif imt >= 30 and imt <= 39.9:
    print('Berat badan anda sangat berlebih')
else:
    print('anda obsesitas')


##EXECISE####
#1
pisang = int(3000)
beli = int(input('Jumlah pisang yang kamu beli:'))
harga = int(pisang * beli)

if harga > 100000:
    print('Total belanja anda adalah', int(harga*0.9), 'IDR')
elif harga < 100000 and harga >= 50000:
    print('Total belanja anda adalah', int(harga*0.95), 'IDR')
else:
    print('Total belanja anda adalah', int(harga))

# 2
Gaji = int(input('Berapa gaji anda:'))
YOS = int(input('Year of Service:'))
Total_gaji = int(Gaji*1.10)

if YOS > 10:
    print('Selamat anda mendapat bonus! Total Gaji anda IDR', Total_gaji)
else:
    print('Kasian deh belum dapat bonus. Gaji anda tetap', Gaji)

#3
umur_user1 = int(input('Umur user 1:'))
umur_user2 = int(input('Umur user 2:'))
umur_user3 = int(input('Umur user 3:'))

if umur_user1 > umur_user2 and umur_user1 > umur_user3:
    print('User 1 adalah yang paling tua')
elif umur_user2 > umur_user1 and umur_user2 > umur_user3:
    print('User 2 adalah yang paling tua')
elif umur_user3 > umur_user1 and umur_user3 > umur_user1:
    print('User 3 adalah yang paling tua')
else:
    print('Tidak ada yang lebih tua')


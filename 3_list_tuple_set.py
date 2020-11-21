'''LIST'''

x = ['angin', 'bulan', 'cuaca', 'denah']

print(x)
print(type(x))

##Indexing = mengambil indeks atau memanggil value
#Indeks dimulai dari 0

# memanggil indeks ketiga (dari depan)
print(x[3]) #denah
x = ['angin', 'bulan', 'cuaca', 'denah']
     #   0       1        2        3


#memanggil indeks ketiga (dari belakang)
print(x[-3]) #bulan
# x = ['angin', 'bulan', 'cuaca', 'denah']
#        -4        -3       -2      -1

#Jika indexing lebih dari indexnya akan error

#Slicing = mengambil satu atau lebih value 
#value start selalu ada, tetapi value stop tidak pernah ikut
#jadi selalu +1 pada stop
#Jika slicing lebih dari indexnya tidak akan error

#[start : stop]
print(x[0:1]) #['angin']
print(x[ : 3]) #['angin', 'bulan', 'cuaca']

#[start : stop : step]
print(x[0:4:2]) #['angin', 'cuaca']


##MODIFY = mengubah value dalam list
x[1] = 'Bumi'
print(x) #['angin', 'Bumi', 'cuaca', 'denah']

##APPEND = ADD ITEM TO THE END OF A LIST (menambahkan satu elemen di posisi paling belakang, bisa satu list dalamnya byk jadi list dalam list)
x.append('Earth') #['angin', 'Bumi', 'cuaca', 'denah', 'Earth']
print(x)

x.append(['Pluto', 'Mars']) 
print(x) #['angin', 'Bumi', 'cuaca', 'denah', 'Earth', ['Pluto', 'Mars']]

#cara memanggil kata 'Pluto':
print(x[5][0])

##DEL = REMOVE ITEMS FROM A LIST
del x[2] #['angin', 'Bumi', 'denah', 'Earth', ['Pluto', 'Mars']]
print(x)

#[start : stop]
del x[-1:] 
print(x) #['angin', 'Bumi', 'denah', 'Earth']

# #EXTEND = memasukkan beberapa element sekaligus di belakang
# # (hasilnya berupa element tapi saat extend function nulisnya list)
x.extend(['Peta', 'Rotasi', 'Sungai']) #['angin', 'Bumi', 'denah', 'Earth', 'Peta', 'Rotasi', 'Sungai']
print(x)

#cara lain extend
y = ['Meander', 'Gerhana']
x.extend(y)
print(x) #['angin', 'Bumi', 'denah', 'Earth', 'Peta', 'Rotasi', 'Sungai', 'Meander', 'Gerhana']

# #IN =  mengecek suatu apakah element tertentu ada di dalam sebuah list (hasilnya boolean)
print('denah' in x) #True
print('Abrasi' in x) #False


#INSERT = memasukkan satu value (bisa satu list) di index tertentu
#misalnya di insert di index ke satu, sisanya mundur
x.insert(1, 'Bumi') #['angin', 'Bumi', 'Bumi', 'denah', 'Earth', 'Peta', 'Rotasi', 'Sungai', 'Meander', 'Gerhana']
print(x)

# #LEN = mengetahui banyak element
print(len(x)) #10


# #POP = Mengambil satu value (bisa recall) dan remove value dari list (dibutuhkan index value untuk func)
y = x.pop(2) ##hasil pop di recall
print(y) #Bumi

x.pop(2) 
print(x) #['angin', 'Bumi', 'Earth', 'Peta', 'Rotasi', 'Sungai', 'Meander', 'Gerhana']

x.pop() #kalo kurung kosong, auto pop list paling belakang
print(x) 


# #REMOVE = remove satu value dari list (dibutuhkan value untuk func)
x.remove('Meander')
print(x) #['angin', 'Bumi', 'Earth', 'Peta', 'Rotasi', 'Sungai']

# #REVERSE = Reverse the items in a	list
x.reverse() #['Sungai', 'Rotasi', 'Peta', 'Earth', 'Bumi', 'angin']
print(x)

# #SORT = mengurutkan secara alfabet atau numerik (PR sais reverse True or False)
x.sort() #['Bumi', 'Earth', 'Peta', 'Rotasi', 'Sungai', 'angin']
print(x)

# cara lain (harus ada reverse = True or False)
x.sort(reverse = True) #mereverse
print(x)

# #COUNT
# count = menghitung ada berapa element tertentu dalam sebuah list
print(x.count('Peta')) #1
x.append('Peta') 
print(x.count('Peta')) #2
print(x) #['angin', 'Sungai', 'Rotasi', 'Peta', 'Earth', 'Bumi', 'Peta']


# #BROADCASTING = cara mengganti beberapa element sekaligus
x[2:4] = 'Cicak', 'Domba' #['angin', 'Sungai', 'Cicak', 'Domba', 'Earth', 'Bumi', 'Peta']
print(x)
x[0], x[2] = 'Duren', 'Jeruk' #['Duren', 'Sungai', 'Jeruk', 'Domba', 'Earth', 'Bumi', 'Peta']
print(x)


##COPY = membuat copy dari list
#jika menggunakan copy
x_copy = x.copy()
print(x_copy)

x_copy.pop()
print(x_copy)
print(x) #tidak akan terdampak oleh pop dari x_copy

#jika menggunakan sama dengan
x2 = x
print(x2)

x2.pop()
print(x2) 
print(x) #terdampak oleh pop dari x_copy karena sama dengan (=) bukan copy

#INDEX = mengetahui index dari sebuah elemen tertentu
print(x.index('Duren')) #0


##ADDITION OPERATOR (+) = menggabungkan atau menambah list
##nambah beberapa value di belakang namun tidak menjadi list dalam list (dan tidak mempengaruhi list asli)
print(x + ['Soil', 'Land'])
print(x)
##hampir sama kayak extend, tapi ini tidak mempengaruhi variabel asli

##MULTIPLICATION OPERATOR (*) 
# menduplikasi value di dalam satu list (dan tidak mempengaruhi list asli)
print(x*3) 

'''
##EXERCISE PR

#soal1
# #Berapa index huruf y dari toyota
# print(mobil[0].index('y'))


#soal2
# print(mobil[0].index('y'))
# print(mobil[mobil.index('Mercedes')].index('s'))
# #     mobil[0].index('y')
# #     'Toyota'.index('y')
'''

####TUPLE#### 
#menggunakan kurung ( )
# sangat terbatas dan gabisa diubah elementnya (Fix data)
# contoh penggunaan tuple di nomer kartu kredit
# tuple bisa dimasukkan ke dalam list

angka = (1,2,3,4,5,6,7,2,2)

print(type(angka)) #<class 'tuple'>

#INDEX
print(angka[3]) #4
# print(angka[11]) #error karena lebih dari indexnya

#SLICE
#[start : stop ]
print(angka[0:3]) #(1, 2, 3) hasilnya tuple

#[start : stop : step]
print(angka[0:7:2]) #(1, 3, 5, 7) hasilnya tuple

#IN = mengecek suatu apakah element tertentu ada di dalam sebuah tuple (hasilnya boolean)
print(7 in angka) #True
print(10 in angka) #False

#LEN = mengetahui banyak elemen
print(len(angka)) #9

#ADDITION OPERATOR (+) : menggabungkan atau menambah tuple
##nambah beberapa value di belakang dan tidak mempengaruhi tuple asli
print(angka + (24, 27, 30, 100)) #(1, 2, 3, 4, 5, 6, 7, 2, 2, 24, 27, 30, 100)

#tidak mempengaruhi tuple asli
print(angka) #(1, 2, 3, 4, 5, 6, 7, 2, 2)

#MULTIPICATION OPERATOR (*)
# menduplikasi value di dalam satu tuple (dan tidak mempengaruhi tuple asli)
print(angka*2) #(1, 2, 3, 4, 5, 6, 7, 2, 2, 1, 2, 3, 4, 5, 6, 7, 2, 2)

#tidak mempengaruhi tuple asli
print(angka) #(1, 2, 3, 4, 5, 6, 7, 2, 2)

#COUNT = menghitung element tertentu
print(angka.count(2)) #3

kata = ('python forever')
print(kata.count('o')) #2

#Tuple bisa dijadikan list
#jika perlu ada value yg diubah
angka_list = list(angka) #[1, 2, 3, 4, 5, 6, 7, 2, 2]
print(angka_list)
#jika sudah fix, bisa dikembalikan ke tuple
back_to_tuple = tuple(angka_list) #(1, 2, 3, 4, 5, 6, 7, 2, 2)
print(back_to_tuple)



###SET### = kurung kurawal #mutable tapi non ordered

#Satu set adalah grup elemen unik yang tidak diurutkan (non ordered)
#gabisa duplicate value (kalo valuenya double, saat diprint cuma satu)
# Set digunakan untuk menjalankan operasi matematika yang melibatkan himpunan seperti intersection, union
# Satu set dapat berisi tipe data yg berbeda seperti float, tuple, string / integer. Namun tidak bisa dict, list dan set
z = {1,2,3,1,2,3} #<class 'set'>
print(type(z))

z2 = {} #<class 'dict'>
print(type(z2))



#INDEX ==> set gabisa index karena set tidak memperhatikan urutan (non ordered)
#SLICE ==> set gabisa index, apalagi slice karena tidak memperhatikan urutan

#LEN = mengetahui banyak element
print(len(z)) #3 (karena kalau set, duplicate value tidak dihitung)

#MAX = mengetahui nilai terbesar dalam set
print(max(z)) #3

#MIN = mengetahui nilai terkecil dalam set
print(min(z)) #1

#SUM = menjumlah value dalam set
print(sum(z)) #6

#ADD = menambah satu element baru di belakang
z.add(5) #{1, 2, 3, 5}
print(z)
z.add('Budi') #{1, 2, 3, 'Budi'}
print(z)

# #UPDATE = menambah beberapa element sekaligus di belakang, dan urutan elemen baru yg ditambahkan tidak diperhatikan
# tapi harus memasukkan datanya dalam bentuk itterable (list, tuple, set, string(akan dipecah kalo string))

#menambah element pake list bisa
z.update([7, 8, 'Andy','Caca']) #{1, 2, 3, 'Caca', 'Andy'}
print(z) 

#menambah element pake tuple bisa
z.update(('Andy','Caca')) #{1, 2, 3, 'Caca', 'Andy'}
print(z)

z.update('Andy') #{1, 2, 3, 'd', 'n', 'A', 'y'} 
print(z) #set tidak memperhatikan urutan (update khusus alfabet dia akan pecah per huruf)


# # DISCARD = menghapus 1 element tertentu, dengan input element yg mau dihilangkan di function
#tidak akan ERROR jika elemen yg diinput tidak ada, hanya print set asli
z.discard(3) #{1, 2}
print(z)

z.discard(8) #{1, 2} #TIDAK ERROR, HANYA TETAP
print(z)


##REMOVE = menghapus 1 element tertentu, dengan input element yg mau dihilangkan di function
#akan ERROR jika elemen yg diinput tidak ada
z.remove('d') #{1, 2}
print(z)

# z.remove(8) #ERROR 
# print(z)

# #POP = Mengambil satu value (bisa recall) dan remove value secara random
# z.pop() #{2, 3}
# print(z)

# z.pop() #{3}
# print(z)

# #CLEAR = menghapus semua element di dalam set
z.clear() #{}
print(z)

#IN and NOT IN = untuk mengecek ada tidaknya item di dalam set, hasl berupa boolean
print(2 in z ) #False
print(2 not in z)  #True 


#GABUNGAN SET
a_set = {1, 3, 4, 5, 7, 8, 9}
b_set = {2, 4, 5, 6, 8, 9, 10}
print(a_set, b_set) #{1, 3, 5, 7, 9} {2, 4, 6, 8, 10}

##SET OPERATION##

#GABUNGAN ATAU UNION = gabungan dari semua himpunan elemen
#Hasilnya adalah kombinasi dari semua elemen yang dikembalikan dalam urutan dari kecil ke besar (jika numeric).
print(a_set.union(b_set))
print(a_set|b_set)
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}


#IRISAN ATAU INTERSECTION = value yang sama dari kedua set
print(a_set.intersection(b_set))
print(a_set&b_set)
#{8, 9, 4, 5}

#SELISIH ATAU DIFFERENCE = value yang ada di satu set, namun tidak ada di set lain
print(a_set.difference(b_set)) #{1, 3, 7}
print(a_set-b_set)
#{1, 3, 7}

print(b_set.difference(a_set))
print(b_set-a_set)
#{2, 10, 6}


#BEDA SETANGKUP / SYMMETRIC DIFFERENCE
print(a_set.symmetric_difference(b_set))
print(a_set^(b_set))
#{1, 2, 3, 6, 7, 10}


########
#kegunaan tuple = mencegah perubahan element
#kegunaan set = lebih dipake untuk diagram vent

'''
#BUATLAH SET
# Buat lah set:
p = {1,2,4,7,9,19}
q = {5,12,16,17,7,9,19,6}
r = {19,6,3,8}

# 1. tentukan gabungan P dengan Q
# print(p|q) #{1, 2, 4, 5, 6, 7, 9, 12, 16, 17, 19}

# 2. tentukan gabungan P dengan R
# print(p|r) #{1, 2, 3, 4, 6, 7, 8, 9, 19}

# 3. tentukan gabungan Q dengan R
# print(q|r) #{3, 5, 6, 7, 8, 9, 12, 16, 17, 19}

# 4. tentukan irisan dari gabungan P dengan Q dan gabungan Q dengan R
# print((p|q)&(q|r)) #{5, 6, 7, 9, 12, 16, 17, 19}

# 5. tentukan symmetric difference dari gabungan Q dengan R dan gabungan P dengan Q
# print((q|r)^(p|q)) #{1, 2, 3, 4, 8}
'''


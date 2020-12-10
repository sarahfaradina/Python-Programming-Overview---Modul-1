'''LAMBDA'''
# adalah anonim function alias tidak perlu bikin nama function (tidak seperti def)
# harus bikin variabel dan pakai keyword lambda
# hanya bsa 1expression tapi bisa banyak argument
# Fungsi lambda biasanya digunakan ketika fungsi tanpa nama diperlukan dalam jangka pendek

# format:
#  lambda arguments:expression

square = lambda x, y : x*y    #lambda tetapi harus dibikin variabel   
print(square(2,3))   # x dan y adalah argumen, x*y adalah expression
#6

#jika menggunakan function
def perkalian(a, b):  
    print(a*b)
perkalian(2,3) #6


y = lambda a,b,c : (a/b)*c
print(y(1,2,3)) #1.5

#jika bikin else if di dalam lambda
z = lambda a: 'Genap' if a%2 == 0 else 'Ganjil'
print(z(4)) #Genap
print(z(3)) #Ganjil

#kapan memakai lambda? jika membuat function sederhana.
#jika function sudah ribet maka pakai def saja.


#contoh lambda dimasukkan ke dalam def (bisa)
def penjumlahan(a,b):
    y = lambda a, b : a+b
    return lambda a, b : a+b

print(penjumlahan(1,2))


##LAMBDA FUNCTION WITH MAP() 
#Fungsi map () Python mengambil daftar dan fungsi lain. 

name_list = 'Andi Budi Caca'.split()

# #kalo map dengan lambda
len_list2 = list(map(lambda a: len(a), name_list))
print(len_list2) #[4, 4, 4]

# #contoh lain jika function diganti jadi halo
def function(a):
    return f'halo {a}'

len_list = list(map(function, name_list))
print(len_list)
#['halo Andi', 'halo Budi', 'halo Caca']

# #bisa dilakukan di dua list sekaligus di dalam map

list_1 = 'cokelat melon nangka'.split()
list_2 = [10000, 5000, 20000]
couple_list = list(map(lambda a, b: a + str(b), list_1, list_2))
print(couple_list)
# ['cokelat10000', 'melon5000', 'nangka20000']


##FILTER## (returnnya hanya bisa True atau False)

# #kalo filter dengan lambda
#(mencari nilai yg sama di dua buah list)
k = [1,2,3,4,5]
l = [1,2,6,7,8]

m = list(filter(lambda a: a in k, l)) #[1, 2]
print(m) 


## REDUCE
# from functools import reduce

numbers = [6,2,3,4,5]
numbers_sum = reduce(lambda a,b: a*b, numbers)
print(numbers_sum) #720

kata = ['ini', 'ibu', 'budi']
o = reduce(lambda a,b: a+b, kata)
print(o) #iniibubudi

##LATIHAN
'''
Pakai map dan lambda
input = [2,4,6,8]
output = [4,16,36,64]
'''
# input_angka = [2,4,6,8]
# zz = list(map(lambda a: a**2, input_angka))
# print(zz)


# ##QUIZZ
'''
quiz poin 1
words_list = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']
what do you want to search: 'me'
output = ['merdeka', 'merah']
what do you want to search: 'ri'
output = ['kari ayam']
what do you want to search: 'tw'
output = []
'''
# word = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah']

# cari=str(input('Masukan huruf Anda: '))
# hasil = filter(lambda a: cari in a, word)
# print(list(hasil))

'''
Quiz
input = [1-100]

output = 5100

[1,2,3,4]
[2,4]
[4,8]
12
rules = bilangannya genap semua, dikalikan 2, baru dijumlah semua.
clue = pakai reduce, filter dan map.
challenge = kalo bisa cuman 1 line. # poin 3
kalo lebih dari 1 line, poinnya 2 
'''


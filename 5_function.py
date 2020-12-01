'''FUNCTION'''

#FUNCTION = kode yang sudah ditulis yang melakukan tugas tertentu
#bisa digunakan berulang kali dan bertujuan untuk memudahkan dan mengurangi pengulangan

#function dibagi dua tipe:
# 1. built in (sudah disediakan oleh python)
# 2. user-defined(dibuat oleh user sesuai dengan syntax python)


#USER-DEFINED

#Format:
#def function_name(parameters):

#satu blok kode function, terdiri dari:
# 1. def keyword : menunjukkan awal fungsi dimulai
# 2. function name: menamakan fungsi dgn unik, karena akan dipakai selanjutnya
# 3. parameter   : digunakan untuk memasukan value dan ditulis dalam tanda kurung (opsional) 
# 4. titik dua   : tanda mengakhiri fungsi yg dibuat
# 5. docstring   : docstring komponen opsional yang biasanya digunakan untuk
#                jelaskan apa fungsinya. Ditulis di line bawah def (printnya => print(functionname.__doc__)) 
# 6. statements  : badan fungsi terdiri dari satu atau lebih pernyataan
# 7. Return statement : mengembalikan nilai dari suatu fungsi. 
#                       Jika tidak ada return dalam fungsi, maka jika di print 'None', bisa lebih dari satu return bisa


# FUNCTION TANPA PARAMETER
def hello(): #bikin dulu definitionnya
    print("Hello world!")
hello()   #panggil


# FUNCTION TANPA PARAMETER
def power(): #9
    print(3**2)
power() #panggil function

# FUNCTION 1 PARAMETER
def power2(x):      #memasukkan parameter x di def
    print(x**2)   

power2(4)  # 16  #pas panggil harus nulis argument

#cara print dalam variabel gabisa
hasil = power2(4)
print(hasil) #none

# jadi kalo mau print (tambahain return di def)
def power2(x): #pakein x di def
    print(x**2)
    return(x**2) #mengembalikan hasil agar bisa dipakai di variabel atau disimpan

hasil = power2(4)
hasil

##return = mengembalikan hasil agar bisa digunakan kembali

#FUNCTION WITH A PARAMETER AND RETURN
def genap(angka):
    if angka % 2 == 0:
        return angka
    else:
        print('Bukan angka genap')

genap(21) #Bukan angka genap


# #FUNCTION 2 PARAMETER  (Tidak ada batasan jumlah parameter)
def power3(angka, pangkat):
    return angka**pangkat

hasil_power3 = power3(3,4)
print(hasil_power3)
#atau
print(power3(3,4))


##VARIABEL SCOPE
# Variabel yang ditentukan di dalam fungsi diperlakukan berbeda dari variabel yang ditentukan di luar. 
# Ada dua perbedaan utama.
#1.variabel lokal = variabel di dalam fungsi yg dapat diakses di dalam fungsinya
#2. variabel global = variabel di luar fungsi yg dapat diakses dimanapun dalam program
	


'''
#BUATLAH SEBUAH FUNCTION DENGAN NAMA CALCULATOR
'''

# kalo mau pake input  
angka1 = int(input('Angka pertama: '))
operasi = input('Masukkan operator(+,-,/,x,^): ')
angka2 = int(input('Angka kedua: '))

def calculator(angka1, operasi, angka2):
    if operasi == '+':
        print(f'Hasil penjumlahan dari {angka1} {operasi} {angka2} adalah {angka1+angka2}') 
    elif operasi == '-':
        print(f'Hasil pengurangan dari {angka1} {operasi} {angka2} adalah {angka1-angka2}')
    elif operasi == 'x':
        print(f'Hasil pengalian dari {angka1} {operasi} {angka2} adalah {angka1*angka2}')
    elif operasi == '/':
        print(f'Hasil pembagian dari {angka1} {operasi} {angka2} adalah {angka1/angka2}')
    elif operasi == '^':
        print(f'Hasil pemangkatan dari {angka1} {operasi} {angka2} adalah {angka1**angka2}') 
    else:
        print(f'Operator {operasi} tidak digunakan')


calculator(angka1, operasi, angka2)
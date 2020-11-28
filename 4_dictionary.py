'''DICTIONARY'''

#Dictionary adalah kumpulan data berpasangan (key-value) yang tidak berurutan
#satu dict dapat berisi berbagai tipe data
#satu dict tidak dapat berisi duplicate keys, tapi bisa duplicate value



#FORMAT
# dict = {
#   'keys' : 'value',
#   'keys' : 'value', 
#   'keys' : {
#       'keys dalam dict' : 'value dalam dict',
#       'keys dalam dict' : 'value dalam dict',
                #'keys dalam dict lagi' : {
                #   'keys : 'value',
                # }
#   }
# }


#wajib kurung kurawal
#wajib pake titik dua di antara keys dan value
#setiap pasangan key-value dipisahkan koma




employee = {
    'nama': 'Andy',
    'usia':20,
    'married': True,
    'Jabatan': 'Data Scientist',
    'kendaraan': ['mobil', 'motor'],
    'address':{   #bisa dict dalam dic
        'street': 'Jalan Mawar',
        'Nomor': 50,
        'geo':{ #bisa dict dalam dict dalamnya lagi dict
            'lat' : 12345.132132,
            'long': 12345.675545,
        }
    }
}    

print(employee)
# {'nama': 'Andy', 'usia': 20, 'married': True, 'Jabatan': 'IT Engineer', 'kendaraan': ['mobil', 'motor'], 'address': {'street': 'Jalan Mawar', 'RT': 5, 'RW': 2, 'Zipcode': 12345, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}} 

#INDEX&SLICE TIDAK ADA
# #memanggil value dengan keys, bukan index lagi
print(employee['nama']) #Andy
print(employee['kendaraan']) #['mobil', 'motor']
print(employee['kendaraan'][0]) #mobil (bisa pake index, karena kendaraan berupa list)
print(employee['address']['street']) #Jalan Mawar

#TYPE = mengetahui tipe data
print(type(employee)) #<class 'dict'>

#KEYS() = menampilkan daftar keys
print(employee.keys()) 
#dict_keys(['nama', 'usia', 'married', 'Jabatan', 'kendaraan', 'address'])
print(list(employee.keys())) #berupa list
#['nama', 'usia', 'married', 'Jabatan', 'kendaraan', 'address']

#VALUES() = menampilkan daftar values
print(list(employee.values())) 
#['Andy', 20, True, 'Data Scientist', ['mobil', 'motor'], {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}]  

#LEN = mengetahui jumlah item di dict
print(len(employee)) #6 (dict umum aja yg dihitung)


#GET = mengambil value melalui keys (karena dict gapunya index)
print(employee.get('nama')) #Andy
print(employee.get('gaji')) #none
print(employee.get('gaji', 'Key Not Found')) #kalo ini bisa dikasih pesan, jika keys tidak ada

#Operator (=)

#1. jika keys belum ada, maka akan ditambah sepasang keys-value di belakang
employee['gaji']= 2000000
print(employee)
#{'nama': 'Andy', 'usia': 20, 'married': True, 'Jabatan': 'Data Scientist', 'kendaraan': ['mobil', 'motor'], 'address': {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}, 'gaji': 2000000} 

#2. Jika keys sudah ada, makan value akan update sesuai keys 
employee['gaji'] = 3000000
print(employee)
#{'nama': 'Andy', 'usia': 20, 'married': True, 'Jabatan': 'Data Scientist', 'kendaraan': ['mobil', 'motor'], 'address': {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}, 'gaji': 3000000}


# UPDATE = menambah beberapa key dan value sekaligus
employee.update({'NIK': 92131231, 'BPJS': 10000002121})
print(employee)
#{'nama': 'Andy', 'usia': 20, 'married': True, 'Jabatan': 'Data Scientist', 'kendaraan': ['mobil', 'motor'], 'address': {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}, 'gaji': 3000000, 'NIK': 92131231, 'BPJS': 10000002121}

#menambah item dalam value
employee['kendaraan'].append('scooter')
print(employee)
#{'nama': 'Andy', 'usia': 20, 'married': True, 'Jabatan': 'Data Scientist', 'kendaraan': ['mobil', 'motor', 'scooter'], 'address': {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}, 'gaji': 3000000, 'NIK': 92131231, 'BPJS': 10000002121}


# ITEM = me-list pasangan value dan keys menjadi tuples (bisa buat looping)
print(employee.items())
#dict_items([('nama', 'Andy'), ('usia', 20), ('married', True), ('Jabatan', 'Data Scientist'), ('kendaraan', ['mobil', 'motor']), ('address', {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}), 
# ('gaji', 3000000), ('NIK', 92131231), ('BPJS', 10000002121)])
print(list(employee.items()))


print(employee['address']['geo'].items())
# dict_items([('lat', 12345.132132), ('long', 12345.675545)])


# IN = cari value apakah ada di dictionary atau tidak
print(3000000 in employee.values()) #True
print('sepeda' in employee.values()) #False


# POP = mengganti nama keys
employee['alamat'] = employee.pop('address')
print(employee)
#{'nama': 'Andy', 'usia': 20, 'married': True, 'Jabatan': 'Data Scientist', 'kendaraan': ['mobil', 'motor'], 'gaji': 3000000, 'NIK': 92131231, 'BPJS': 10000002121, 'alamat': {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}}


#menghapus sepasang value-keys, namun bisa dikembalikan
employee.pop('Jabatan')
print(employee)
#{'nama': 'Andy', 'usia': 20, 'married': True, 'kendaraan': ['mobil', 'motor'], 'address': 
# {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}}


#DEL = menghapus sepasang key-value
del employee['usia']
print(employee)
#{'nama': 'Andy', 'married': True, 'Jabatan': 'Data Scientist', 'kendaraan': ['mobil', 'motor'], 'address': {'street': 'Jalan Mawar', 'Nomor': 50, 'geo': {'lat': 12345.132132, 'long': 12345.675545}}}

#CLEAR = menghapus semua element dalam dict menjadi dict kosong
employee.clear() 
print(employee) #{}


#cari value terkecil atau terbesar di dalam dictionary
nilai_ujian = {
    'fisika': 82,
    'matematika':65,
    'sejarah':75
}

print(min(nilai_ujian, key=nilai_ujian.get)) #Matematika
print(max(nilai_ujian, key=nilai_ujian.get))  #Fisika
##kalo ada value yg sama berarti yg diambil itu pertama kali

#menggabungkan 2 dict
dict1 = {'Ten':10, 'Twenty': 20, 'Thirty':30}
dict2 = {'Forty':40, 'Fifty':50, 'Sixty':60}

# #cara1:
dict1.update(dict2)
print(dict1)
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50, 'Sixty': 60}

#cara2
dict3 = {'Ten':10, 'Twenty': 20, 'Thirty':30}
dict4 = {'Forty':40, 'Fifty':50, 'Sixty':60}

dict3_dict4 ={**dict3, **dict4}
print(dict3_dict4)
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50, 'Sixty': 60}

#membuat dictionary dari dua buah list
key = ['Ten', 'Twenty', 'Thirty']
value = [10, 20, 30]

sample_dict = dict(zip(key, value))
print(sample_dict)
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

### zip bisa untuk menyatukan antar iterable, beda jumlah keys dan value tidak apa-apa


# keys berupa list dan value berupa set bisa dijadikan dict. Initialize dictionary with default values
karyawan = ['Doni', 'Fiki', 'Akbar']
defaults = {'designation': 'Application Developer', 'salary': 5000000}

dict_full = dict.fromkeys(karyawan, defaults)
print(dict_full)
#{'Doni': {'designation': 'Application Developer', 'salary': 5000000}, 'Fiki': {'designation': 'Application Developer', 'salary': 5000000}, 'Akbar': {'designation': 'Application Developer', 'salary': 5000000}}

print(dict_full['Doni'])
#{'designation': 'Application Developer', 'salary': 5000000}


##DICTIONARY COMPREHENSION
#membuat dictionary dari looping
square = {x:x**2 for x in range (5)}
print(square)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

square2 = {x:x**2 for x in range (5) if x % 2 == 0}
print(square2)
#{0: 0, 2: 4, 4: 16}

'''
# No. 1
# Masukkan hari: Senin 
# output: bahasa inggris dari Senin adalah Monday
'''

days = input(str('Masukkan hari:')).lower()

dict_hari = {
    'senin' : 'monday',
    'selasa' : 'tuesday',
    'rabu' : 'wednesday',
    'kamis' : 'thursday',
    'jumat' : 'friday',
    'sabtu' : 'saturday',
    'minggu' : 'sunday',
}

if days in list(dict_hari.keys()):
    print(f'Bahasa inggris dari {days} adalah {dict_hari[days]}')
else:
    print('Invalid input')


'''
# No. 2
# Masukkan hari (INA/ENG): senin
# output: bahasa inggris dari senin adalah Monday

# Masukkan hari (INA/ENG): monday
# output: bahasa indonesia dari monday adalah Senin
'''

#CARA1
days = input('Masukkan hari (INA/ENG):').lower()
dict_hari = {
    'senin' : 'monday',
    'selasa' : 'tuesday',
    'rabu' : 'wednesday',
    'kamis' : 'thursday',
    'jumat' : 'friday',
    'sabtu' : 'saturday',
    'minggu' : 'sunday',
}

dict_hari2 = {
    'monday' : 'senin',
    'tuesday' : 'selasa',
    'wednesday' : 'rabu',
    'thursday' : 'kamis',
    'friday' : 'jumat',
    'saturday' : 'sabtu',
    'sunday' : 'minggu',
}

ina = list(dict_hari)
eng = list(dict_hari2)

if days in ina:
    print(f'Bahasa inggris dari {days} adalah {dict_hari[days]}')
elif days in eng:
    print(f'Bahasa indonesia dari {days} adalah {dict_hari2[days]}')
else:
    print('Kata yang anda masukkan bukan hari')



#CARA2
days = input(str('Masukkan hari (INA/ENG):')).lower()
dict_hari = {
    'senin' : 'monday',
    'selasa' : 'tuesday',
    'rabu' : 'wednesday',
    'kamis' : 'thursday',
    'jumat' : 'friday',
    'sabtu' : 'saturday',
    'minggu' : 'sunday',
}

ina = list(dict_hari.keys())
eng = list(dict_hari.values())

if days in ina:
    print(f'Bahasa inggris dari {days} adalah {dict_hari[days]}')
elif days in eng:
    print(f'Bahasa indonesia dari {days} adalah {ina[eng.index(days)]}')
else:
    print('Kata yang anda masukkan bukan hari')
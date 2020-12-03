#LOOPING = melakukan kerjaan yg sama berulang kali hingga statement tidak lagi valid
#hanya akan menjalankan code ketika kondisinya True
#dibagi menjadi while loops dan for loops


##FOR LOOP
# digunakan untuk mengulang iterable seperti list, string, atau tuple.
# Di pernyataan for, variabel 'val' menyimpan nilai setiap item pada urutan dengan setiap iterasi. 
# Perulangan berlangsung hingga semua elemen habis.

# format
# for variabel in sequence:  #pake titik dua
# 	    statement(s)

#FOR LOOP WITH STRING
for letter in 'Sarah':
    print(letter)
# S
# a
# r
# a
# h

# FOR LOOP WIRH LIST
weather = ['rainy', 'sunny']
for x in weather:
    print(f'its a {x} day')
print('Dress appropriately!')

# its a rainy day
# its a sunny day
# Dress appropriately!


#FOR LOOP WITH TUPLE
color = ('black', 'white', 'yellow')

for x in color:
    print(f'I am wearing {x} dress')
# I am wearing black dress
# I am wearing white dress
# I am wearing yellow dress

#FOR LOOP WITH THE RANGE() FUNCTION
# Fungsi range () dapat digunakan untuk memberikan angka yang dibutuhkan oleh sebuah loop

# for variabel in range (stop): 
for i in range (4):
    print(i)
# 0
# 1
# 2
# 3

# for variabel in range (start, stop, step):
x = 15
total = 0

for number in range (1, x+1):
    total += number

print(total) #120

##BREAK STATEMENT IN FOR LOOP
#ingin keluar dari keseluruhan loop ketika kondisi yg diinginkan telah terpenuhi
#kondisi setelah break, tidak diikutkan

animals = ['lion', 'ant', 'cow', 'bird']

for name in animals:
    if name == 'cow':
        break   #jadi bird gak ikut, karena di break dgn kondisi sampe cow aja
    print(f'cool animal : {name}')
print('Thats all amazing animals')

# cool animal : lion
# cool animal : ant
# Thats all amazing animals


# CONTINUE STATEMENT IN FOR LOOP
# melewati kondisi yg diinginkan, namun tetap melanjutkan hingga looping selesai

animals = ['lion', 'ant', 'cow', 'bird']

for name in animals:
    if name == 'cow':
        continue   #jadi cow di skip, dilanjutkan ke setelahnya
    print(f'cool animal : {name}')
print('Thats all amazing animals')

# cool animal : lion
# cool animal : ant
# cool animal : bird
# Thats all amazing animals


#WHILE LOOPS digunakan saat Anda perlu berulang kali mengeksekusi pernyataan saat true. 
# Ketika sudah false, looping akan berhenti.
#while loop rawan sekali terjadi infinity loop

#FORMAT:
# declare variable counter #berfungsi untuk  penghitung loop
#while condition:
    #statement(s)
    #valueback to counter #crucial line

i = 1  #line1 berpasangan dgn line4 sbg pembatas #variabelcounter
while i <= 4: #conditional statement
    print(i*2) #print
    i += 1 #update variabel ===> kalo line ini gak ditulis, dia akan ngeprint trs gak berenti
#jika sudah sampai i=4, maka i+1 sudah false. While akan berenti jika false

# 2
# 4
# 6
# 8

#Contoh lain:
i = 1 
while i <= 5: 
    if i <= 3: 
        print(i*2)
    else:
        print(i*3)
    i += 1 

# 4
# 6
# 12
# 15
# 18


''' 
Menggunakan while loop buatlah program sederhana,
ketika bertemu dengan angka ganjil, maka print angkanya.
ketika bertemu dengan angka genap, maka print "GENAP"
1-20
'''

i = 1
while i <= 20:
    if i%2 == 0:
        print('Genap')
    else:
        print(i)
    i += 1

'''
Password Attempt

No. 1
password = '12345'

case 1:
input = 23452
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 23423
'Try again later'

case 2:
input 12345
'Password Correct'

case 3:
input = 23452
'Password Incorrect'
input = 23423
'Password Incorrect'
input = 12345
'Password Correct'
'''

# password = '12345'
# attempt = 1
# while attempt <= 4: # 5 => False
#     input_password = input('Masukkan Password: ')
#     if input_password == password:
#         print('Password Correct')
#         break
#     else:
#         if attempt == 4:
#             print('Try Again Later!')
#             break
#         else:
#             if attempt == 3:
#                 print(f'Password Incorrect! You have {4-attempt} attempt left!')
#             else:
#                 print(f'Password Incorrect! You have {4-attempt} attempts left!')
#             attempt +=1

'''
# PRIME NUMBER
'''
# num = int(input('Enter a number: ')) #5

# if num > 1:
#     for i in range(2, num): 
#         if(num % i) == 0: 
#             print(f'{num} is not a prime number')
#             break
#     else: 
#         print(f'{num} is a prime number')
# else:
#     print(f'{num} is not a prime number')

'''
# PRIME NUMBER IN INTERVAL
'''
# lower = 800
# upper = 850

# print(f'Prime number from {lower} to {upper} are:')

# for num in range (lower, upper+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)

##Prime number from 800 to 850 are
# 809
# 811
# 821
# 823
# 827
# 829
# 839

'''
##FIND THE FACTORIAL OF NUMBER
'''
# num = int(input('Enter a number:'))
# factorial = 1

# if num < 0:
#     print('Sorry, factorial is not for negative number')
# elif num == 1:
#     print(num)
# else:
#     for i in range (1, num+1):
#         factorial = factorial*i
#     print(f'The factorial of {num} is {factorial}')

#Enter a number:5
# The factorial of 5 is 120

'''
##MULTIPLICATION TABLE
'''
# num = int(input('Enter a number:'))

# for i in range (100, 106):
#     print(f'{num} x {i} = {num*i}')

#10 x 100 = 1000
# 10 x 101 = 1010
# 10 x 102 = 1020
# 10 x 103 = 1030
# 10 x 104 = 1040
# 10 x 105 = 1050

'''
##Print First 10 natural numbers using while loop
'''
# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

'''
##Accept number from user and calculate the sum of all number between 1 and given number
##For example user given 10 so the output should be 55
'''
# sum = 0
# num = int(input('Enter a number: '))

# for i in range (1, num+1):
#     sum += i
# print(sum)
# #10 ===> 55

'''
##Exercise Question 4: Print multiplication table of given number
# For example num = 2 so the output should be
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
'''
#answer
# num = int(input('Enter a number: '))

# for i in range (1, 11):
#     print(i*num)

'''
# Exercise Question 5: Given a list iterate it 
# and display numbers which are divisible by 5 
# and if you find number greater than 150 stop the loop iteration
#expected output:
# 15
# 55
# 75
# 150
'''

# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# for i in list1:
#     if i > 150:
#         break
#     if i % 5 == 0:
#         print(i)
'''
Write a Python program to find those numbers which 
are divisible by 7 and multiple of 5, 
between 1500 and 2700 (both included)
'''

# for i in range (1500, 2701):
#     if i % 7 == 0 and i % 5 == 0:
#         print(str(i))

'''
 Write a Python program to convert temperatures to
 and from celsius, fahrenheit. Go to the editor
 [ Formula : c/5 = f-32/9 ]
 '''

# temp = input('Enter a number temp:   (ex:50F/50C)')
# degree = int(temp[:-1])
# # print(degree) #50
# conv = temp[-1]
# # print(conv) #F

# if conv.lower() == 'c':
#     result = round((9*degree)/5 + 32)
#     o_conv = 'Fahrenheit'
# elif conv.lower() == 'f':
#     result = round((degree - 32)*5/9)
#     o_conv = 'Celcius'
# else:
#     print('Input proper convention')

# print(f'The temperature in {o_conv} is {result} degree')

'''
Write a Python program to guess a number between 1 to 9.
'''
# import random

# target, guess = random.randint(0,10), 0
# while target != guess:
#     guess = int(input('Guess a number from 1 to 9, until get right: '))
# print('Well guessed!')

# guess = int(input('Guess a number from 1 to 9, until get right: '))

# target, guess = random.randint(0,10), 0

# while target != guess:
#     print('Lets try again!')
#     break
#  target == guess:
#     print('Well guessed!')

'''
# Exercise Question 6: Given a number count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.
'''
# num = 56789
# count = 0

# while num != 0:
#     num //= 10
#     count += 1
# print(count)


# atau

# num = input('Enter a number: ')
# num_count = len(num)
# print(num_count)


'''
##hasil
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
'''
# num = int(input('Enter a number:'))

# for i in range (1, num+1): 
#     for j in range (1, i+1):
#         print(j, end=' ')
#     print('')


'''
##kebalikannya
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
'''

# n = 5
# k = 5

# for i in range(0, n+1):
#     for j in range (k-i, 0, -1):
#         print(j, end=' ')
#     print()


'''
# Exercise Question 8: Reverse the following list using for loop
# list1 = [10, 20, 30, 40, 50]
# Expected output:
# 50
# 40
# 30
# 20
# 10
'''
# start = len(list1) - 1
# stop = -1
# step = -1
# for i in range (start, stop, step):
#     print(list1[i])

'''
# Exercise Question 9: Display -10 to -1 using for loop
'''
# for i in range (-10, 0):
#     print(i)
# # -10
# # -9
# # -8
# # -7
# # -6
# # -5
# # -4
# # -3
# # -2
# # -1

'''
# Exercise Question 10: Display a message “Done” 
# after successful execution of for loop
'''
# for i in range (5):
#     print(i)
# print('Done!')
# 0
# 1
# 2
# 3
# 4
# Done!


'''
##ENCRYPTION
'''
# kata = input('Enter a word: ')
# alfa = 'abcdefghijklmnopqrstuvwxyz'

# encrip = []

# for i in kata:
#     if i == 'y':
#         print('a')
#     elif i == 'z':
#         print('b')
#     elif i == ' ':
#         print(' ')
#     else:
#         encrip.append(alfa[alfa.index(i)+2])
# print(''.join(encrip))


'''
case 1
buat sebuah function untuk game fizz buzz!
function ini menerima 1 parameter.
ketika bertemu angka yang habis dibagi 3 maka dia akan print fizz [3,6,9,12]
ketika bertemu angka yang habis dibagi 5 maka dia akan print buzz [5,10,15,20,25]
ketika bertemu angka yang habis dibagi 3 dan 5 maka dia akan print fizz buzz [15, 30, 45]

contoh:
input : fizzbuzz(15)
output :
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
'''

# def fizzbuzz(x):
#     for i in range (1, x+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('fizzbuzz')
#         elif i % 3 == 0:
#             print('fizz')
#         elif i % 5 == 0:
#             print('buzz')
#         else:
#             print(i)

# fizzbuzz(15)



'''
case 2
tanpa membuat function, buatlah sebuah program untuk reversing namun menggunakan for loop
input = [1,2,3,4,5,6,7]

output = [7,6,5,4,3,2,1]

'''
# num = [1,2,3,4,5,6,7]
# num2 = []

# for i in range (1, len(num)+1):
#     num2.append(num[-i])
# print(num2) 
# ##[7, 6, 5, 4, 3, 2, 1]




'''
case 3 
PALINDROME
tanpa membuat function, buatlah sebuah program untuk mengecek apakah suatu kata palindrom atau bukan.
Palindrome: kondisi ketika suatu kata akan dieja sama, baik dieja dari depan maupun belakang.
contoh: "malam", dibalik juga "malam"
contoh: "kodok", dibalik juga "kodok"
contoh bukan palindrome: "kotak", dibalik jadi "katok"

input = malam
output = Is word malam a palindrome = True

input = malab
output = Is word malab a palindrome = False

input = kodok
output = Is word kodok a palindrome = True
'''

# kata = input('Enter the word: ')

# if kata == kata[::-1]:
#     print(f'{kata} is a palidrom')
# else:
#     print(f'{kata} is not a palidrom')

'''
case 4
buatlah sebuah function yang menerima 1 parameter, untuk membuat segitiga siku-siku menggunakan *

contoh:
segitiga_siku(5)

output =
 * 
 *  * 
 *  *  *
 *  *  *  *
 *  *  *  *  *
'''

# star = ''

# for i in range (6): 
#     star += ' * '
#     print(star)


'''
contoh:
segitiga_siku(7)

output = 
 * 
 *  *
 *  *  *
 *  *  *  *
 *  *  *  *  * 
 *  *  *  *  *  *
 *  *  *  *  *  *  * 
'''

# star = ''

# for i in range (8): 
#     star += ' * '
#     print(star)



'''
case 5

sama seperti case 4, cuman segitiganya dibalik
segitiga_siku_reversed(5)

output = 
 *  *  *  *  *
 *  *  *  *
 *  *  *
 *  *
 *
'''

# star = ''

# for i in range(x, 0, -1): # [7, 6, 5, 4, 3, 2, 1]
#         for j in range(0, i): # [0]
#             star += ' * '
#         star += '\n'
#     print(star)

'''
Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
# n = 5
# for i in range(n):
#     for j in range(i):
#         print ('* ', end="")
#     print('')

# for i in range(n,0,-1):
#     for j in range(i):
#         print('* ', end="")
#     print('')

'''
Write a Python program that accepts a word from the user and reverse it
'''
# kata = input('Enter a word: ')
# kata_dibalik = kata[::-1]

# print(f'{kata} dibalik menjadi {kata_dibalik}')

'''
Write a Python program to count the number 
of even and odd numbers from a series of numbers
'''
# even = 0
# odd = 0

# num = (1,2,3,4,5,6,7,8,9)

# for i in num:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print(f'Number of even number: {even}')
# print(f'Number of odd number: {odd}')

'''
Write a Python program that prints each item and 
its corresponding type from the following list.
'''
# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# for item in datalist:
#     print(f'Type of {item} is {type(item)}')

#answer:
# Type of 1452 is <class 'int'>
# Type of 11.23 is <class 'float'>
# Type of (1+2j) is <class 'complex'>
# Type of True is <class 'bool'>
# Type of w3resource is <class 'str'>
# Type of (0, -1) is <class 'tuple'>
# Type of [5, 12] is <class 'list'>
# Type of {'class': 'V', 'section': 'A'} is <class 'dict'>

'''
Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5
'''
# for i in range (7):
#     if i == 3:
#         continue
#     elif i == 6:
#         continue
#     else:
#         print(i, end = ' ')

# 0 1 2 4 5

'''
FIBONACI
Write a Python program to get the Fibonacci series between 0 to 50
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
'''
# x = 0
# y = 1

# while y < 50:
#     print(y, end=' ')
#     x,y = y, x+y

# 1 1 2 3 5 8 13 21 34

'''
ARMSTRONG NUMBER
programiz
'''

'''
##nomer11
Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1
'''
# row_num = int(input("Input number of rows: "))
# col_num = int(input("Input number of columns: "))
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# for row in range(row_num):
#     for col in range(col_num):
#         multi_list[row][col]= row*col

# print(multi_list)
'''
nomer12:
Write a Python program that accepts a sequence of lines (blank line to terminate) as input 
and prints the lines as output (all characters in lower case)
'''
# line = []

# while True:
#     a = input()
#     if a:
#         line.append(a.lower())
#     else:
#         break
# for a in line:
#     print(a)

'''
nomer13
'''

'''
nomer14
Write a Python program that accepts a string 
and calculate the number of digits and letters.
'''
# d = 0
# l = 0

# kata = input('Enter a word: ')

# for i in kata:
#     if i.isalpha():
#         l += 1
#     elif i.isdigit():
#         d +=1
#     else:
#         break
# print(f'Letter is {l}')
# print(f'Digit is {d}')

'''
nomer15
Write a Python program to check the validity of password input by users
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
'''
# import re
# p= input("Input your password")
# x = True
# while x:  
#     if (len(p)<6 or len(p)>12):
#         break
#     elif not re.search("[a-z]",p):
#         break
#     elif not re.search("[0-9]",p):
#         break
#     elif not re.search("[A-Z]",p):
#         break
#     elif not re.search("[$#@]",p):
#         break
#     elif re.search("\s",p):
#         break
#     else:
#         print("Valid Password")
#         x=False
#         break

# if x:
#     print("Not a Valid Password")
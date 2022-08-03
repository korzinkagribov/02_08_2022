import math
import random

per_one = 0
#Функция bin() преобразует целое число в двоичную строку с префиксом 0b.
print(bin(per_one))
print(pow(2, 2, 2))#c делением по мод
#элемент pow использует доп pow
print(pow(pow(2, 3), 2))
print(divmod(70, 9), "// - %")#// , % pair
some_num = 20
#print(--(some_num))
#bite
#|or
#^ decline or
#~ inversion
#>> << bite slide
print(~some_num)
print(some_num>>1)
print(some_num<<1)
print(some_num&20)
print(15&some_num)
print("-"*50)
print(some_num.bit_length())

print(((some_num*300)*300).to_bytes(10, byteorder='big'))

#oct - 16, hex - 8

print("Sq of Pi - ", math.sqrt(math.pi))

rand_number = random.random()

print(rand_number)

a_cmpx = complex(20, 80)
b_cmpx = complex(4, 10)
common_cmpx = a_cmpx + b_cmpx
print(common_cmpx, common_cmpx.imag, common_cmpx.real, common_cmpx.conjugate(), pow(common_cmpx.imag, common_cmpx))

def main_dunction():
    print("za")

main_dunction()
'''
задание 8
'''
type = input("Введите тип операции(+,-,*,/) - ")
number_1 = int(input("first number - "))
number_2 = int(input("second_number - "))
def plus(number_1,number_2):
    a = number_1 + number_2
    print(a)
def minus(number_1,number_2):
    a = number_1 - number_2
    print(a)
def delete(number_1,number_2):
    a = number_1 / number_2
    print(a)
def umn(number_1,number_2):
    a = number_1 * number_2
    print(a)
if type == ("+"):
    plus(number_1,number_2)
if type == ("-"):
    minus(number_1,number_2)
if type == ("/"):
    delete(number_1,number_2)
if type == ("*"):
    umn(number_1,number_2)



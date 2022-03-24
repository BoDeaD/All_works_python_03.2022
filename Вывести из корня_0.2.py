from math import *
while(True):
 print ("\nЭта прога выводит корень из числа которое вы введёте:\n       --------------------------")
 a = int(input ("Введите число - "))
 if a != 2203:
  if a >= 0:
   result = sqrt(a)
   print (f"       --------------------------\nРезультат = {result}\n -------- to exit enter 2203 at entry field -------- ")
  if a < 0:
   result = abs(a)
   result1 = sqrt(result)
   print(f"       --------------------------\nРезультат = {result1}\n -------- to exit enter 2203 at entry field -------- ")
 elif a == 2203:
     print ("       --------------------------\n           EXIT FROM PROGRAM       \n       --------------------------")
     break




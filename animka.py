import os
import time
#ВАЖНО!!!!! Поставить настройки: Run -> Edit Configurations -> Execution -> Emulate terminal in output console -> галочка
#Без этого консоль не очищается
RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLACK = '\u001b[40m'
END = '\u001b[0m'


#Без этого первый кадр не виден я не знаю почему
os.system('cls')

#Первый кадр

#1 стока
print(f'{WHITE}{"   "*8}{END}')

#2,3 строки
for i in range (2):
    print(f'{WHITE}{"   "}{RED}{"   "*2}{WHITE}{"   "*2}{RED}{"   "*2}{WHITE}{"   "}{END}')

#4 строка
print(f'{WHITE}{"   "*8}{END}')

#5 строка
print(f'{RED}{"   "}{WHITE}{"   " * 6}{RED}{"   "}{END}')

#6
print(f'{WHITE}{"   "}{RED}{"   "}{WHITE}{"   " * 4}{RED}{"   "}{WHITE}{"   "}{END}')

#7
print(f'{WHITE}{"   "*2}{RED}{"   "*4}{WHITE}{"   "*2}{END}')

#8
print(f'{WHITE}{"   "*8}{END}')


time.sleep(1)
os.system('cls')


#Второй кадр

#1 стока
print(f'{WHITE}{"   "*8}{END}')

#2,3 строки
for i in range (2):
    print(f'{WHITE}{"   "}{RED}{"   "*2}{WHITE}{"   "*2}{RED}{"   "*2}{WHITE}{"   "}{END}')

#4,5 строки
for i in range(2):
    print(f'{WHITE}{"   "*8}{END}')

#6
print(f'{RED}{"   "*8}{END}')

#7,8
for i in range(2):
    print(f'{WHITE}{"   "*8}{END}')



time.sleep(1)
os.system('cls')


#Третий кадр

#1 стока
print(f'{WHITE}{"   "*8}{END}')

#2,3 строки
for i in range (2):
    print(f'{WHITE}{"   "}{RED}{"   "*2}{WHITE}{"   "*2}{RED}{"   "*2}{WHITE}{"   "}{END}')

#4 строка
print(f'{WHITE}{"   "*8}{END}')

#5
print(f'{WHITE}{"   "*2}{RED}{"   "*4}{WHITE}{"   "*2}{END}')

#6
print(f'{WHITE}{"   "}{RED}{"   "}{WHITE}{"   " * 4}{RED}{"   "}{WHITE}{"   "}{END}')

#7
print(f'{RED}{"   "}{WHITE}{"   " * 6}{RED}{"   "}{END}')

#8
print(f'{WHITE}{"   "*8}{END}')
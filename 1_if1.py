"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main(n):
    if n <= 7:
      return 'быть в садике'
    elif 7 < n <=18:
      return 'учиться в школе'
    elif 18 < n <= 24:
      return 'учиться в университете'
    else:
      return 'Работать'

print("Напиши свой возраст:")
man = int(input())
if __name__ == "__main__":
    print(main(man))

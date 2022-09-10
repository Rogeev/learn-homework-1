"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(string1, string2):
    if type(string1) == str and type(string2)  == str:
      print(0)
      if string1.lower() == string2.lower():
        return 1
      elif len(string1) > len(string2):
        return 2
      elif len(string1) != len(string2) and string2.lower() == 'learn':
        return 3
      
string1 = input('строка 1:')
string2 = input('строка 2:') 

if __name__ == "__main__":
    print(main(string1, string2))

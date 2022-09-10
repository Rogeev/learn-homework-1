"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main(spis):
  return sum(spis), sum(spis)/len(spis)    

store_num = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

if __name__ == "__main__":
  all_sell = 0
  avr_sell = 0
  for prod in store_num:
    sum_prod, sred_prod = main(prod['items_sold'])
    print(f'Сумарное количество продаж {prod["product"]} : {sum_prod}')
    print(f'Среднее количество продаж {prod["product"]} : {round(sred_prod, 1)}')
    all_sell += sum_prod
    avr_sell += sred_prod
  print(f'Сумарное количество всех продаж : {all_sell}')
  print(f'Среднее количество всех продаж : {round(avr_sell/len(store_num), 2)}')
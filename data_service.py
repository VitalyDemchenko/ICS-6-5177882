"""модуль для роботи з файлами первинних даних
-зчитування та вивід на екран
"""


def get_goods():
    """повертає список товарів який отримує з файлу 'goods.txt'

    Returns:
      goods_list:список товарів
    """
    with open("./data/goods.txt") as goods_file:
        from_file = goods_file.readlines()

    #накопичувач товарів
    goods_list = []
            
    for line in from_file:
       
       #відрізати '\n' в кінці рядка
       line = line[:-2]

       line_list = line.split(';')
       goods_list.append(line_list)
    
    return goods_list

def show_goods(goods):
    """виводить на екран список товарів заданого діапазона
        
    Args:    
      goods([list]):список товарів
    """

    good_code_from = input("З якого кода вивести список товарів?  Введіть код товара і натисніть <Enter>: ")
    good_code_to = input("По який код вивести список товарів?   Введіть код товара і натисніть <Enter>: ")
    
    kol_lines = 0
    
    for good in goods:
        if good_code_from <= good[0] <= good_code_to:
           print("код: {:4} назва: {:15} скидка: {:4}".format(good[0], good[1], good[2]))
           kol_lines += 1
    
    if kol_lines == 0:
         print("Код не знайдено")

#goods = get_goods()
#show_goods(goods)


def get_goods_circulations():
  """повертає список товарообігу універмагу який отримує з файлу 'goods_circulations.txt'

  Returns:
    goods_circulations_list:список товарообігу
  """
  with open("./data/goods_circulations.txt") as goods_circulations_file:
      from_file = goods_circulations_file.readlines()
  
  #накопичувач товарообігів
  goods_circulations_list = []

  for line in from_file:
     
     #відрізати '\n' в кінці рядка
     line = line[:-2]

     line_list = line.split(';')
     goods_circulations_list.append(line_list)

  return goods_circulations_list

def show_goods_circulations(goods_circulations):
    """виводить на екран список товарообігу заданого діапазона

    Args:
      goods_circulations ([list]):список товарообігу
    """

    goods_circulation_code_from = input("З якого кода вивести список товарообігу? Введіть код товара і натисніть <Enter>: ")
    goods_circulation_code_to = input("По який код вивести список товарообігу?  Введіть код товара і натисніть <Enter>: ")

    kol_lines = 0

    for goods_circulation in goods_circulations:
        if goods_circulation_code_from <= goods_circulation[0] <= goods_circulation_code_to:
           print("код: {:4} план: {:4} очікуєме виконання: {:4} рік: {:5}".format(goods_circulation[0], goods_circulation[1], goods_circulation[2], goods_circulation[3]))
           kol_lines += 1

    if kol_lines == 0:
         print("Код не знайдено")

#goods_circulations = get_goods_circulations()
#show_goods_circulations(goods_circulations)
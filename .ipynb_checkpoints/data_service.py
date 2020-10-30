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

    good_code_from = input("З якого кода? ")
    good_code_to = input("По який код? ")
    
    kol_lines = 0
    
    for good in goods:
        if good_code_from <= good[0] <= good_code_to:
           print("код: {:4} назва: {:15} скидка: {:4}".format(good[0], good[1], good[2]))
           kol_lines += 1
    
    if kol_lines == 0:
         print("Код не знайдено")

goods = get_goods()
show_goods(goods)
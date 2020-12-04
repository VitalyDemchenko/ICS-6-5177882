"""головний модуль задачі
- виводить на екран та в файл розрахункову таблицю
- виводить на екран первинні файли 
"""

import os
from process_data import create_gross_income
from data_service import show_goods, show_goods_circulations, get_goods, get_goods_circulations


MAIN_MENU = \
"""
~~~~~~~~~~~~~~~~~~~ ОБРОБКА ВАЛОВОГО ДОХОДУ УНІВЕРМАГУ НА ПОТОЧНИЙ РІК ~~~~~~~~~~~~~~~~    

1 - вивід валового доходу на екран
2 - запис валового доходу в файл
3 - вивід списка товарообіга універмагу
4 - вивід списка товарних груп
0 - завершення роботи
-------------------------------------------
"""

TITLE = "ВАЛОВИЙ ДОХІД УНІВЕРМАГУ НА ПОТОЧНИЙ РІК"

HEADER = \
""" 
============================================================================================================================
| Найменування   |   Рік   |        Товарообіг,тис.грн        |  Торгова    |             Валовий дохід,тис.грн.           |
| товарної групи |         |==================================|  скидка, %  |==============================================|
|                |         |   План   |  Очіковане виконання  |             |         План         |  Очіковане виконання  |  
===========================================================================================================================|
"""

FOOTER = \
'''
============================================================================================================================

'''

STOP_MESSAGE = 'Для продовження натисніть <Enter>'

def show_gross_income(gross_income_list):
    """виводить таблицю валового доходу

    Args:
        gross_income_list ([type]): список валового доходу
    """
    print(f"\n\n{TITLE:^111}")
    print(HEADER)

    for gross_income in gross_income_list:
        print(f"{gross_income['name_of_goods_group']:17}",
              f"{gross_income['year']:^11}",
              f"{gross_income['plan_of_commodity_circulations']:^7}",
              f"{gross_income['expected_performance_of_commodity_circulations']:>23}",
              f"{gross_income['trade_discount']:>13}",
              f"{gross_income['plan_of_gross_income']:>23.2f}",
              f"{gross_income['expected_performance_of_gross_income']:>23.2f}",
              )

    print(FOOTER)

def write_gross_income(gross_income_list):
    """записує список валового доходу у текстовий файл

    Args:
        gross_income_list ([type]): список валового доходу
    """

    with open('./data/gross_income.txt', 'w') as gross_income_file:
        for gross_income in gross_income_list:
            line = \
                gross_income['name_of_goods_group'] + ';' +                                    \
                str(gross_income['year']) + ';' +                                              \
                str(gross_income['plan_of_commodity_circulations']) + ';' +                    \
                str(gross_income['expected_performance_of_commodity_circulations']) + ';' +    \
                str(gross_income['trade_discount']) + ';' +                                    \
                str(gross_income['plan_of_gross_income']) + ';' +                              \
                str(gross_income['expected_performance_of_gross_income']) + '\n'

            gross_income_file.write(line)

    print("Файл успішно сформовано ...")


while True:

    #вивід головного меню
    os.system('clear')
    print(MAIN_MENU)
    command_number = input("Введіть номер команди: ")

    #обробка команд користувача
    if command_number == '0':
        print('\nПрограма завершила роботу')
        exit(0)

    elif command_number == '1':
        gross_income_list = create_gross_income()
        show_gross_income(gross_income_list)
        input(STOP_MESSAGE)

    elif command_number == '2':
        gross_income_list = create_gross_income()
        write_gross_income(gross_income_list)

    elif command_number == '3':
        goods_circulations = get_goods_circulations()
        show_goods_circulations(goods_circulations)
        input(STOP_MESSAGE)

    elif command_number == '4':
        goods = get_goods()
        show_goods(goods)
        input(STOP_MESSAGE)

print(MAIN_MENU)
command_number = input("Введіть номер команди: ")
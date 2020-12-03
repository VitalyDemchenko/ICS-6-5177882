"""Модуль для виведення валового доходу універмагу на поточний рік
"""
from data_service import get_goods, get_goods_circulations


#структура запису для вихідних даних
#gross_income - валовий дохід
gross_income = {   
    'goods_group'                                     : "",       #товарна група
    'year'                                            : "",       #рік
    'plan_of_commodity_circulations'                  : 0.0,      #план товарообігу
    'expected_performance_of_commodity_circulations'  : 0.0,      #очікуване виконання товарообігу
    'trade_discount'                                  : 0.0,      #торгова скидка
    'plan_of_gross_income'                            : 0.0,      #план валового доходу
    'expected_performance_of_gross_income'            : 0.0       #очікуване виконання валового доходу
}

def create_gross_income():
    """формування списку валового доходу

    Returns:
        gross_income_list: список валового доходу
    """
    
    def get_goods_group_name(good_code):
        """знаходить товар по коду"""
        for good in goods:
            if good_code == good[0]:
                return good[1]
        return "*** Назва не знайдена ***"
    
    def get_trade_discount(trade_discount_code):
        """знаходить скидку по коду"""        
        for trade_discount in goods:
            if trade_discount_code == trade_discount[0]:
                return trade_discount[2]
        return "*** Назва не знайдена ***"
    

    #накопичувач валового доходу
    gross_income_list = []

    goods_circulations = get_goods_circulations()
    goods = get_goods()

    for goods_circulation in goods_circulations:
        
        #робоча змінна
        gross_income_work = gross_income.copy()
        
        gross_income_work['year']                                           = goods_circulation[3]
        gross_income_work['plan_of_commodity_circulations']                 = goods_circulation[1]
        gross_income_work['expected_performance_of_commodity_circulations'] = goods_circulation[2]
        gross_income_work['goods_group']                                    = get_goods_group_name(goods_circulation[0])
        gross_income_work['trade_discount']                                 = get_trade_discount(goods_circulation[0])
        gross_income_work['plan_of_gross_income']                           = float(gross_income_work['plan_of_commodity_circulations']) * float(gross_income_work['trade_discount']) * 0.01
        gross_income_work['expected_performance_of_gross_income']           = float(gross_income_work['expected_performance_of_commodity_circulations']) * float(gross_income_work['trade_discount']) * 0.01

        gross_income_list.append(gross_income_work)
        
    return gross_income_list

#gross_incomes = create_gross_income()

#for item in gross_incomes:
#    print(item)

#print(get_goods())
#print(get_goods_circulations())
''' Program to calculate the money exchanged'''

def exchange_money(budget, exchange_rate):
    """ Function to make the conversion from currency A to B based on the budget and exchange_rate
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """ Function to calculate the amount of money left after exchange
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """ Function to calculate the total value of bills
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return denomination * number_of_bills

def get_number_of_bills(budget, denomination):
    """ Function to calculate the number of bills
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget // denomination)

def get_leftover_of_bills(budget, denomination):
    """ Function to calculate the leftover after the calculations of the number of bills
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    return budget % denomination
 
def exchangeable_value(budget, exchange_rate, spread, denomination):
    """ Function to calculate the maximum value to get 
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    new_exchange_rate = exchange_rate + (exchange_rate * (spread / 100))
    money = exchange_money(budget, new_exchange_rate)
    nr_bills = get_number_of_bills(money, denomination)
    return get_value_of_bills(denomination, nr_bills)

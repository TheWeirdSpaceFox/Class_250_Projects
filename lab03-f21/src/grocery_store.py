"""
Practice with lists, tuples, dictionary, and strings


@author Amanda Sanders
@version 9/9/21-9/14/21

"""
# pylint: disable-msg=C0103

def stock():
    """
    Returns the dictionary reference with key:value pairs
    described in README
    :return: reference to a dictionary object
    """
    dictionary = {"pink lady apple": 2.99, "honeycrisp apple": 3.99,
                  "eggs": 1.29, "bananas": 3.99, "milk": 4.59, "ground beef": 8.99, "cheerios": 3.69}
    return dictionary


def shop(stock_dict, grocery_list):
    """
    Calculate total cost of shopping trip

    See the README for description of the output

    :param stock_dict:  dictionary containing grocery stock with item_name:price_per_quantity pairs
    :param grocery_list:  list of tuples of [(item_name1, quantity1), (item_name2, quantity2),... ]
    :return: tuple with (total, receipt, out_of_stock_list)
    """
    # print('s=',stock_dict)
    # print('g=',grocery_list)
    total = 0
    out_of_stock_list = []
    list_of_keys = []
    for key in stock_dict:
        key = key
        if key is not int:
            list_of_keys.append(key)

    for tuple in grocery_list:
        item = tuple[0]
        if item in list_of_keys:
            total += stock_dict[item]*tuple[1]
        else:
            out_of_stock_list.append(item)
    # print('total', total)
    # print(out_of_stock_list)
    receipt = ''
    for tuple in grocery_list:
        item = tuple[0]
        if item not in out_of_stock_list:
            receipt += "{:<20} ${:>5}\n".format(item, stock_dict[item] * tuple[1])
    receipt += "{:>28}\n{:<20} $ {:>5}".format('-------',"total",total)
    #     if item not in out_of_stock_list:
    #         receipt += "{}  $ {}\n".format(item, stock_dict[item]*tuple[1])
    # receipt += "    ------\n total   $ {}".format(total)

    tuple_final = (total, receipt, out_of_stock_list)

    return tuple_final


# No need to change this part of code - Just to help you debug
if __name__ == '__main__':


    print(" Example usage of stock() and shop() :")

    # Get the stock dictionary as defined in README
    store_stock = stock()
    print(" Stock : ", store_stock)

    # Define a grocery list
    grocery_list = [("honeycrisp apple", 2), ("milk", 1), ("delci food", 1)]
    print("Shopping list: ", grocery_list)

    # Do the shopping
    total, receipt, out_of_stock = shop(store_stock, grocery_list)
    print(" Total=", total)
    print(receipt)
    print(" Out of stock: ", out_of_stock)

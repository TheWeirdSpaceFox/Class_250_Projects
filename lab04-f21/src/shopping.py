import os

def foodlion_dict():
    foodlion_list = []
    foodlion_dict = {}
    file_path = os.path.join("data","FoodLion.txt")
    with open(file_path) as file:
        lines = file.readlines()
        # print(lines)
        for string in lines:
            items_and_prices_fl = string.strip()
            foodlion_list.append(items_and_prices_fl)
            # print(items_and_prices_fl)
    for item_price in foodlion_list:
        #items into dictionary based on length due to longer words
        #stripped $ so could turn into float for comparison between stores
        item_and_price_split = item_price.split()
        if len(item_and_price_split) == 2:
            item = item_and_price_split[0]
            price = item_and_price_split[1].strip('$')
            foodlion_dict[item] = price
        elif len(item_and_price_split) == 3:
            item = item_and_price_split[0] + ' ' + item_and_price_split[1]
            price = item_and_price_split[-1].strip('$')
            foodlion_dict[item] = price
        else:
            item = item_and_price_split[0] + ' ' + item_and_price_split[1] + ' ' + item_and_price_split[2]
            price = item_and_price_split[-1].strip('$')
            foodlion_dict[item] = price
    # print('###########')
    # print(foodlion_list)
    # print(foodlion_dict)
    return foodlion_dict

def harristeeter_dict():
    harristeeter_list = []
    harristeeter_dict = {}
    file_path = os.path.join("data","HarrisTeeter.txt")
    with open(file_path) as file:
        lines = file.readlines()
        # print(lines)
        for string in lines:
            items_and_prices_ht = string.strip()
            harristeeter_list.append(items_and_prices_ht)
            # print(items_and_prices_ht)
    for item_price in harristeeter_list:
        item_and_price_split = item_price.split()
        if len(item_and_price_split) == 2:
            item = item_and_price_split[0]
            price = item_and_price_split[1].strip('$')
            harristeeter_dict[item] = price
        elif len(item_and_price_split) == 3:
            item = item_and_price_split[0] + ' ' + item_and_price_split[1]
            price = item_and_price_split[-1].strip('$')
            harristeeter_dict[item] = price
        else:
            item = item_and_price_split[0] + ' ' + item_and_price_split[1] + ' ' + item_and_price_split[2]
            price = item_and_price_split[-1]
            harristeeter_dict[item] = price.strip('$')
    # print('###########')
    # print(harristeeter_list)
    # print(harristeeter_dict)
    return harristeeter_dict

def list_shopping():
    list_list = []
    list_dict = {}
    quantity_list = []
    item = []
    list_final = []
    file_path = os.path.join("data", "List.txt")
    with open(file_path) as file:
        lines = file.readlines()
        # print(lines)
        for string in lines:
            items_and_quantity_list = string.strip()
            # print(items_and_quantity_list)
            list_list.append(items_and_quantity_list)
            # print(list_list)
    for item_quantity in list_list:
        #Get in order item price
        item_and_quantity_split = item_quantity.split()
        if len(item_and_quantity_split) == 2:
            for str_int in item_and_quantity_split:
                if str_int.isdigit():
                    quantity_list.append(str_int)
                else:
                    item.append(str_int)
        elif len(item_and_quantity_split) == 3:
            two_word_item = ''
            for str_int in item_and_quantity_split:
                if str_int.isdigit():
                    quantity_list.append(str_int)
                else:
                    two_word_item += str_int + ' '

            two_word_item = two_word_item.split()

            item.append("{} {}".format(two_word_item[0], two_word_item[1]))
        else:
            three_word_item = ''
            for str_int in item_and_quantity_split:
                if str_int.isdigit():
                    quantity_list.append(str_int)
                else:
                    three_word_item += str_int + ' '

            three_word_item = three_word_item.split()

            item.append("{} {} {}".format(three_word_item[0], three_word_item[1], three_word_item[2]))
    # print(quantity_list)
    # print(item)
    i = 0
    while i <= len(item)-1:
        # put into tuple in list
        list_final.append((item[i], quantity_list[i]))
        i += 1
    # print('###########')
    # print(list_list)
    # print(list_dict)
    # print(list_final)
    return list_final

def not_sold():
    list = list_shopping()
    # print(list)
    not_sold_list = []
    harristeeter = harristeeter_dict()
    foodlion = foodlion_dict()
    har_key = []
    food_key = []
    not_har = []
    not_food = []
    # could probably take out key thing to shorten put because couldn't figure out what was wrong solved issue
    for key in harristeeter:
        key = key
        if key is not int:
            har_key.append(key)
    for key in foodlion:
        key = key
        if key is not int:
            food_key.append(key)
    for tuple in list:
        item = tuple[0]
        if item not in har_key:
            not_har.append(item)
        if item not in food_key:
            not_food.append(item)

    for item in not_har:
        if item in not_food:
            not_sold_list.append(item)
    # print(not_food)
    # print(not_har)
    # print(not_sold_list)
    return not_sold_list

def compare_price():
    list = list_shopping()
    list_minus_missing = []
    harristeeter = harristeeter_dict()
    foodlion = foodlion_dict()
    buy = []
    for tuple in list:
        item = tuple[0]
        if item not in not_sold():
            list_minus_missing.append(tuple)
    # print(list_minus_missing)
    for tuple in list_minus_missing:
        item = tuple[0]
        if item in harristeeter and item in foodlion:
            price_h = harristeeter[item]
            price_f = foodlion[item]
            if float(price_h) < float(price_f):
                buy.append(('Harris Teeter', item, float(price_h)))
            else:
                buy.append(('Food Lion', item, float(price_f)))
        elif item in foodlion:
            price_f = foodlion[item]
            buy.append(('Food Lion',item, float(price_f)))
        elif item in harristeeter:
            price_h = harristeeter[item]
            buy.append(('Harris Teeter', item, float(price_h)))
    return buy

def total():
    store_item_price = compare_price()
    item_quantity = list_shopping()
    price = []
    quantity = []
    total_price = []
    item = []
    store = []
    store_item_quantity_price = []
    for i in store_item_price:
        price.append(i[2])
        item.append(i[1])
        store.append(i[0])
    for i in item_quantity:
        quantity.append(i[1])
    # print(price)
    # print(quantity)
    i = 0
    while i <= len(price)-1:
        total_price.append(price[i] * float(quantity[i]))
        i+=1
    # print(total_price)
    i = 0
    while i <= len(total_price)-1:
        store_item_quantity_price.append((store[i], item[i], quantity[i], total_price[i]))
        i+=1
    # print(store_item_quantity_price)
    return store_item_quantity_price

def formating():
    store_item_quantity_price = total()
    not_found = not_sold()
    total_price = 0
    receipt = ' {:<28} {:<28} {:<28} {:<28}'.format('Store', 'Item', 'Quantity', 'Total Price')
    for i in store_item_quantity_price:
        store = i[0]
        item = i[1]
        quantity = i[2]
        price = i[3]
        total_price += price
        receipt += '\n {:<28} {:<28} {:<28} ${:.2f}'.format(store,item,quantity,price)
    receipt += '\n' + '-'* 98
    receipt += '\n {:>88}: ${:.2f}'.format('Total', total_price)
    receipt += '\n' + '-' * 98
    receipt += '\n {}'.format('Not Found:')
    for item in not_found:
        receipt += '\n {}'.format(item)
    return receipt








if __name__ == '__main__':
    # print(foodlion_dict())
    # print('*********************************************')
    # print(harristeeter_dict())
    # print('*********************************************')
    # print(list_shopping())
    # print('*********************************************')
    # print(not_sold())
    # print('*********************************************')
    # print(compare_price())
    # print('*********************************************')
    # total()
    print(formating())
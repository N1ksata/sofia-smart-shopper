import json

def load_prices():
    with open('market_prices.json', 'r') as f:
        prices = json.load(f)
        return prices

def read_shopping_list():
    found = False
    shopping_list = []
    with open('my_list.txt', 'r') as f:
        for line in f:
            item = line.strip()
            if item:
                shopping_list.append(item)
                found = True
    if not found:
        print('No shopping list')
    return shopping_list

def calculate_price(prices,shopping_list):
    total_price = 0.0
    for item in shopping_list:
        for category in prices:
            if item in prices[category]:
                total_price += prices[category][item]["price"]
                break
    return round(total_price ,  2)



# test
# if __name__ == "__main__":
#     grocery_data = load_prices()
#     print("Successfully loaded data:")
#     print(grocery_data)

# if __name__ == "__main__":
#     grocery_data = load_prices()
#
#     # Test your new function
#     my_items = read_shopping_list()
#     print("Successfully loaded shopping list:")
#     print(my_items)

if __name__ == "__main__":
    grocery_data = load_prices()
    my_items = read_shopping_list()

    print(calculate_price(grocery_data, my_items) ,"EURO")

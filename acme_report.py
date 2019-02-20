from acme import Product
import random


def generate_products(n=30):
    products = {}
    for i in range(n):
        adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        prefix = random.choice(adjective)
        suffix = random.choice(noun)
        name = f'{prefix} {suffix}'
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0, 2.6)
        products[i] = Product(name, price, weight, flammability)
    return products


def inventory_report(n):
    list_of_names = []
    list_of_prices = []
    list_of_weights = []
    list_of_flammability = []

    for i in range(len(n)):
        list_of_names.append(n[i].name)
        list_of_prices.append(n[i].price)
        list_of_weights.append(n[i].weight)
        list_of_flammability.append(n[i].flammability)

    unique = len(set(list_of_names))
    average_price = sum(list_of_prices) / 30
    average_weight = sum(list_of_weights) / 30
    average_flammability = sum(list_of_flammability) / 30

    print ("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    print ("Unique product names: ", unique)
    print ("Average price: ", average_price)
    print ("Average weight: ", average_weight)
    print ("Average flammability: ", average_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())

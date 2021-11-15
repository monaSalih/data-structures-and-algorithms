import sys

menu = [
    {"type": "Appetizers",
     "items": [
         {"name": "Wings", "count": 0},
         {"name": "Cookies", "count": 0},
         {"name": "Spring Rolls", "count": 0},
       ],
    },

    {"type": "Entrees",
     "item": [
         {"name": "Salmon", "count": 0},
         {"name": "Steak", "count": 0},
         {"name": "Meat Tornado", "count": 0},
         {"name": "A Literal Garden", "count": 0},
        ],
    },

    {"type": "Desserts",
     "items": [
         {"name": "Ice Cream", "count": 0},
         {"name": "Cake", "count": 0},
         {"name": "Pie", "count": 0},
        ],
    },

    {"type": "Drinks",
     "items": [
         {"name": "Coffee", "count": 0},
         {"name": "Tea", "count": 0},
         {"name": "Unicorn Tears", "count": 0},
        ],
    },
]

def get_menu():
    for type in menu:
        print (type["type"])
        print("----------")
        for item in type["items"]:
            print(item["name"])
        print("\n")

def print_order():
    print ("Your order:")
    for type in menu:
        for item in type["items"]:
            if item["count"] > 0:
                print (f'{item["count"]} {item["name"]}')

def order_something():
    while True:
        item_exists = False
        order = input()
        if order.lower() == "quit":
            sys.exit(0)
        elif order.lower() == "summary":
            print_order()
        else:
            for type in menu:
                print (type,"type result")
                for item in type["items"]:
                    # print (item,"item result")
                    if order.lower() == item["name"].lower():
                        item_exists = True
                        item["count"] += 1
                        if item["count"] == 1:
                            print(f'**{item["count"]} order of {item["name"]} has been added to your meal **')
                        else:
                            print(f'**{item["count"]} orders of {item["name"]} have been added to your meal **')
            if item_exists == False:
                print(f'Sorry, {order} is not on our menu.')


if __name__ == "__main__":
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print("** To view your oder, type \"summary\" **")
    print("** To quit at any time, type \"quit\" **")
    print("**************************************")
    print("\n")
    get_menu()
    print("**************************************")
    print("** What would you like to order? **")
    print("**************************************")
    order_something()

welcomeMassage = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""
menu = [
    {
        'type':1,
        'foods':[
            'Wings','Cookies','Spring Rolls',
        ]
    },
    {
        'type':'Entrees',
        'foods':[
            'Salmon','Steak','Meat Tornado','A Literal Garden',
        ]
    },
    {
        'type':'Desserts',
        'foods':[
            'Ice Cream','Cake','Pie',
        ]
    },
    {
        'type':'Drinks',
        'foods':[
            'Coffee','Tea','Unicorn Tears',
        ]
    },
]

appetizers = """group1
----------
Wings
Cookies
Spring Rolls
"""
entrees = """Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
"""
desserts = """Desserts
--------
Ice Cream
Cake
Pie
"""
drinks = """Drinks
------
Coffee
Tea
Unicorn Tears
"""
print(welcomeMassage)
print(appetizers)
print(entrees)
print(desserts)
print(drinks)
orderlist = []
counter = 0
flag = 1
while flag == 1:
    order = input("""***********************************
    ** What would you like to order? **
    ***********************************
    >""")

    if order == "quit":
        flag = 0
        break
    else:
        for foodtype in menu:
            for kind in foodtype["foods"]:
                if order.lower() == kind.lower():
                    orderlist.append(order)
                    # print(orderlist)
                    if order in orderlist:
                        counter = orderlist.count(order)
                        # print("inside counterrrrr",counter)
                        print(f"** {counter} orders of {order} have been added to your meal **")
                        break
                    else:
                        print(f"** {counter} orders of {order} have been added to your meal **")


if flag == 0:
    print("Thank you for ordering from our restaurant")

'''
DICTIONARIES
'''

# person = {
#     "name": "justin",
#     "shirt":"black",
#     "pants": "blue"
#     }

# print(person["name"])
# print(person["shirt"])
# print(person["pants"])


def introducer():
    person = {
        "name": "justin",
        "shirt": "black",
        "pants": "blue",
        "assets": 100,
        "debt": 50,
        "netWorth": lambda: person["assets"] - person["debt"],
        "favFruits": ["oranges", "apples", "bananas"]
    }

    print(f'hello my name is {person["name"]}, i have a {person["shirt"]} shirt, and wearing {person["pants"]} pants, and new worth is {person["netWorth"]()}, also my favorite fruits are {person["favFruits"]}')


introducer()

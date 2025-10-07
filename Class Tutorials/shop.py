shop = {
'milk': 70,
'bread': 89,
'sugar': 99
}

bought = []
item1 =input('what do you buy?')
item2 =input('what do you buy?')
bought.append(item1)
bought.append(item2)

total = shop[item1] + shop[item2]

print(f'what you want to buy sir is {item1} and {item2}, the total amount of what you want to buy is  £{total}')
if total > 100:
    print('great shoping 😊' )
else:
    print('shop more')


# bought =[]
# bought.append('see')
# bought.append('time')
# print(bought)


# see = {
#     'car': 30,
#     'shoe': 300,
#     'tie': 3000,
#     'cup': 60
# }


# print(see['car'])

P_lang = ("C++","Java","Python","Django")
print(P_lang[1])
Sets = {1,2,3,3,4,5}
print(Sets)
Dicts = {"Name":["Michael,james"],
         "Age":[29,33],
         "country":["France","Japan"]}
print(Dicts.values())
Dicts["Name"]


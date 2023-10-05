def read_file(read_file):

    with open(read_file, encoding = "utf-8") as recipes_file:
        cook_book = {}
        for line in recipes_file.read().split("\n\n"):
            meal_name = line.split("\n")
            dish_name = meal_name[0]
            ingredients_list = []
            for id_, value in enumerate(meal_name):
                if id_ < 2:
                    continue
                ingredient_list = meal_name[id_].split(" | ")
                ingredients_list.append({'ingredient_name': ingredient_list[0], 'quantity': ingredient_list[1], 'measure': ingredient_list[2]})

            cook_book[dish_name] = ingredients_list

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_file('recipes.txt')
    ingredients_list = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                if ingredient['ingredient_name'] in ingredients_list.keys():
                    ingredients_list[ingredient['ingredient_name']] = {
                        'quantity': ingredients_list[ingredient['ingredient_name']]['quantity'] +
                                    int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}
                else:
                    ingredients_list[ingredient['ingredient_name']] = {
                        'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}

    return ingredients_list


shop_list_by_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print(shop_list_by_dishes)
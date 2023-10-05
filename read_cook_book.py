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
                ingredient_name = ingredient_list[0]
                quantity = ingredient_list[1]
                measure = ingredient_list[2]
                ingredients_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})

            cook_book[dish_name] = ingredients_list

    return cook_book


cook_book = read_file('recipes.txt')
print(cook_book)
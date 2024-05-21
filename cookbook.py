def read_recipes(file):
    cook_book = {}
    with open(file, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredient_count = int(file.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure,
                })
            cook_book[dish_name] = ingredients
            file.readline()  # Пропуск пустой строки между рецептами
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {
                        'measure': ingredient['measure'],
                        'quantity': quantity
                    }
    return shop_list

# Пример использования
cook_book = read_recipes('recipes.txt')
print(cook_book)

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(shop_list)
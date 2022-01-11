
#import pprint #from pprint


def get_dishes_names(file_name):
    dishes = []
    with open(file_name, encoding='utf8') as file:
        for line in file:
            dishes.append(line.strip())
            number_of_ingredients = int(file.readline().strip())
            for dish_name in range(number_of_ingredients):
                file.readline()
            file.readline()

    return dishes



def get_ingredients(file_name):   
    ingredients_for_all_dishes = []    
    with open(file_name, encoding='utf8') as file:
        for line in file:
            number_of_ingredients = int(file.readline().strip())
            for dish_name in range(number_of_ingredients + 1):
                ingredients_for_all_dishes.append([file.readline().strip()])

    return ingredients_for_all_dishes


def split_on(list_for_split):
    splitted = [[]]
    for item in list_for_split:
        if item == ['']:
            splitted.append([])
        else:
            splitted[-1].append(item)
    splitted.pop()

    return splitted


def cook_book_dict(file_name):
    cook_book_dictionary = {}

    for i in range(0, len(get_dishes_names(file_name))):
        cook_book_dictionary[get_dishes_names(file_name)[i]] = split_on(get_ingredients(file_name))[i]

    return cook_book_dictionary


def upgrade_list(list_for_upgrade):  # приведем список к необходимому виду.
    new_list = []
    for val in list_for_upgrade:
        new_list.append(val)
        for ing in val:
            ing = str(ing)[2:-2]
            ing = ing.split('|')
        val.append(ing)
        #print(new_list)

    return list_for_upgrade



if __name__ == '__main__':

    print(split_on(get_ingredients('recipe')))
    cook_book = cook_book_dict('recipe')
    print(cook_book_dict('recipe'))
    print(get_dishes_names('recipe'))



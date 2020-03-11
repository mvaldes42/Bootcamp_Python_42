import sys
import pickle
import ast
# cookbook = {
#     'sandwich': {
#         'ingredients': {'ham', 'bread', 'cheese', 'tomatoes'},
#         'meal': 'lunch',
#         'prep_time': 10
#     },
#     'cake': {
#         'ingredients': {'flour', 'sugar', 'eggs'},
#         'meal': 'desert',
#         'prep_time': 60
#     },
#     'salad': {
#         'ingredients': {'avocado', 'arugula', 'tomatoes', 'spinach'},
#         'meal': 'lunch',
#         'prep_time': 15
#     }
# }

with open('cookbook.p', 'rb') as fp:
    cookbook = pickle.load(fp)


def add_recipe():
    print("You wish to add a recipe. Please enter its details below\n")
    recipe_name = input("Enter the name of the recipe\n")
    ingredients = input("""Enter its ingredients as follows >\
    {\"ingr1\",\"ingredient2\"}\n""")
    meal_type = input("Enter its meal type\n")
    prep_time = input("Enter its preparation type\n")
    cookbook.update({
        recipe_name: {
            'ingredients': ast.literal_eval(ingredients),
            'meal': meal_type,
            'prep_time': prep_time
        },
    })
    print("New recipe {recip_name} added !\n")


def print_recipe(recipe_name):
    i_s = str(cookbook[recipe_name]["ingredients"])
    print(f'\n{"Name:":<20} {recipe_name}')
    print(f'{"Ingredients:":<20} {i_s.replace("{","[").replace("}", "]")}')
    print(f'{"Type of meal":<20} {cookbook[recipe_name]["meal"]}')
    print(f'{"Peparation time":<20} {cookbook[recipe_name]["prep_time"]} m\n')


def promp_user():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe")
    text = input("4: Print the cookbook\n5:Quit\n")
    text_analyzer(text)


def text_analyzer(text):
    '''this is a cookbook'''
    try:
        text = int(text)
    except ValueError:
        print("This option doesn't exist, please type a corresponding number.")
        text = int(input("To exit, enter 5\n"))
        if text == 5:
            exit(print("Cookbook closed"))
        else:
            text_analyzer(text)
    while text != 5:
        if text == 1:
            add_recipe()
            promp_user()
        if text == 2:
            text = input("Enter the name of the recipe to delete\n")
            del cookbook[text]
            promp_user()
        if text == 3:
            print_recipe(input("Enter the name of the recipe to print\n"))
            promp_user()
        if text == 4:
            print("Printing cookbook ...")
            for recipe_name in cookbook.keys():
                print_recipe(recipe_name)
            promp_user()
    if text == 5:
        try:
            import cPickle as pickle
        except ImportError:  # python 3.x
            import pickle

        with open('cookbook.p', 'wb') as fp:
            pickle.dump(cookbook, fp, protocol=pickle.HIGHEST_PROTOCOL)
        exit(print("Cookbook closed"))


promp_user()

from book import Book
from recipe import Recipe
import datetime

tourte = Recipe("Tourte", 2, 57, ["eau", "beurre"], "lunch", "Super recette !")
cake = Recipe("Cake", 2, 57, ["eau", "beurre"], "starter", "Super recette !")
salad = Recipe("Salad", 2, 57, ["eau", "beurre"], "starter", "Super recette !")
recipetype = {'starter': [cake, salad], 'lunch': 0, 'desert': 0}

to_print = str(tourte)
print(to_print)
print("===============================")
book_01 = (Book("Le Book", datetime.date(2020, 9, 25),
                datetime.date(2020, 5, 15), recipetype))
to_print = str(book_01.get_recipe_by_name(cake))
print(to_print)
pizza = Recipe("Pizza", 1, 30, ["peperonni", "pate"], "starter", "Excellent!")
to_print = str(book_01.add_recipe(pizza))
print(to_print)
to_print = str(book_01.get_recipes_by_types('starter'))
print(to_print)

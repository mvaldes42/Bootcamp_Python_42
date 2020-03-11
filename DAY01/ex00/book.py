import datetime
from recipe import Recipe


class Book:
    def __init__(
            self,
            name,
            last_update,
            creation_date,
            recipe_list,
    ):
        if isinstance(name, str):
            self.name = name
        else:
            raise NameError('Type Error')
        if isinstance(last_update, datetime.date):
            self.last_update = last_update
        else:
            raise NameError('Datetime format error 01')
        if isinstance(creation_date, datetime.date):
            self.creation_date = creation_date
        else:
            raise NameError('Datetime format error')
        if isinstance(recipe_list, dict):
            self.recipe_list = recipe_list
        else:
            raise NameError('Not a dic')

    def __str__(self):
        text = (
            'Recipe(Name = ' + self.name
            + ', last_update = ' + str(self.last_update)
            + ', creation date = ' + str(self.creation_date)
            + ', recipe_list = ' + str(self.recipe_list)
        )
        return text

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        recipe = self.recipe_list[name.recipe_type].index(name)
        recipe_re = self.recipe_list[name.recipe_type][recipe]
        i_s = str(recipe_re.ingredients)
        print(f'\n{"Name:":<20} {recipe_re.name}')
        print(f'{"Cooking level:":<20} {recipe_re.cooking_lvl}')
        print(f'{"Cooking time:":<20} {recipe_re.cooking_time} m')
        print(f'{"Ingredients:":<20} {i_s.replace("{","[").replace("}", "]")}')
        print(f'{"Recipe type:":<20} {recipe_re.recipe_type}')
        print(f'{"Description:":<20} {recipe_re.description}')
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for names in self.recipe_list.keys():
            if names == recipe_type:
                for nameu in self.recipe_list[names]:
                    return (self.get_recipe_by_name(nameu))
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        self.last_update = datetime.date.today
        self.recipe_list[recipe.recipe_type].append(recipe)
        print("New recipe " + recipe.name + " added!")
        pass

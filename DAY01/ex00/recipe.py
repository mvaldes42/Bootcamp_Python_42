class Recipe:
    def __init__(
            self,
            name,
            cooking_lvl,
            cooking_time,
            ingredients,
            recipe_type,
            description,
    ):
        if isinstance(name, str):
            self.name = name
        else:
            raise NameError('Type Error')
#
        if cooking_lvl <= 5 and cooking_lvl >= 1:
            self.cooking_lvl = str(cooking_lvl)
        else:
            raise NameError('Out of bounds')
#
        if cooking_time > 0:
            self.cooking_time = cooking_time
        else:
            raise NameError('Type Error')
#
        if isinstance(ingredients, list):
            self.ingredients = ingredients
        else:
            raise NameError('Type Error')
#
        if (
                isinstance(recipe_type, str)
                and any(r_type in recipe_type
                        for r_type in ('lunch', 'desert', 'starter'))
        ):
            self.recipe_type = recipe_type
        else:
            raise NameError('Type Error')
#
        self.description = description

    def __str__(self):
        s_ingredients = str(self.ingredients)
        text = ('Recipe(Name = ' + self.name + ', Cooking level = '
                + str(self.cooking_lvl) + '/5' + ', Cooking time = '
                + str(self.cooking_time) + ' min' + ', Ingredients = '
                + (s_ingredients.replace("[", "(").replace("]", ")")
                                .replace("'", "").replace(",", " &"))
                + ', Recipe type = ' + str(self.recipe_type)
                + ', Description = ' + str(self.description) + ').')
        return text

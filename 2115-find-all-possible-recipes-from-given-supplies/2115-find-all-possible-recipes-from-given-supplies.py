class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """

        prepared_count = 0
        supplies = set(supplies)
        remaining_count = len(recipes)
        prepared_recipes = []

        while True:
            prepared = False
            for i in range(len(ingredients)):
                can_prepare = True
                for ingredient in ingredients[i]:
                    if ingredient not in supplies:
                        can_prepare = False
                        break
                
                if can_prepare: supplies.add(recipes[i])
                prepared_count += 1
                prepared = True
                remaining_count -= 1
                prepared_recipes.append(recipes[i])

            if not prepared or not remaining_count: break

        return prepared_recipes

        
def get_input():
  input = open('21_input.txt', 'r')
  foods = []
  for line in input:
    ingredients, allergens = line.strip().split(' (contains ')
    ingredients = ingredients.strip().split(' ')
    allergens = allergens.replace(')', '').split(', ')
    foods.append((ingredients, allergens))
  return foods

def possible_allergens_per_ingredient(foods):
  ing_by_alg = {} # ingredient -> set of possible allergies
  for ingredients, allergens in foods:
    for allergen in allergens:
      ingredients = set(ingredients)
      if allergen not in ing_by_alg:
        ing_by_alg[allergen] = ingredients
      else:
        ing_by_alg[allergen] &= ingredients

  return ing_by_alg

def ingredient_appearance_count(foods):
  ing_appearances = {} # ingredient -> number of appearances
  for ingredients, allergens in foods:
    for ingredient in ingredients:
      if not ingredient in ing_appearances:
        ing_appearances[ingredient] = 0
      ing_appearances[ingredient] += 1

  return ing_appearances


def part_1():
  foods = get_input()
  ing_by_alg = possible_allergens_per_ingredient(foods)
  ing_appearances = ingredient_appearance_count(foods)

  all_ing = set(ing_appearances.keys())
  for _, ingredients in ing_by_alg.items():
    all_ing -= ingredients
  return sum([ing_appearances[ing] for ing in all_ing])

def part_2():
  foods = get_input()
  ing_by_alg = possible_allergens_per_ingredient(foods)
  allergens = list(ing_by_alg.keys())
  allergens.sort(key = lambda i: len(ing_by_alg[i]))

  seen_ingredients = set()
  while allergens:
    allergen = allergens.pop(0)
    ingredients = ing_by_alg[allergen]
    ingredients -= seen_ingredients

    if len(ingredients) == 1:
      ingredient = list(ingredients)[0]
      seen_ingredients.add(ingredient)
      ing_by_alg[allergen] = ingredient
    else:
      allergens.append(allergen)

  allergens_sorted = sorted(list(ing_by_alg.keys()))
  ingredients_sorted = [ing_by_alg[alg] for alg in allergens_sorted]
  return ",".join(ingredients_sorted)

print(part_2())

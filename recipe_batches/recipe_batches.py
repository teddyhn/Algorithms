#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  n = len(recipe)
  keys = list(recipe.keys())

  batches = [0] * n

  for i in range(n):
    if ingredients.get(keys[i]) is None:
      return 0

    temp = ingredients.get(keys[i]) // recipe.get(keys[i])
    if temp == 0:
      return 0
    else:
      batches[i] = temp

  return min(batches)



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
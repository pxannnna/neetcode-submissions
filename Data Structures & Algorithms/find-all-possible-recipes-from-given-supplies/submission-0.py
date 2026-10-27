from collections import defaultdict, deque
from typing import List

class Solution:

  def findAllRecipes(
      self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
  ) -> List[str]:
    ingredienttorecipe = defaultdict(list)
    indegree = {r: len(ing) for r, ing in zip(recipes, ingredients)}

    for r, ingrs in zip(recipes, ingredients):
      for ingr in ingrs:
        ingredienttorecipe[ingr].append(r)

    queue = deque(supplies)
    res = []

    while queue:
      curr = queue.popleft()

      for next_recipe in ingredienttorecipe[curr]:
        if next_recipe in indegree:
          indegree[next_recipe] -= 1
          if indegree[next_recipe] == 0:
            queue.append(next_recipe)
            res.append(next_recipe)

    return res

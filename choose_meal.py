import random
from get_meals_from_file import get_stored_meals

meals = get_stored_meals()


def choose_meals(num_options) -> str:
    meal = meals[:]  # make a copy of the input list
    random.shuffle(meal)
    for i in range(num_options):
        print(meal.pop())
    return random.choice(meals)

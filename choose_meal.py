import random
from get_meals_from_file import get_stored_meals

meals = get_stored_meals()


def choose_meals(num_options) -> str:
    for _ in range(0, num_options, 1):
        print(random.choice(meals))
    return random.choice(meals)

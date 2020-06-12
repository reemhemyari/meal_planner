import random
from typing import List
from get_meals_from_file import get_stored_meals

meals = get_stored_meals()
meals_copy = meals


def choose_meals(num_options) -> List[str]:
    chosen_meals = []
    if len(meals_copy) > 0:
        for _ in range(0, num_options, 1):

            choice = random.choice(meals_copy)
            if choice not in chosen_meals:
                chosen_meals.append(choice)
                meals_copy.remove(choice)
            else:
                choice2 = random.choice(meals_copy)
                chosen_meals.append(choice2)

    return chosen_meals

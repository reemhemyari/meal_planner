import random
from typing import List
from meal_planner import get_meals_from_file

meals = get_meals_from_file.get_stored_meals()


def choose_meals(num_options: int) -> List[str]:
    chosen_meals = []
    if len(meals) > 0:
        for _ in range(0, num_options, 1):

            choice = random.choice(meals)
            if choice not in chosen_meals:
                chosen_meals.append(choice)
                meals.remove(choice)
            else:
                choice2 = random.choice(meals)
                chosen_meals.append(choice2)

    return chosen_meals

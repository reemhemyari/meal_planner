import random
from typing import List
from mealplanner.meal_store import MealStore


class MealChooser:
    def __init__(self, meal_store: MealStore) -> None:
        self.meals = meal_store.get_stored_meals()

    def make_choice(self, num_options: int) -> List[str]:
        chosen_meals = []
        if len(self.meals) > 0:
            if len(self.meals) < num_options:
                chosen_meals += self.meals
                for item in chosen_meals:
                    if item in self.meals:
                        self.meals.remove(item)
            else:
                for _ in range(0, num_options, 1):
                    choice = random.choice(self.meals)
                    if choice not in chosen_meals:
                        chosen_meals.append(choice)
                        self.meals.remove(choice)
                    else:
                        choice2 = random.choice(self.meals)
                        chosen_meals.append(choice2)

        else:
            print("Error - List empty")

        # if len(chosen_meals) < num_options:
        # for item in chosen_meals:
        # chosen_meals.remove(item)

        return chosen_meals

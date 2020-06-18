import pathlib
from typing import List

default_recipes = str(pathlib.Path(__file__).parent.parent / "recipes.txt")


class MealStore:
    def __init__(self, file_name: str = default_recipes) -> None:
        self.store = file_name

    def get_stored_meals(self) -> List[str]:
        with open(self.store, "r") as file:
            return [(line.strip()) for line in file]

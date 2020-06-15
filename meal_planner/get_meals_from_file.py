from typing import List


def get_stored_meals() -> List[str]:
    with open("recipes.txt", "r") as file:
        return [(line.strip()) for line in file]

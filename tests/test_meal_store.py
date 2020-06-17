import pathlib

from mealplanner.meal_store import MealStore

get_meals_from_file = MealStore()
meals = get_meals_from_file.get_stored_meals()
test_recipes = pathlib.Path(__file__).parent / 'test_recipes.txt'


def test_no_num_there():
    for lines in meals:
        [(line.strip()) for line in meals]
        assert any(character.isdigit() for character in lines) is False
        # The isdigit() methods returns “True”
        # if all characters in the string are digits,
        # Otherwise, It returns “False”. Syntax : string.


def test_get_stored_meals_is_not_empty():
    assert len(meals) != 0


def test_there_are_three_meals():
    file_reader = MealStore(test_recipes)
    items_in_file = file_reader.get_stored_meals()
    assert len(items_in_file) == 5

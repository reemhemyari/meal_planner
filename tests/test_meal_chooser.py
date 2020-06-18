import pathlib

from mealplanner.meal_chooser import MealChooser
from mealplanner.meal_store import MealStore

meal_store = MealStore()
num_options = 3
test_recipes = pathlib.Path(__file__).parent / 'test_recipes.txt'


def test_make_choice_doesnt_choose_option_more_than_once_in_lists():
    meal_chooser = MealChooser(meal_store)
    returned_list1 = meal_chooser.make_choice(num_options)
    returned_list2 = meal_chooser.make_choice(num_options)
    for item_in_list1 in returned_list1:
        for item_in_list2 in returned_list2:
            assert item_in_list1 != item_in_list2


def test_make_choice_doesnt_choose_option_more_than_once_in_list():
    meal_chooser = MealChooser(meal_store)
    returned_list = meal_chooser.make_choice(num_options)
    for item in returned_list:
        assert returned_list.count(item) == 1, "Same option appears more than once"


def test_choose_meals_returns_correct_num_options():
    meal_chooser = MealChooser(meal_store)
    returned_list = meal_chooser.make_choice(num_options)
    assert len(returned_list) == num_options, "Didn't print correct number of options"


def test_make_choice_doesnt_pick_option_more_than_once():
    test_meal_store = MealStore(test_recipes)
    meal_chooser = MealChooser(test_meal_store)
    returned_list1 = meal_chooser.make_choice(num_options)
    returned_list2 = meal_chooser.make_choice(num_options)
    for item_list1 in returned_list1:
        for item_list2 in returned_list2:
            assert item_list1 != item_list2, "At least one item appears in both lists"

    assert len(returned_list2) == 2


def test_make_choice_is_empty_after_part_full_result():
    test_meal_store = MealStore(test_recipes)
    meal_chooser = MealChooser(test_meal_store)
    meal_chooser.make_choice(num_options)
    meal_chooser.make_choice(num_options)
    returned_list = meal_chooser.make_choice(num_options)

    assert len(returned_list) == 0


def test_make_choice_returns_empty_list_when_list_is_empty():
    meal_chooser = MealChooser(meal_store)
    meal_chooser.make_choice(24)
    returned_list2 = meal_chooser.make_choice(num_options)

    assert len(returned_list2) == 0
    # you could also output an error message and check if it gets outputted

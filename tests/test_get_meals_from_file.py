from meal_planner import get_meals_from_file


def test_no_num_there():
    meals = get_meals_from_file.get_stored_meals()
    for lines in meals:
        [(line.strip()) for line in meals]
        assert any(character.isdigit() for character in lines) is False
        # The isdigit() methods returns “True”
        # if all characters in the string are digits,
        # Otherwise, It returns “False”. Syntax : string.


def test_get_stored_meals_is_not_empty():
    meals = get_meals_from_file.get_stored_meals()
    assert len(meals) != 0

from get_meals_from_file import get_stored_meals

meals = get_stored_meals()


def test_no_num_there():
    for lines in meals:
        [(line.strip()) for line in meals]
        assert any(character.isdigit() for character in lines) is False
        # The isdigit() methods returns “True” if all characters in the string are digits,
        # Otherwise, It returns “False”. Syntax : string.


def test_get_stored_meals_is_not_empty():
    assert len(meals) != 0


if __name__ == '__main__':
    test_get_stored_meals_is_not_empty()
    test_no_num_there()

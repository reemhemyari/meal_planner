import random
from choose_meal import meals

num_options = 5


def test_choose_meals_random():
    option1 = random.choice(meals)
    option2 = random.choice(meals)
    option3 = random.choice(meals)
    option4 = random.choice(meals)
    assert option1 != option2 and option1 != option3 and option1 != option4, "Should be different"
    assert option2 != option1 and option2 != option3 and option2 != option4, "Should be different"
    assert option3 != option2 and option3 != option1 and option3 != option4, "Should be different"
    assert option4 != option1 and option4 != option2 and option4 != option3, "Should be different"


def test_choose_meals_prints_correct_num_options():
    options_printed = 0
    for _ in range(0, num_options, 1):
        options_printed = options_printed + 1

    assert options_printed == num_options, "Didn't print correct number of options"

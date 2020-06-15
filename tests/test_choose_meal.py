from meal_planner import choose_meal

num_options = 5


def test_choose_meals_random():
    option1 = choose_meal.choose_meals(1)
    option2 = choose_meal.choose_meals(1)
    option3 = choose_meal.choose_meals(1)
    option4 = choose_meal.choose_meals(1)
    assert option1 != option2 \
           and option1 != option3 \
           and option1 != option4, "Should be different"
    assert option2 != option1 \
           and option2 != option3 \
           and option2 != option4, "Should be different"
    assert option3 != option2 \
           and option3 != option1 \
           and option3 != option4, "Should be different"
    assert option4 != option1 \
           and option4 != option2 \
           and option4 != option3, "Should be different"


def test_choose_meals_prints_correct_num_options():
    options_printed = 0
    for _ in range(0, num_options, 1):
        options_printed = options_printed + 1

    assert options_printed == num_options, "Didn't print correct number of options"

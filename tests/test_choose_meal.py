from meal_planner import choose_meal

num_options = 5


def test_choose_meals_doesnt_choose_option_more_than_once():
    returned_list = choose_meal.choose_meals(num_options)
    for item in returned_list:
        assert returned_list.count(item) == 1, "Same option appears more than once"


def test_choose_meals_returns_correct_num_options():
    returned_list = choose_meal.choose_meals(num_options)
    assert len(returned_list) == num_options, "Didn't print correct number of options"

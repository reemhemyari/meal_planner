from mealplanner.meal_store import MealStore
from mealplanner.meal_chooser import MealChooser

meal_store = MealStore()
meals = meal_store.get_stored_meals()


def main() -> None:

    num_options = int(
        input("Enter a number of options you would like to be generated: ")
    )

    # if statement ensures that the user chooses to generate at least one option,
    # otherwise stopping the program
    if num_options < 1:
        print("")
        print("Error - Number must be 1 or larger")
        print("Program stopped")
    elif num_options > len(meals):
        print("")
        print("Error - There aren't that many options available")
        print("Program stopped")
    else:
        meal_chooser = MealChooser(meal_store)
        chosen_meals = meal_chooser.make_choice(num_options)
        print(chosen_meals)

        # the while loop allows the user to regenerate options
        new_options = "y"
        while new_options == "y":
            new_options = str(input("Would you like to generate new options? (y/n): "))
            if new_options == "y":
                second_set_of_choices = meal_chooser.make_choice(num_options)
                if len(second_set_of_choices) > 0:
                    print(second_set_of_choices)
                else:
                    print("Error - List empty, no options left")
                    break
            else:
                print("")
                print("Program stopped")


if __name__ == "__main__":
    main()

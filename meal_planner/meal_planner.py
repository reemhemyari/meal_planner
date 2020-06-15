import get_meals_from_file
import choose_meal


def main() -> None:
    meals = get_meals_from_file.get_stored_meals()

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
        chosen_meals = choose_meal.choose_meals(num_options)
        print(chosen_meals)

        # the while loop allows the user to regenerate options
        new_options = "y"
        while new_options == "y":
            new_options = str(input("Would you like to generate new options? (y/n): "))
            if new_options == "y":
                regenerated_choice = choose_meal.choose_meals(num_options)
                if len(regenerated_choice) > 0:
                    print(regenerated_choice)
                else:
                    print("Error - List empty, no options left")
                    break
            else:
                print("")
                print("Program stopped")


if __name__ == "__main__":
    main()

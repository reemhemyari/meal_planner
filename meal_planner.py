
def main():
    from get_meals_from_file import get_stored_meals
    from choose_meal import choose_meals

    meals = get_stored_meals()

    num_options = int(input("Enter a number of options you would like to be generated: "))

    # if statement ensures that the user chooses to generate at least one option, otherwise stopping the program
    if num_options < 1:
        print("Error - Number must be 1 or larger")
        print("Program stopped")
    elif num_options > len(meals):
        print("Error - There aren't that many options available")
        print("Program stopped")
    else:
        choose_meals(num_options)

        # the while loop allows the user to regenerate options
        new_options = "y"
        while new_options == "y":
            new_options = str(input("Would you like to generate new options? (y/n): "))
            if new_options == "y":
                choose_meals(num_options)
            else:
                print("Program stopped")


if __name__ == '__main__':
    main()

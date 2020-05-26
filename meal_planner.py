import csv
import random
meals = []


def generate_random_options(num_options):
    for option in range(0, num_options, 1):
        print(random.choice(meals))


def file_reader():
    global meals

    file = open('recipes.txt', 'r')
    meals = csv.reader(file)
    meals = [(line.strip()).split() for line in file]
    file.close()

    return


def main():
    file_reader()

    num_options = int(input("Enter a number of options you would like to be generated: "))

    # the if statement ensures that the user chooses to generate at least one option, otherwise stopping the program
    if num_options < 1:
        print("Error - Number must be 1 or larger")
        print("Program stopped")
    else:
        generate_random_options(num_options)

        # the while loop allows the user to regenerate options
        new_options = "y"
        while new_options == "y":
            new_options = str(input("Would you like to generate new options? (y/n): "))
            if new_options == "y":
                generate_random_options(num_options)
            else:
                print("Program stopped")


if __name__ == '__main__':
    main()

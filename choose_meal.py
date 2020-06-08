import random

meals = ["Chicken Fajitas", "Spaghetti", "Sweet Potato and Beans", "Salmon Pasta", "Fish Tacos",
         "Beef Tacos", "Chicken and Carrots", "Chicken Curry", "Salmon with Veg", "Roast Chicken",
         "Roast Beef", "Eat out", "Chicken and Leak pie", "Lentil Spinach Curry", "Chicken Stir-fry",
         "Veg Stir-fry", "Pasta Bake", "Home-made Pizza", "Beef Hot Pot", "Fried Chicken"]


class ChooseMeal:
    def choose_meals(self, num_options: int) -> str:
        for _ in range(0, num_options, 1):
            print(random.choice(meals))
        return random.choice(meals)

    if __name__ == '__main__':
        num_of_options = int(input("Enter a number of options you would like to be generated: "))
        choose_meals(None, num_of_options)

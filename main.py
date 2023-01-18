#print("Hello World!")

import random


Destinations = ["California", "Virginia", "New York", "Austrailia"]
Restaurants = ["Russo's", "Italiano's", "Green Seed Vegan", "Torchy's"]

#PURE FUNCTION
def random_trip_selection(list):
    user_validation = True
    while user_validation == True:
        trip_selection = random.choice(list)
        user_prompt = input(f"Do you like this selection {trip_selection}?")
        if user_prompt == "yes":
            print("We added this to your trip!")
            return trip_selection
        else:
            print("we will reselect for you!")

#VOID FUNCTION
def display_welcome():
    print("Welcome to the Day Trip Generator")



destination = random_trip_selection(Destinations)
resturant = random_trip_selection(Restaurants)





# answer = "no"

# while answer == "no":
#     for destination in Destinations:
#             choice_one = random.choice(Destinations)
#             print(choice_one)
#             break
#     answer = input("Do you like selected location? ")



# answer = "no"

# while answer == "no":
#     for restaurant in Restaurants:
#             choice_two = random.choice(Restaurants)
#             print(choice_two)
#             break
#     answer = input("Do you like selected restaurant? ")


# answer = "no"

# while answer == "no":
#     Transportation = ["Train", "Airplane", "Boat", "Teleport"]
#     for transportation in Transportation:
#             choice_three = random.choice(Transportation)
#             print(choice_three)
#             break
#     answer = input("Do you like selected mode of transportation? ")



# answer = "no"

# while answer == "no":
#     Entertainment = ["Sports", "Cooking", "Nature", "Movies"]
#     for entertainment in Entertainment:
#             choice_four = random.choice(Entertainment)
#             print(choice_four)
#             break
#     answer = input("Do you like selected form of entertainment? ")


# print("You have completed Day Trip Generator")

# print("Destination: " + choice_one)
# print("Restaurant: " + choice_two)
# print("Transportation: " + choice_three)
# print("Entertainment: " + choice_four)






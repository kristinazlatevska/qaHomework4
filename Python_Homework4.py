# Write a program that will print out your name.
# Write a program that will print out the first 10 numbers (by using a for loop).
def first10numbers():  # task 2
    for i in range(1, 11):
        print(i)


# Write a program that will print out the first 10 odd numbers (by using a for loop).
def first10odd():  # task 3
    for i in range(1, 21, 2):
        print(i)


# Write a program that will ask the user to enter a number. Print out that number multiplied by 2.
def multiply_by_two():  # task 4
    user_input = float(input("Enter a number: "))
    user_input = int(user_input)
    result = user_input * 2
    print(f"The result of {user_input} multiplied by 2 is: {result}")


# Write a program that will ask the user to enter their name. Print out how many characters are in their name.
def name_characters():  # task5
    user_name = input("Enter your name: ")
    characters = len(user_name)
    print(f"Your name has {characters} characters")


if __name__ == '__main__':

    print('Kristina\n')  # task1

    first10numbers() # task2
    print('\n')

    first10odd()  # task3
    print('\n')

    multiply_by_two()  # task4
    print('\n')

    name_characters()  # task5



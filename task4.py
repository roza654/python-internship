import random

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    
    n = int(input("Enter your choice: "))

    
    while n> 3 or n < 1:
        n = int(input('Enter a valid choice please : '))

    
    if n == 1:
        n_name = 'Rock'
    elif n == 2:
        n_name = 'Paper'
    else:
        n_name = 'Scissors'

    
    print('User choice is:', n_name)
    print("Now it's Computer's Turn...")

    
    comp_choice = random.randint(1, 3)

    
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer choice is:", comp_choice_name)
    print(n_name, 'vs', comp_choice_name)


    if n== comp_choice:
        result = "DRAW"
    elif (n == 1 and comp_choice == 2) or (comp_choice == 1 and n == 2):
        result = 'Paper'
    elif (n == 1 and comp_choice == 3) or (comp_choice == 1 and n== 3):
        result = 'Rock'
    elif (n == 2 and comp_choice == 3) or (comp_choice == 2 and n == 3):
        result = 'Scissors'

    
    if result == "DRAW":
        print("<== It's a tie! ==>")
    elif result == n_name:
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break


print("Thanks for playing!")

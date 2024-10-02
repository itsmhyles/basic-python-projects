def adventure_game():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself at a crossroad in a dark forest.")

    while True:
        choice = input("Do you want to go left, right, or straight ahead? (l/r/s): ").lower()

        if choice == 'l':
            print("You chose to go left.")
            print("You encounter a friendly wizard who grants you a magic wand.")
            print("Congratulations! You win the game!")
            break
        elif choice == 'r':
            print("You chose to go right.")
            print("You fall into a pit filled with snakes. Game Over!")
            break
        elif choice == 's':
            print("You chose to go straight ahead.")
            print("You find a treasure chest, but it's guarded by a dragon.")
            fight_choice = input("Do you want to fight the dragon? (y/n): ").lower()
            if fight_choice == 'y':
                print("You defeat the dragon and claim the treasure. You win!")
            else:
                print("You run away. The game ends.")
            break
        else:
            print("Invalid choice. Please choose l, r, or s.")

adventure_game()
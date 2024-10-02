import random

def rock_paper_scissors_game():
    choices = ['Rock', 'Paper', 'Scissors']
    
    print('Welcome to Rock Paper Scissors!')
    
    while True:
        print('\nMake your choice:')
        for i, choice in enumerate(choices, 1):
            print(f'{i}. {choice}')
        
        user_choice = input('Enter the number of your choice (or q to quit): ')
        
        if user_choice.lower() == 'q':
            break
        
        try:
            user_choice = choices[int(user_choice) - 1]
            computer_choice = random.choice(choices)
            
            print(f'\nYou chose: {user_choice}')
            print(f'Computer chose: {computer_choice}')
            
            if user_choice == computer_choice:
                print('It\'s a tie!')
            elif ((user_choice == 'Rock' and computer_choice == 'Scissors') or
                  (user_choice == 'Paper' and computer_choice == 'Rock') or
                  (user_choice == 'Scissors' and computer_choice == 'Paper')):
                print('You win!')
            else:
                print('Computer wins!')
        except (ValueError, IndexError):
            print('Invalid choice. Please try again.')

rock_paper_scissors_game()
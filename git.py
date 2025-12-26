# Dice Rolling Simulator - Basic Python
import random

def show_menu():
    """Show main menu."""
    print("\n" + "*" * 40)
    print("     DICE ROLLING SIMULATOR")
    print("*" * 40)
    print("1. Roll a single dice")
    print("2. Roll multiple dice")
    print("3. Play vs Computer")
    print("4. Play Target Game")
    print("5. Exit")
    print("*" * 40)

def roll_single_dice():
    """Roll one dice."""
    print("\n--- Roll Single Dice ---")
    
    # Ask for dice sides
    while True:
        try:
            sides = int(input("Enter number of sides (2-20): "))
            if 2 <= sides <= 20:
                break
            else:
                print("Please enter between 2 and 20")
        except:
            print("Please enter a valid number")
    
    # Roll the dice
    input("\nPress Enter to roll the dice...")
    roll = random.randint(1, sides)
    
    print(f"\nYou rolled: {roll}")
    
    # Show simple dice face
    print("   _______")
    if roll == 1:
        print("  |       |")
        print("  |   *   |")
        print("  |_______|")
    elif roll == 2:
        print("  | *     |")
        print("  |       |")
        print("  |_____*_|")
    elif roll == 3:
        print("  | *     |")
        print("  |   *   |")
        print("  |_____*_|")
    elif roll == 4:
        print("  | *   * |")
        print("  |       |")
        print("  |_*___*_|")
    elif roll == 5:
        print("  | *   * |")
        print("  |   *   |")
        print("  |_*___*_|")
    elif roll == 6:
        print("  | *   * |")
        print("  | *   * |")
        print("  |_*___*_|")
    else:
        print("  |       |")
        print(f"  |   {roll}   |")
        print("  |_______|")
    
    input("\nPress Enter to continue...")

def roll_multiple_dice():
    """Roll multiple dice."""
    print("\n--- Roll Multiple Dice ---")
    
    # Ask for number of dice
    while True:
        try:
            num_dice = int(input("How many dice? (1-10): "))
            if 1 <= num_dice <= 10:
                break
            else:
                print("Please enter between 1 and 10")
        except:
            print("Please enter a valid number")
    
    # Ask for dice sides
    while True:
        try:
            sides = int(input("Enter number of sides per dice (2-20): "))
            if 2 <= sides <= 20:
                break
            else:
                print("Please enter between 2 and 20")
        except:
            print("Please enter a valid number")
    
    # Roll all dice
    input(f"\nPress Enter to roll {num_dice} dice...")
    
    rolls = []
    total = 0
    
    print("\nRolling dice:", end=" ")
    
    for i in range(num_dice):
        roll = random.randint(1, sides)
        rolls.append(roll)
        total += roll
        print(roll, end=" ")
    
    print(f"\n\nIndividual rolls: {rolls}")
    print(f"Total of all dice: {total}")
    
    # Check for special results
    if num_dice == 2:
        if rolls[0] == rolls[1]:
            print("🎯 You got doubles!")
        if total == 7:
            print("✨ Lucky 7!")
        if total == 2:
            print("🐍 Snake eyes!")
    
    input("\nPress Enter to continue...")

def play_vs_computer():
    """Player vs Computer game."""
    print("\n--- Player vs Computer ---")
    print("First to reach 50 points wins!")
    
    player_score = 0
    computer_score = 0
    round_num = 1
    
    while player_score < 50 and computer_score < 50:
        print(f"\n--- Round {round_num} ---")
        print(f"Player: {player_score}   Computer: {computer_score}")
        
        # Player's turn
        input("\nYour turn - Press Enter to roll...")
        player_roll = random.randint(1, 6)
        print(f"You rolled: {player_roll}")
        player_score += player_roll
        
        # Computer's turn
        print("\nComputer's turn...")
        computer_roll = random.randint(1, 6)
        print(f"Computer rolled: {computer_roll}")
        computer_score += computer_roll
        
        round_num += 1
        
        if player_score >= 50 or computer_score >= 50:
            break
    
    print("\n" + "=" * 40)
    print("GAME OVER!")
    print(f"Final Score - Player: {player_score}, Computer: {computer_score}")
    
    if player_score > computer_score:
        print("🏆 YOU WIN! 🏆")
    elif computer_score > player_score:
        print("💻 Computer wins!")
    else:
        print("🤝 It's a tie!")
    
    input("\nPress Enter to continue...")

def play_target_game():
    """Try to reach target score."""
    print("\n--- Target Game ---")
    print("Try to reach the target score in as few rolls as possible!")
    
    target = random.randint(20, 50)
    print(f"Target score: {target}")
    
    score = 0
    rolls = 0
    history = []
    
    while score < target:
        print(f"\nCurrent score: {score}")
        print(f"Still need: {target - score}")
        
        # Ask how many dice
        while True:
            try:
                num_dice = int(input("How many dice to roll? (1-3): "))
                if 1 <= num_dice <= 3:
                    break
                else:
                    print("Please enter between 1 and 3")
            except:
                print("Please enter a valid number")
        
        input(f"\nPress Enter to roll {num_dice} dice...")
        
        # Roll dice
        roll_total = 0
        current_rolls = []
        
        for i in range(num_dice):
            roll = random.randint(1, 6)
            current_rolls.append(roll)
            roll_total += roll
        
        rolls += 1
        score += roll_total
        history.append(f"Roll {rolls}: {current_rolls} = {roll_total}")
        
        print(f"You rolled: {current_rolls}")
        print(f"This roll: {roll_total}")
        print(f"New total: {score}")
        
        if score > target:
            print(f"\nOh no! You went over by {score - target} points!")
            print("Game over!")
            break
    
    if score == target:
        print("\n🎯 PERFECT! You hit the target exactly!")
    
    if score >= target:
        print(f"\nYou reached {score} in {rolls} rolls")
        print("\nYour rolls:")
        for h in history:
            print(f"  {h}")
    
    input("\nPress Enter to continue...")

def show_stats():
    """Show statistics."""
    print("\n=== GAME STATISTICS ===")
    print("1. Dice with 6 sides:")
    print("   Average roll: 3.5")
    print("   Most common: All equal chance")
    print("\n2. Dice Probabilities:")
    print("   Rolling 2 dice:")
    print("   7 is most common (16.7%)")
    print("   2 and 12 are least common (2.8%)")
    print("\n3. Fun Facts:")
    print("   - Opposite sides of a dice always add to 7")
    print("   - The dots on dice are called 'pips'")
    print("   - Casinos use 5 dice for craps")

def main():
    """Main game loop."""
    print("Welcome to Dice Rolling Simulator!")
    
    while True:
        show_menu()
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            roll_single_dice()
        elif choice == '2':
            roll_multiple_dice()
        elif choice == '3':
            play_vs_computer()
        elif choice == '4':
            play_target_game()
        elif choice == '5':
            print("\nThanks for playing! Goodbye!")
            break
        else:
            print("\nInvalid choice! Please enter 1-5")
            continue
        
        # Ask if user wants to see stats
        if choice in ['1', '2', '3', '4']:
            see_stats = input("\nWould you like to see dice statistics? (y/n): ").lower()
            if see_stats == 'y':
                show_stats()
                input("\nPress Enter to continue...")

# Start the game
if __name__ == "__main__":
    main()

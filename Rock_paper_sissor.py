import random 

print("\n--------Rock Paper Scissor --------\n")

print("Instructions:\n R = Rock\n P = Paper\n S = Scissor\n ")
choices = {'R':'Rock',
           'P':'Paper',
           'S':'Scissor'
           }
run = True
score = 0

def display():
   print(f"Bot choice: {choices[bot_choice]} and Your choice: {choices[player_choice]}")
   print("Score:",score)
   print("________________________")


while run:
    bot_choice = random.choice(list(choices))
    player_choice = input("Enter your choice(R/P/S or exit):").upper()

    if player_choice == 'R' :
        if bot_choice == 'S':
            print("🟢 You Win 🟢")
            score += 1
        elif bot_choice == 'P':
            print("🔴 You Lose 🔴")
            score -= 1
        else:
            print("🟡 Draw 🟡")    
        display()
    elif player_choice == 'P' :
        if bot_choice == 'R':
            print("🟢 You win 🟢")
            score += 1
        elif bot_choice == 'S':
            print("🔴 You Lose 🔴") 
            score -= 1
        else:    
            print("🟡 Draw 🟡")      
        display()     
    elif player_choice == 'S' :
        if bot_choice == 'R':
            print("🟢 You Win 🟢")
            score += 1 
        elif bot_choice == 'P':
            print("🔴 You Lose 🔴")  
            score -= 1
        else:
            print("🟡 Draw 🟡")      
        display()           
    elif player_choice == 'EXIT':
        print("⚪️ Game over , your score is:", score ,"⚪️")
        run = False
    else:
        print("🙏🏻 Please aise kuch bhi mat enter mat karo na yaar 🥹")
        








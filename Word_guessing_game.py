import random 
print("\n--------Word guessing game--------")

#
words = ["Python","Script","Binary","Debug","Server","Coding","Deploy","Socket","Github","Kernel","Banana"]
word = random.choice(words)
length = len(word)
turns = 5
disp_text = "_" * length 
while turns > 0 :
    letter = input("\nEnter your guess : ")

    if letter.lower() in word.lower():
        indices = [i for i, ltr in enumerate(word.lower()) if ltr == letter.lower()]
        for i in indices:
            s = disp_text[:i] + letter + disp_text[i+1:]   
            disp_text = s
        print("***** Good job *****")
    else:    
        print("***** Oops Wrong guess 😅 *****")
        turns -= 1
    print(disp_text)
    print(f"\n--You have {turns} turns left--")
    if word.lower() == disp_text:
        print("✨✨✨✨✨ Congratulations, you won ✨✨✨✨✨")
        turns = 0 
    elif turns == 0 :
        print("🥲 You lose, Try again 🥲")    
    print("______________________________")           

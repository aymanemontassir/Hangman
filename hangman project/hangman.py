import random as rnd
def check_word(word,answer):
    if word == answer:
        return True
    else:
        return False
    
def print_menu():
    print("H A N G M A N\nThe game will be available soon.")
# -------------------------------------
print_menu()
words = ('python',"java","swift","javascript")
i = round(rnd.uniform(0,3))
answer = words[i]

word = input("Guess the word:") 
if check_word(word,answer) == True:
    print("You survived!")
else:
    print("You lost!") 

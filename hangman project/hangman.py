def check_word(word,answer):
    if word == answer:
        return True
    else:
        return False
    
def print_menu():
    print("H A N G M A N\nThe game will be available soon.")
# -------------------------------------
print_menu()
x = input("Guess the word:") 
if check_word(x,"python") == True:
    print("You survived!")
else:
    print("You lost!") 

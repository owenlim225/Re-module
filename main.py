import re
import time
import os
import sys


#Clear screen
def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
        
class select:
    def __init__(self):
        pass

#A Ask the user to input a string and check if the string starts with a small letter and ends with a non=digit and non-letter character using regex. 
    def str_scanner(self):
        #INPUT
        print()
        user_input = input("Enter a string: ")
        
        pattern = r'^[a-z].*[^\w\d]$'
        
        #OUTPUT
        if re.match(pattern, user_input):
            print("Valid string!")
            time.sleep(3)            
            clear_screen()
        else:
            print("Invalid string.")
            time.sleep(3)
            clear_screen()
            

#B Ask the user to input a paragprah. Using regex, replace the negative words hate, angry, bully, punch, and rant with "-". 
    def rem_nega(self):
        n_words =["hate", "angry", "bully", "punch", "rant"]
        pattern = r'\b(?:' + '|'.join(n_words) + r')\b'
        
        #INPUT
        print()
        user_input = input("Enter a paragraph: ")
        update_input = re.sub(pattern, "-", user_input, flags=re.IGNORECASE)
        
        #OUTPUT
        print("Updated paragraph:", update_input)
        time.sleep(3)
        clear_screen()

#C Ask the user to input two string, a and b. check if b exist in a using regex.
    def sub_string(self):
        #INPUT
        print()
        input_a = input("Enter string a: ")
        input_b = input("Enter string b: ")
        
        input_b = re.escape(input_b)
        is_match = re.search(input_b, input_a)
        
        #OUTPUT
        if is_match:
                print()
                print(f"{input_b} found in {input_a}!")
                time.sleep(3)
                clear_screen()               
        else:
                print()
                print(f"{input_b} not found in {input_a}.")
                time.sleep(3)
                clear_screen()
    
    
    

if __name__ == "__main__":
    while True:      
        user_input = input("\nChoose your program:\n \nA) Utilize a string scanner \nB) Eliminate negativity from strings \nC) Extract substrings\n \nD) Exit\n \nProgram: ").lower()

    
        check = select()
        
        if user_input == "a":
            check.str_scanner()
            continue
        elif user_input == "b":
            check.rem_nega()
            continue
        elif user_input == "c":
            check.sub_string()
            continue
        elif user_input == "d":
            break
        else:
            print("Invalid Input")
            print()
            continue



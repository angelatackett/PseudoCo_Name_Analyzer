# This program is going to evaluate the users imaginary company name and identify
# special characters, capitalize the first letter of the words, and determine if
# the user's initials are found within the input.
# Developer : Angela D. Tackett        CMIS 102              25JUN22

def main():

    #display_welcome
    welcome()
    #prompt user inputs
    format_name = name_input()
    #count characters_vowels
    v_count,char_count = Counts(format_name)
    #initials prompt
    init_ver,init = initials_ver(format_name)
    #display findings
    anal_display(format_name,v_count,char_count,init_ver,init)

    
#functions ------------------------------
def welcome():
    print('\nWelcome to the PseudoCo Name Analyzer!\n')
     
#business name proposal cleanup -
def name_input():
    #prompt for business name and intials
    name = input('Enter imaginary business name: ')
    while True:
        if len(name) < 1:
            name = input('Enter imaginary business name: ')
        else:
            break
    #remove unnecessary spaces & capitalize
    format_name = name.lower().strip().title()
    return format_name

    return format_name

#analyze chosen name-----------------------
def Counts(format_name):
    #count vowels
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    v_count = 0
    for letter in format_name:
        if letter in vowel:
            v_count = v_count + 1
    #count characters
    char_count = len(format_name)
    return v_count,char_count

#initials ------------------------------------
def initials_ver(format_name):
    init = input('Enter your first and last name initials [2 letter]: ')
    while True:
        if init.isalpha() and len(init) == 2:
            break
        else:
            init = input('Enter your first and last name initials [2 letter]: ')

    init_ver = True
    for letter in init:
        if letter.lower() in format_name.lower():
            init_ver = 'present'
        else:
            init_ver = 'NOT present'
            
    return init_ver,init
    

#display analysis ---------------------------
def anal_display(format_name,v_count,char_count,init_ver,init):
    print('\n*****************************************************************************')
    print(f'\nPseudo Name:  {format_name}\nCharacter Count: {char_count}\nVowel Count: {v_count}\nInitials: {init.upper()}')
    print(f'\nThe combination of letters in your initials are {init_ver} within the name.') 

main()
    

    
    

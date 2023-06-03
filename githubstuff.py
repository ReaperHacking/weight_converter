#Weight Converter (KG to LB vice versa)
#Enjoy :)

print("Welcome to my weight converter! Below just type in if you want to convert KG to LB or LB to KG! \n")

#Function for the weight conversion and conditionals for them
def conversion(kg_or_lb):
    if kg_or_lb == 'K':
        kg = int(input("How much weight from KG ?: "))
        kg_form = kg * 2.2
        print(f'The number you provided in KG, is {kg_form} LB!')

    elif kg_or_lb == 'L':
        lb = int(input("How much weight from LB?: "))
        lb_form = lb / 2.2
        print(f'The number you provided in LB, is {lb_form} KG!')

    else:
        print("Sorry, invalid letter or character, supposed to be K or L, try again :/")

#Restarting functions and while loop
re_do = "Y"

while re_do == "Y":
    kg_or_lb = input("Would you like to convert to (K)KG or (L)LB?: ").upper()
    conversion(kg_or_lb)

#Asks users if they would like to restart the program with conditionals
    re_measure = input("Would you like to convert the weights again? (Y/N):").upper()
    if re_measure == "N":
        break
    elif re_measure == "Y":
        continue
    else:
        print("Sorry, invalid option, either Y or N, try again :/")
        break
    

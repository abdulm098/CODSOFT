import random
print("Welcome to password generator")
letters=["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','&',"*"]
letter=int(input("How many letters would you like in your password?\n  "))
symbol=int(input("How many symbols?\n  "  ))
number=int(input("How many numbers?\n   "))
password=""
#Generate random letters in the password
for i in range(1,letter+1):
    random_letter=random.choice(letters)
    password=password+random_letter

#Generate random Symbols in the password
for i in range(0,symbol+1):
    random_symbol=random.choice(symbols)
    password=password+random_symbol

#Generate random numbers in the password
for i in range(0,number+1):
    random_numbers=random.choice(numbers)
    password=password+random_numbers

#print the generated password    
print(password)    


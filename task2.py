import random
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
ui_letters = int(input("How many letters would you like in your password\n"))
ui_symbols = int(input("How many symbols would you like?\n"))
ui_numbers = int(input("How many numbers would you like?\n"))

password = ""

for char in range(1, ui_letters + 1 ):
    temp_char = random.choice(alphabets)
    password += temp_char
for sym in range(1, ui_symbols + 1):
    temp_sym = random.choice(symbols)
    password += temp_sym
for num in range(1, ui_numbers + 1 ):
    temp_num = random.choice(numbers)
    password += temp_num


pass_list = list(password)
random.shuffle(pass_list)

new_pass = ""
for i in pass_list:
    new_pass += i
print(new_pass)
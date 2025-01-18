import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

count_letters = int(input("How many letters would you like in your password?\n"))
count_symbols = int(input("How many symbols would you like?\n"))
count_numbers = int(input("How many numbers would you like?\n"))

# easy
# password = " "
# for chair in range(1, count_letters + 1):
#     password += random.choice(letters)
#
# for chair in range(1, count_symbols + 1):
#     password += random.choice(letters)
#
# for chair in range(1, count_numbers + 1):
#     password += random.choice(letters)
#
# print(password)

# hard

password_list = []
password = ''
for chair in range(1, count_letters + 1):
    password_list.append(random.choice(letters))

for chair in range(1, count_symbols + 1):
    password_list.append(random.choice(symbols))

for chair in range(1, count_numbers + 1):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)
for char in password_list:
    password += char

print(f'Your password is: {password}')

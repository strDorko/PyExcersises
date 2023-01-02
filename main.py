# Only print even index letters

str = input("What work would you like to check: ")


for letter in str:
    if int(str.find(letter)) % 2 == 0:
        print(letter)


# remove "X" amount of letters from the beginning
removal_str = input("Write a word to have their letters removed: ")
remove_range = int(input("Now write the ammount of letters to remove: "))

removal_str = removal_str[remove_range:]

print(removal_str)


# Write a program to check how many times something appears in a text.
text_input = input("What text do you want to input? ")
word_check = input("What word do you want to find in the text? ")

word_count = text_input.count(word_check)
print(word_count)

#Print as many numbers as the value itself
for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print("\n")

#Check if the number is a palindrom

palindrome_num = input("Input which int you would like to check ")
if palindrome_num[-1] == palindrome_num[0]:
    print("Its a palindrome")
else:
    print("Its not a palindrome")

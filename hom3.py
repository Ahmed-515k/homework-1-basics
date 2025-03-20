text = input("Enter a string :")
vowel = "aAeEiIoOuU"
count = 0
for char in text:
    if char in vowel :
        count = count +1
print("Number of vowel :",count)

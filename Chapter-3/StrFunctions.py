name = "Tafsir Chy"

print(len(name)) # get the length of the string

print(name.endswith("sir")) # check if the string ends with "sir"
print(name.endswith("SIR")) # check if the string ends with "SIR"
print(name.startswith("Taf")) # check if the string starts with "Taf"
print(name.startswith("taf")) # check if the string starts with "taf"

print(name.upper()) # convert the string to uppercase
print(name.lower()) # convert the string to lowercase

print(name.isupper()) # check if the string is in uppercase
print(name.islower()) # check if the string is in lowercase

print(name.title()) # convert the string to title case

print(name.count("a")) # count the number of occurrences of "a" in the string

print(name.index("f")) # find the index of the first occurrence of "f"

print(name.find("s")) # find the index of the first occurrence of "s"

print(name.capitalize()) # capitalize the first character of the string

print(name.strip()) # remove leading and trailing whitespace from the string

print(name.split("a")) # split the string into a list using "a" as the delimiter

print(name.join(["Hello", "World"])) # join the list of strings with "Tafsir" as the separator

print(name.find("sir")) # find the index of the first occurrence of "sir"

print(name.replace("Taf", "Tafsir")) # replace "Taf" with "Tafsir"

# --------------------------------------------------------------------------------------------------

text = "  Hello Python  "
text2 = "hello world"
text3 = "banana"
text4 = "12345"
text5 = "Python123"

# 1. lower() - Convert to lowercase
print(text.lower())
# Output: "  hello python  "

# 2. upper() - Convert to uppercase
print(text.upper())
# Output: "  HELLO PYTHON  "

# 3. strip() - Remove spaces from both ends
print(text.strip())
# Output: "Hello Python"

# 4. replace() - Replace part of a string
print(text.replace("Python", "World"))
# Output: "  Hello World  "

# 5. split() - Convert string into a list
print(text.strip().split())
# Output: ['Hello', 'Python']

# 6. join() - Join list elements into a string
words = ["Hello", "Python"]
print(" ".join(words))
# Output: Hello Python

# 7. find() - Find the first occurrence of a substring
print(text.find("Python"))
# Output: 8

# 8. count() - Count occurrences
print(text3.count("a"))
# Output: 3

# 9. startswith() - Check if string starts with something
print(text.strip().startswith("Hello"))
# Output: True

# 10. endswith() - Check if string ends with something
print(text.strip().endswith("Python"))
# Output: True

# 11. isalpha() - Only letters?
print("Python".isalpha())
# Output: True

print("Python123".isalpha())
# Output: False

# 12. isdigit() - Only digits?
print(text4.isdigit())
# Output: True

print("123abc".isdigit())
# Output: False

# 13. isalnum() - Letters and digits only?
print(text5.isalnum())
# Output: True

print("Python 123".isalnum())
# Output: False

# 14. title() - Capitalize the first letter of every word
print(text2.title())
# Output: Hello World

# 15. capitalize() - Capitalize only the first letter
print(text2.capitalize())
# Output: Hello world
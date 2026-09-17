# Dictionaries

# Lists are looked up by index
my_list = ["A", "B", "c"]
print(my_list[1])

# A dictionary is used when we want to
# look up an element using a specific key
letter_value = {"E":1, "T":1, "A":1}
# Any type but have to be integers to add points 

# We can store something later using
# dict[key] = value
letter_value["D"] = 2
print(letter_value)
# letter value is already global
# string and lists have specific order
# dictionaries dont

#not the position, letters matter
# SHOULD HAVE SOMETHING TO KEEP TRack

def word_value(word):
    total = 0
    for letter in word:
        value = letter_value[letter]
        total += value
        
    return total

print(word_value("DATE"))

# have to initialize the variable before using it in a loop
# can't write steps in a return function

# when using something... and .append or anyother function, return the original variable stored than the new one
# logical and syntax errors
# try to find alternatives
# double checking my work
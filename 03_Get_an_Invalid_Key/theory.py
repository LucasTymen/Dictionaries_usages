"""

Using Dictionaries
Get an Invalid Key

Let’s say we have our dictionary of building heights from the last exercise:

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

What if we wanted to know the height of the Landmark 81 in Ho Chi Minh City? We could try:

print(building_heights["Landmark 81"])

But "Landmark 81" does not exist as a key in the building_heights dictionary! So this will throw a KeyError:

KeyError: 'Landmark 81'

One way to avoid this error is to first check if the key exists in the dictionary:

key_to_check = "Landmark 81"

if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

This will not throw an error, because key_to_check in building_heights will return False, and so we never try to access the key.
Instructions
1.

Review the code in the editor and predict what the output will be. Run the code to see if you are correct!
2.

Because "energy" is not a key in zodiac_elements, a KeyError is thrown in the terminal!

Using an if statement, check if "energy" is a key in zodiac_elements. Nest the existing print() statement within the if statement so that it will only execute if "energy" is a key.

Run your code again. This time, there should be no errors in the terminal!
3.

Add the key "energy" to the zodiac_elements. It should map to a value of "Not a Zodiac element". Run the code. Since "energy" is now a key, its value prints to the terminal!
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""

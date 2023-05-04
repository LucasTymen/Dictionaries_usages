"""

Using Dictionaries
Get All Values

Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!)
with all of the values in the dictionary. It can be used in the place of a list for iteration:
"""

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

for score_list in test_scores.values():
  print(score_list)

"""
will yield:

[80, 72, 90]
[88, 68, 81]
[80, 82, 84]
[98, 96, 95]
[78, 80, 78]
[64, 60, 75]

There is no built-in function to get all of the values as a list, but if you really want to, you can use:
"""

list(test_scores.values())

"""
However, for most purposes, the dict_values object will act the way you want a list to act.
Instructions
1.

Create a variable called total_exercises and set it equal to 0.
2.

Iterate through the values in the num_exercises list and add each value to the total_exercises variable.
3.

Print the total_exercises variable to the console.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""

"""
Using Dictionaries
Get All Items

You can get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list
object. Each element of the dict_list returned by .items() is a tuple consisting of:

(key, value)

so to iterate through, you can use this syntax:
"""
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
"""
which would yield this output:

Apple has a value of 184 billion dollars.
Google has a value of 141.7 billion dollars.
Microsoft has a value of 80 billion dollars.
Coca-Cola has a value of 69.7 billion dollars.
Amazon has a value of 64.8 billion dollars.

Instructions
1.

Use a for loop to iterate through the items of pct_women_in_occupation. For each key : value pair, print out a string
that looks like:

Women make up [value] percent of [key]s.

Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""

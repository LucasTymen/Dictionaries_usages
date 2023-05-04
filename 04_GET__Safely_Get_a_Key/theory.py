"""
Using Dictionaries
Safely Get a Key

We saw in the last exercise that we had to add a key:value pair to a dictionary in order to avoid a KeyError. This
solution is not sustainable. We can’t predict every key a user may call and add all of those placeholder values to our
dictionary!

Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the
key you are trying to .get() does not exist, it will return None by default:
"""

building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

#this line will return 632:
building_heights.get("Shanghai Tower")

#this line will return None:
building_heights.get("My House")

"""
You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height
of 0 if our desired building is not in the dictionary:
"""

building_heights.get('Shanghai Tower', 0)
# 632
building_heights.get('Mt Olympus', 0)
# 0
building_heights.get('Kilimanjaro', 'No Value')
# 'No Value'

"""
Instructions
1.

Use .get() to get the value of "teraCoder"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it
in a variable called tc_id. Print tc_id to the console.
2.

Use .get() to get the value of "superStackSmash"‘s user ID, with 100000 as a default value if the user doesn’t exist.
Store it in a variable called stack_id. Print stack_id to the console.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""

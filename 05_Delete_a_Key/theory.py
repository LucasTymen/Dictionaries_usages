"""

Using Dictionaries
Delete a Key

Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this
dictionary mapping ticket numbers to prizes:
"""

raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}

"""
When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize
has been given away. We can use .pop() to do this. Just like with .get(), we can provide a default value to return if
the key does not exist in the dictionary:
"""

raffle.pop(320291, "No Prize")
# "Gift Basket"
raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
raffle.pop(100000, "No Prize")
# "No Prize"
raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
raffle.pop(872921, "No Prize")
# "Concert Tickets"
raffle
{223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}

"""
.pop() works to delete items from a dictionary, when you know the key value.
Instructions
1.

You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player’s
inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains"
to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist,
add 0 to health_points.
2.

In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not
exist, add 0 to health_points.
3.

In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does
not exist, add 0 to health_points.
4.

Print available_items and health_points.
Concept Review
Want to quickly review some of the concepts you’ve been learning? Take a look at this material's cheatsheet!

"""

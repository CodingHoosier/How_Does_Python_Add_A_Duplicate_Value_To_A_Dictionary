# https://www.youtube.com/watch?v=avixY34zzGw
# How Does Python Add A Duplicate Value To A Dictionary?
# Create a dictionary...
# Two keys have the same value.
# That's perfectly OK. 
CPUs = {"Pentium":"Intel",
        "Ryzen": "AMD",
        "A4": "Apple",
        "M6":"Apple"}
# Let's see what we have so far:
print(f"CPUs: {CPUs}")
# Add another key and value:
#  the value is a duplicate.
CPUs["Core I7"] = "Intel"
print(f"CPUs: {CPUs}")
# Of course, a duplicate key
#  is not allowed.
# The old value is overwitten.
CPUs["Core I7"] = "Apple"
print(f"CPUs: {CPUs}")
# Extract the values into a set.
#  This removes duplicates
values = set(CPUs.values())
print(f"value set: {values}")
# Extract the values into a list.
# This does not 
#  remove duplicates.
values = list(CPUs.values())
print(f"value list: {values}")

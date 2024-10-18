# This program attempts to make an intentional index error.

colors = ["Red", "Blue", "Green"]
print(colors[3])

# Output:
# Traceback (most recent call last):
#   File "/home/marco/Programming/python_learn/3-11_intentional_error.py", line 4, in <module>
#     print(colors[3])
#           ~~~~~~^^^
# IndexError: list index out of range
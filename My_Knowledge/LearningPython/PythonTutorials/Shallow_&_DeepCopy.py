import copy

color1 = ["Red", "Blue"]
color2 = ["White", "Black"]
color3 = [color1, color2]

# --> normal copy
color4 = color3
print(id(color3) == id(color4))
print(id(color3[0]) == id(color4[0]))

# Shallow copy
color4 = copy.copy(color3)
print("Color 4: ", color4)
print("Shallow copy: ", id(color3) == id(color4)) # => False - color4 is now a new project
print(id(color3[0]) == id(color4[0]))             # => True = The new variables refers to original variable

# Deep Copy
color4 = copy.deepcopy(color3)
print("Deep copy color4 is ", color4)
print("Id Color3: {0} and Id color4: {1}", id(color3), id(color4))
print("Deep copy: ", id(color3) == id(color4))
print(id(color3[0]) == id(color4[0]))

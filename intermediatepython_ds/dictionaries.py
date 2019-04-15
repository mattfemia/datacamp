
# List strategy to connect two data sets (Order matters)

pop = [30.55, 2.77, 39.21]
countries = ["afghanistan", "albania", "algeria"]

ind_alb = countries.index("albania")

print(ind_alb)
print(pop[ind_alb])


# Dictionary strategy (Order doesn't matter)

world = {"afghanistan": 30.55, "albania": 2.77, "algeria":39.21}
print(world["albania"])

print(world.keys()) # prints out all of the keys


world["sealand"]= 0.000027 # Appending dict
print(world)

print("sealand" in world) # Check to see if key is in dict

del(world["sealand"])
print(world)


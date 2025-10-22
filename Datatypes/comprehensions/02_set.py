# chai_flavors = ["ginger chai","masala chai","mint chai","ginger chai","normal chai","black tea","mint chai"]

# unique_chai_flavors = { chai for chai in chai_flavors}
# print(unique_chai_flavors)



recipes = {
    "masala chai":["ginger","cardamon","clove"],
    "elaichi chai":["elaichi","cardamon","milk"],
    "spicy chai":["ginger","black pepper","clove"]
}

print(recipes.values())

unique_items = {item for chai in recipes.values() for item in chai}

print(unique_items)
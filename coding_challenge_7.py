
def add_element(dict, key, value):
    if key not in dict:
        dict[key] = value


product = {}
add_element(product, "Apple", 200)
add_element(product, "Orange", 300)
add_element(product, "Grapes", 350)
add_element(product, "Watermelon", 400)
for i in product.values():
    print(i)
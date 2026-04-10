# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

candy1 = items[:9]       # Bubblegum
candy2 = items[11:20]    # Chocolate
dry_goods = items[22:]    # Pasta

# 2. Slice the `categories` string into individual categories
category1 = categories[:11]  # Candy Aisle
category2 = categories[13:]  # Pasta Aisle

# 3. Define price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

# 4. Print the statements
print("We have " + candy1 + " for " + bubblegum_price + " in the " + category1)
print("We have " + candy2 + " for " + chocolate_price + " in the " + category1)
print("We have " + dry_goods + " for " + pasta_price + " in the " + category2)

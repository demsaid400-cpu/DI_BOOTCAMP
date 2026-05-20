# ==========================================
# Challenge 1
# Count the number of occurrences of each letter
# and store their positions in a dictionary.
# ==========================================

word = input("Enter a word: ")

letter_indexes = {}

for index, letter in enumerate(word):
    if letter not in letter_indexes:
        letter_indexes[letter] = []

    # Add the current index to the list
    letter_indexes[letter].append(index)

print(letter_indexes)


# ==========================================
# Challenge 2
# Create a shopping basket based on the
# items that can be afforded.
# ==========================================

items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

# Convert wallet amount to an integer
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

basket = []

for item, price in items_purchase.items():
    # Convert item price to an integer
    item_price = int(price.replace("$", "").replace(",", ""))

    # Add the item if it can be afforded
    if item_price <= wallet_amount:
        basket.append(item)

# Sort the basket alphabetically
basket.sort()

# Print the result
if basket:
    print(basket)
else:
    print("Nothing"))

#Challenge 1: Letter Index Dictionary

user_word = input("Enter a word : ")

letter_indices = {}

for index, letter in enumerate(user_word):
    if letter in letter_indices:
        letter_indices[letter].append(index)
    else:
        letter_indices[letter] = [index]

print(letter_indices)



#Challenge 2: Affordable Items

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet_str = "$300"
wallet = int(wallet_str.replace("$", "").replace(",", ""))
basket = []

for item, price_str in items_purchase.items():
    item_price = int(price_str.replace("$", "").replace(",", ""))
    if wallet >= item_price:
        basket.append(item)
        wallet -= item_price

if len(basket) == 0:
    print("Nothing")
else:
    print(sorted(basket))
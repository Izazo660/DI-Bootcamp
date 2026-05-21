import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]

target_number   = 3728

seen_numbers = set()

printed_pairs = set()

print(f"Searching for pairs that sum up to {target_number}...\n")

for num in list_of_numbers:
    complement = target_number - num
    if complement in seen_numbers:
        pair = (min(num, complement), max(num, complement))
        if pair not in printed_pairs:
            print(f"{pair[0]} and {pair[1]} sums to the target_number {target_number}")
            printed_pairs.add(pair)
    seen_numbers.add(num)


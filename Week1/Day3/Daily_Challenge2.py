print("--- Caesar Cipher Program ---")

choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

if choice not in ['E', 'D']:
    print("Invalid choice! Please choose 'E' or 'D'.")
else:
    message = input("Enter your message: ")
    shift_input = input("Enter the shift number (e.g., 3): ")
    if not shift_input.strip().replace("-", "").isdigit():
        print("Please enter a valid integer for the shift.")
    else:
        shift = int(shift_input)
        if choice == 'D':
            shift = -shift
        result_text = ""
        for letter in message:
            if letter.isupper():
                new_char = chr((ord(letter) - 65 + shift) % 26 + 65)
                result_text += new_char
            elif letter.islower():
                new_char = chr((ord(letter) - 97 + shift) % 26 + 97)
                result_text += new_char
            else:
                result_text += letter
        action = "Encrypted" if choice == 'E' else "Decrypted"
        print(f"\n{action} message: {result_text}")
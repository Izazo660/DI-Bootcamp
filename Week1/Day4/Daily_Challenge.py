MATRIX_STR = '''
7ii
Tsx
h%?
i #
sM 
$a 
#t%''' 

# Step 1: Convert matrix_string to a 2D list (matrix)
matrix = []
lines = MATRIX_STR.splitlines()
for line in lines:
    if line:
        matrix.append(list(line))

num_rows = len(matrix)
num_columns = len(matrix[0])
alpha_chars_with_markers = [] 

# Step 2: Iterate through columns
for col in range(num_columns):
    for row in range(num_rows):
        char = matrix[row][col]
        # Step 3: Filter alpha characters
        if char.isalpha():
            alpha_chars_with_markers.append(char)
        else:
            alpha_chars_with_markers.append("SYMBOL_MARKER")

# Step 4: Replace symbols with spaces
decoded_message = ""
symbols_encountered = False

for item in alpha_chars_with_markers:
    if item != "SYMBOL_MARKER":
        if symbols_encountered and len(decoded_message) > 0:
            decoded_message += " "
        decoded_message += item
        symbols_encountered = False
    else:
        symbols_encountered = True

# Step 5: Print the decoded message
print(decoded_message)

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
    if line:  # Évite de prendre les lignes vides
        matrix.append(list(line))

num_columns = max(len(row) for row in matrix) if matrix else 0
num_rows = len(matrix)

for row in matrix:
    while len(row) < num_columns:
        row.append(" ")

# Step 2: Iterate through columns
decoded_message = ""
symbols_encountered = False

for col in range(num_columns):
    for row in range(num_rows):
        char = matrix[row][col]
        # Step 3: Filter alpha characters
        if char.isalpha():
            # Step 4: Replace symbols with spaces (Intégré directement pour simplifier)
            if symbols_encountered and len(decoded_message) > 0:
                decoded_message += " "
            decoded_message += char
            symbols_encountered = False
        else:
            symbols_encountered = True

# Step 4: Replace symbols with spaces
# Step 5: Print the decoded message
print(decoded_message)
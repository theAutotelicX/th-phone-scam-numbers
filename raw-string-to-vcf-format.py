import re

# List of input numbers
numbers = ["020795271"]

# Define regex pattern
pattern = r"(\d{3})(\d{3})(\d{3})"

# Loop through each number
for number in numbers:
    # Replace the pattern with the desired format
    formatted_number = re.sub(pattern, r"\1-\2-\3", number)
    print(f"TEL;HOME:{formatted_number}")

# Output:
# 020-795-271

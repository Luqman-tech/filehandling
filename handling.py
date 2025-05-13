# Read input.txt, process the text, and save results in output.txt

# Read the original text
with open("input.txt", "r") as file:
    content = file.read()

# Count the words
words = content.split()
word_count = len(words)

# Convert text to uppercase
upper_text = content.upper()

# Prepare the output text
output = upper_text + f"\n\nWord count: {word_count}"

# Write to output.txt
with open("output.txt", "w") as file:
    file.write(output)

print("✅ Done! The processed text has been saved to 'output.txt'.")

"""
# Store the sentence we want to work with
text = "A quick brown fox jumps over the lazy dog."

# Convert the text to lowercase, remove spaces, and remove the full stop
result = text.lower().replace(" ", "").replace(".", "")

# Create an empty list to store each letter only once
result_02 = []

# Go through each letter in the cleaned text
for i in result:

    # Check if the letter is not already in the list
    if i not in result_02:

        # Add the letter to the list
        result_02.append(i)

# Sort the letters in alphabetical order
result_02.sort()

# Ask the user which letter they want to check
inp = input("Type which letter you are looking for: ").lower()

# Print the score of the letter
print(f"Word score of {inp}: ", result_02.index(inp) + 1) """

def get_word_score(word):
  text = "A quick brown fox jumps over the lazy dog."
  result = text.lower().replace(" ","").replace(".","")
  result_02 = []
  for i in result:
    if i not in result_02:
      result_02.append(i)

  result_02.sort()
  return result_02.index(word) + 1

inp = input("type which letter you are looking for: ").lower()
print(f"word score of {inp}: ", get_word_score(inp))

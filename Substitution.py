pattern = r"\d+"
text = "There are 123 apples and 456 bananas."
new_text = re.sub(pattern, "X", text)
print(new_text)  # Output: There are X apples and X bananas.

pattern = r"\b\w+\b"
text = "Hello, world! How are you today?"
matches = re.findall(pattern, text)
print(matches)  # Output: ['Hello', 'world', 'How', 'are', 'you', 'today']

pattern = r"world"
text = "Hello, world!"
match = re.search(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("Pattern not found")

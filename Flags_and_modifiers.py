pattern = r"apple"
text = "An APPLE and an Apple."
match = re.search(pattern, text, re.IGNORECASE)
if match:
    print("Pattern found:", match.group())

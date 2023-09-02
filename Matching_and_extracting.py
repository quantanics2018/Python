pattern = r"(\d{2})-(\d{2})-(\d{4})"
text = "Date: 21-08-2023"
match = re.search(pattern, text)
if match:
    print("Full match:", match.group(0))
    print("Day:", match.group(1))
    print("Month:", match.group(2))
    print("Year:", match.group(3))

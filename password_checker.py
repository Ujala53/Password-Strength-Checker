password = input("Enter your password (e.g., Ujala@123): ")

length = len(password)

has_upper = False
has_number = False
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.isdigit():
        has_number = True
    elif not char.isalnum():
        has_symbol = True

score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_number:
    score += 1
if has_symbol:
    score += 1

print("\nChecking password...\n")

if score <= 1:
    print("Weak Password")
elif score == 2 or score == 3:
    print("Medium Password")
else:
    print("Strong Password")

print("\nSuggestions to improve your password:")
if length < 8:
    print("- Use at least 8 characters")
if not has_upper:
    print("- Add uppercase letters")
if not has_number:
    print("- Include numbers")
if not has_symbol:
    print("- Add special symbols like @, #, $")

# Example password using your name
example_password = "Ujala@123"
print("\nExample Password:", example_password)

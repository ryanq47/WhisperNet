import bcrypt

# String to be hashed
password = "1234"

# Convert the string to bytes (bcrypt expects bytes)
password_bytes = password.encode("utf-8")

# Generate a random salt and hash the password
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password_bytes, salt)

# Print the hashed password
print("Hashed Password:", hashed_password.decode("utf-8"))  # Decode to convert bytes to a string for printing

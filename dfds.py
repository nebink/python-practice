def encrypt(msg, n):
    encrypted_msg = ""
    for char in msg:
        if char.isalpha():
            ascii_val = ord(char.upper()) - 65
            encrypted_val = (ascii_val + n) % 26
            encrypted_char = chr(encrypted_val + 65)
            if char.islower():
                encrypted_char = encrypted_char.lower()
            encrypted_msg += encrypted_char
        else:
            encrypted_msg += char
    return encrypted_msg

msg = "ATTACKATONCE"
n = 5
encrypted_msg = encrypt(msg, n)

print("Original message:", msg)
print("Encrypted message:", encrypted_msg)

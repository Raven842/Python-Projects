key = int(input("State the number of places to be shifted: "))
plain = input("Plaintext: ")
l = len(plain)
cipher = [0] * l
for i in range(0, l):
    cipher[i] = chr(ord(plain[i].lower()) + key)
    if ord(cipher[i]) > 122:
        cipher[i] = chr(ord(cipher[i]) - 26)
cipher = "".join(cipher)
print("Ciphertext: ", cipher)
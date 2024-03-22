import sys
key = input("Key: ")
if len(key) != 26:
    print("The key must be 26 charcters in length")
    sys.exit(1)
plain = input("Plaintext: ")
plain_dict = [97, 98, 99, 100, 101, 102, 103, 104 ,105, 106, 107, 108, 109, 110, 111 ,112, 113, 114 ,115, 116 ,117, 118, 119, 120, 121, 122]
cipher = [0] * len(plain)
for i in range(0, len(plain)):
    for j in range(0, 25):
        if ord(plain[i].lower()) == plain_dict[j]:
            if plain[i].isupper():
                cipher[i] = key[j].upper()
            else:
                cipher[i] = key[j].lower()
cipher = "".join(cipher)
print("Ciphertext: ", cipher)
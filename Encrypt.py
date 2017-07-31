def encrypt(message, key):
    cipherText = []

    if len(key) < len(message):  # make sure key length is sufficient
        print("Insufficient key length")

    for el in range(len(message)):  # for each element
        cipherText.append(str((int(key[el]) + int(message[el])) % 2))  # xor with key

    return "".join(cipherText)  # return the cipher text

# print(encrypt("11001", "11111"))
# input("Any Key to close")

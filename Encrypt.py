def encrypt(message, key):
	cipherText = []

	if len(key) != len(message):
		print("Insufficient key length")

	for el in range(len(message)):
		cipherText.append(str((int(key[el]) + int(message[el]))%2))

	return "".join(cipherText)

#print(encrypt("11001", "11111"))
#input("Any Key to close")

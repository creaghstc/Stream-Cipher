from Encrypt import encrypt

def Decrypt(CipherText, key):
	message = encrypt(CipherText, key)
	return(message)

print(Decrypt("00110", "11111"))
input("press")
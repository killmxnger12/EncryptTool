#!/usr/bin/python
import random


def GenKey():
	return random.randint(5, 20) # Modular part #1


def GenKeyValue(key):
	return int((pow(key, 8) + pow(key, 3))/(key * 3)) # Modular part #2


def Encrypt(data):
	encrypted_values = ""
	key = GenKey()

	encrypted_values += str(key) + ","
	for x in data:
		if x == " ":
			encrypted_values += " "
		else:
			char_value = ord(x) + GenKeyValue(key)
			encrypted_values += str(char_value)
			char_value = ""

	WriteToFile(encrypted_values, "encrypted.txt")


def Decrypt(encrypted):
	decrypted = ""
	counter = 0

	key = encrypted.split(',')[0]
	encrypted_value = encrypted.split(',')[1]

	key_value_len = GetKeyValueLength(key)
	char = ""
	for x in encrypted_value:
		if counter == key_value_len:
			character = chr(int(char) - GenKeyValue(int(key)))
			decrypted += character
			char = ""
			counter = 0
			if x == " ":
				decrypted += " "
			else:
				char += str(x)
				counter += 1
		else:
			char += str(x)
			counter += 1

	character = chr(int(char) - GenKeyValue(int(key)))
	decrypted += character
	char = ""
	counter = 0

	WriteToFile(decrypted, "output.txt")


def GetKeyValueLength(key):
	if 5 <= int(key) <= 6:
		return int(5)
	if 7 <= int(key) <= 8:
		return int(6)
	if 9 <= int(key) <= 11:
		return int(7)
	if 12 <= int(key) <= 16:
		return int(8)
	if 17 <= int(key) <= 20:
		return int(9)


def WriteToFile(values, filename):
	with open(filename, "w") as file:
		file.truncate()
		file.write(values)
		file.close()

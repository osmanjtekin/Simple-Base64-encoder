alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","`","@","#","$","%","^","&","*","(",")","_","-","+","[","]","{","}",";",":","|",",","<",">",".","/","?"]
padding = {0:"",8:"0000", 16:"00"}
padding_equals = {0:"",8:"==", 16:"="}

#Encode a text with base64
def base64Encode(data_to_encode):
	binary_string=base64string= ""

	for character in data_to_encode: # Loop through characters in the given data
		binary_character = bin( ord(character) ) # Convert character to its binary representation
		binary_character_length = len( binary_character ) # Store binary character length
		binary_string += "0"*(10-binary_character_length)+binary_character[2:] # Remove the first two numbers (0b) from the binary character, then add zeroes to the left (pad) to make it 8 byte long
	
	data_length = len(binary_string) % 24 # Calculate data length dividing remainder
	binary_string += padding[ data_length ] # Use the data remainder to add a zero padding so to make it evenly sized

	for binary_items in xrange(0, len(binary_string), 6): # for binary items in the 6x divided binary string
		base64string += alphabet[int( binary_string[binary_items:binary_items+6], 2 )] # Convert to base64 equivalent char from "alphabet"
	
	return base64string+padding_equals[data_length] # Return the base64 converted string, and if there's padding add it at the end (=)

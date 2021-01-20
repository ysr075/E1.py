
LED_off = "\nLED off"
LED_on = "\nLED on"

while True:
	choise = float(input("\n1.on / 0.off: "))
	if choise == 1:
		print(LED_on)
	elif choise == 0:
		print(LED_off)
	else:
		exit()

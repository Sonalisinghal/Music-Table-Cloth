import pygame
import serial
pygame.init()
pygame.mixer.init()
arduinoData=serial.Serial("/dev/cu.usbmodem14101",9600)
while True:
	myData=arduinoData.readline().strip()
	t = myData.decode('utf-8')
	print(t)
	if t=="1":
		print("yo")
		file = 'Kick01 Drums1DOTcom.mp3'
		# pygame.mixer.music.load(file)
		# pygame.mixer.music.play()
		# pygame.time.delay(100)

	elif t=="2":
		file = 'Kick52 Drums1DOTcom.mp3'
		# pygame.mixer.music.load(file)
		# pygame.mixer.music.play()
		# pygame.time.delay(100)
	else:	
		file = 'Kick52 Drums1DOTcom.mp3'
		# pygame.mixer.music.load(file)
		pygame.mixer.music.set_volume(0)
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	pygame.time.delay(100)

# file3 = 'Kick35 Drums1DOTcom.mp3'
# file4 = 'Kick43 Drums1DOTcom.mp3'
# pygame.mixer.music.load(file2)
# pygame.mixer.music.play()
# pygame.time.delay(1000)
# pygame.mixer.music.load(file3)
# pygame.mixer.music.play()
# pygame.time.delay(1000)
# pygame.mixer.music.load(file4)
# pygame.mixer.music.play()
# pygame.time.delay(1000)
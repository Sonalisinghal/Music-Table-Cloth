import pygame
import serial
pygame.init()
pygame.mixer.init()
mode=0
arduinoData=serial.Serial("/dev/cu.usbmodem144301",9600)
def modechange():
	mode=(mode+1)%4

while True:
	myData=arduinoData.readline().strip()
	t = myData.decode('utf-8')
	print(type(t))
	if t=="change":
		modechange()
	if mode==0:
		if t=="1":
			print("yo")
			file = 'Drum 1.mp3'
			pygame.mixer.music.set_volume(1)
		elif t=="2":
			file = 'Drum 2.mp3'
			pygame.mixer.music.set_volume(1)
		elif t=="3":
			file = 'Drum 3.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="4":
	        file = 'Drum 4.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="5":
	        file = 'Drum 5.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="6":
	        file = 'Drum 6.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="0":
	        file = 'Drum 6.mp3'
			pygame.mixer.music.set_volume(0)
	elif mode==1:
		if t=="1":
			print("yo")
			file = 'Guitar 1.mp3'
			pygame.mixer.music.set_volume(1)
		elif t=="2":
			file = 'Guitar 2.mp3'
			pygame.mixer.music.set_volume(1)
		elif t=="3":
			file = 'Guitar 3.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="4":
	        file = 'Guitar 4.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="5":
	        file = 'Guitar 5.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="6":
	        file = 'Guitar 6.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="0":
	        file = 'Guitar 6.mp3'
			pygame.mixer.music.set_volume(0)
	elif mode==2:
		if t=="1":
			print("yo")
			file = 'Piano 1.mp3'
			pygame.mixer.music.set_volume(1)
		elif t=="2":
			file = 'Piano 2.mp3'
			pygame.mixer.music.set_volume(1)
		elif t=="3":
			file = 'Piano 3.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="4":
	        file = 'Piano 4.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="5":
	        file = 'Piano 5.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="6":
	        file = 'Piano 6.mp3'
	        pygame.mixer.music.set_volume(1)
	    elif t=="0":
	        file = 'Piano 6.mp3'
			pygame.mixer.music.set_volume(0)
	# elif mode==3:
	# 	if t=="1":
	# 		print("yo")
	# 		file = 'Kick01 Drums1DOTcom.mp3'
	# 		pygame.mixer.music.set_volume(1)
	# 	elif t=="2":
	# 		file = 'Kick52 Drums1DOTcom.mp3'
	# 		pygame.mixer.music.set_volume(1)
	# 	elif t=="3":
	# 		file = 'Kick43 Drums1DOTcom.mp3'
	#         pygame.mixer.music.set_volume(1)
	#     elif t=="4":
	#         file = 'Kick07 Drums1DOTcom.mp3'
	#         pygame.mixer.music.set_volume(1)
	#     elif t=="5":
	#         file = 'Kick35 Drums1DOTcom.mp3'
	#         pygame.mixer.music.set_volume(1)
	#     elif t=="6":
	#         file = 'Kick52 Drums1DOTcom.mp3'
	#         pygame.mixer.music.set_volume(1)
	#     else:
	#         file = 'Kick52 Drums1DOTcom.mp3'
	# 		pygame.mixer.music.set_volume(0)

	print("running now")
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()
	pygame.time.delay(100)

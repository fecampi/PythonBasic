import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def falar(audio):
	tts = gTTS("%s"%audio,lang='pt-br')
	tts.save("conversa.mp3")
	playsound("conversa.mp3")

def ouvir():
	microfone = sr.Recognizer()

	with sr.Microphone() as source:

		microfone.adjust_for_ambient_noise(source)
		print("Ouvindo..")
		audio = microfone.listen(source)

	try:
		frase = microfone.recognize_google(audio,language='pt-BR')
		print("Você disse: " + frase)

	except sr.UnkownValueError:
		print("Não entendi")

	return frase

def gravar():
	microfone = sr.Recognizer()

	with sr.Microphone() as source:
		microfone.adjust_for_ambient_noise(source)
		print("Ouvindo..")
		audio = microfone.listen(source)

		with open("VozUsuario/fala2.wav","wb") as f:
			print("Gravando..")
			f.write(audio.get_wav_data())

def VozEmTexto(audio):
	r = sr.Recognizer()
	
	with sr.AudioFile(audio) as source:
		audio = r.record(source)
		print ("Analizando")
	try:
		text = r.recognize_google(audio,language='pt-BR')
		print("Sussesso")

	except sr.UnkownValueError:
		print("Não entendi")

	return text

falar('OI Felipe,tudo bem com voce?')



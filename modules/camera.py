# -*- coding: utf-8 -*-
from picamera import PiCamera
from time import sleep

#instancia objeto Picamera
camera = PiCamera()

#visualização por cinco segundos 
camera.start_preview()
sleep(5)
camera.stop_preview()

#visualização transparente 0 e 255.
camera.start_preview(alpha=200)
sleep(5)
camera.stop_preview()

#girar a imagem 0,90, 180 ou 270graus.
camera.rotation = 180

#tira foto(importante o tempo de 2 segundos antes para o sensor da câmera para detectar os níveis de luz)
camera.start_preview()
sleep(2)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

#loop para tirar n fotos seguidas:
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()

#gravando vídeo por n segundos
camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()

#resolução maxima Foto 2592 × 1944 e videos 1920 × 1080, minima 64 × 64.
camera.resolution = (2592, 1944)

#adicionar texto a imagem.
camera.annotate_text = "Hello world!"

#tamanho do texto 6 a 160 padrão é 32.
camera.annotate_text_size = 50

#alterar a cor do texto.
from picamera import PiCamera, Color
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')

#alterar o brilho da visualização de 0 a 100 padrão é 50.
camera.brightness = 70

#contraste da visualização de 0 a 100
camera.contrast = 0

#efeito de imagem, padrão é none.
camera.image_effect = 'colorswap'

"""
none - Nenhum
negative - negativo
solarize - solarizar
sketch - esboço
denoise - ruído
emboss - relevo
oilpaint - pintura a óleo
hatch- chocar
gpen - caneta
pastel - pastel
watercolor - aquarela
film - filme
blur - borrão
saturation - saturação
colorswap - troca de cores
washedout - lavado
posterise - posterizar
colorpoint - balanço de cores
colorbalance - balanço de cores 
cartoon - desenho animado
deinterlace1 - desentrelaçar 1
deinterlace2 - desentrelaçar 2
"""
#todos os efeitos de imagem 
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.capture("/home/pi/Documents/%s.jpg"%effect)
    sleep(5)
camera.stop_preview()


#exposição de imagem, modo padrão é auto.
camera.exposure_mode = 'beach'

"""
off - desligado
auto - auto
night - noite
nightpreview - visualização da noite
backlight - luz de fundo
spotlight - holofote
sports - esportes
snow - neve
beach - praia
verylong - muito longo
fixedfps - fps fixos
antishake - foto sem tremer
fireworks - fogos de artificio 
"""


#todos as exposições de imagem 
camera.start_preview()
for expo in camera.EXPOSURE_MODES:
    camera.capture("/home/pi/Documents/%s.jpg"%expo)
    sleep(5)
camera.stop_preview()

#equilíbrio de branco, modo padrão e auto
camera.awb_mode = 'sunlight'

"""
off - desligado
auto - auto
sunlight - luz do sol
cloudy - nublado
shade - sombra
tungsten - tungstênio
fluorescent - fluorescente
incandescent- incandescente
flash - flash
horizon - horizonte

"""
#todos os equilíbrios de branco
camera.start_preview()
for branco in camera.AWB_MODES:
    camera.capture("/home/pi/Documents/%s.jpg"%branco)
    sleep(5)
camera.stop_preview()















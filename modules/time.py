# -*- coding: utf-8 -*-
import time


#obter tempo em segundos
tempo1 = time.time()

#converte segundos em dia de semana, mes, dia, hora e ano. 
tempo2 = time.ctime(tempo1)

#converte segundos em tupla
tempo3 = time.gmtime(tempo1)

#tupla de hora agora
tempo4 = time.localtime()

#ano
tempo5 = tempo4.tm_year 

#mês
tempo5 = tempo4.tm_mon

#dia
tempo6 = tempo4.tm_mday

#hora
tempo7 = tempo4.tm_hour

#minuto
tempo8 = tempo4.tm_min

#segundo
tempo9 = tempo4.tm_sec

#dia da semana
tempo10 = tempo4.tm_wday

#dia do ano
tempo11 = tempo4.tm_yday

#horario de versão
tempo12 = tempo4.tm_isdst


"""     Mais formatação


%a		Dia da semana como nome abreviado do idioma.
%A		Dia da semana como nome completo do local
%b		Mês como nome abreviado do código do idioma.
%B		Mês como nome completo do local.
%c		Representação de data e hora apropriada da localidade.
%d		Dia do mês como um número decimal com zero.
%f		Microssegundo 
%H		Hora (relógio de 24 horas) 
%I		Hora (relógio de 12 horas) 
%j		Dia do ano
%m		Mês (1-12)
%M		Minutos(00-59)
%p		AM ou PM.
%S		Segundos
%U		Número da semana do ano (domingo como o primeiro dia da semana) 
%w		Dia da semana como um número decimal, onde 0 é domingo e 6 é sábado
%W	    Número da semana do ano (segunda-feira como o primeiro dia da semana) 
%x		Representação de data apropriada da localidade.
%X		Representação de tempo apropriada do local.
%y		Ano(00-99)
%Y		Ano 4 dígitos
%Z		Nome do fuso horário
"""
tempo13 = time.strftime("%x")


print(tempo13)
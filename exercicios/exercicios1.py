import math


#Primeiro Exercício: Se você fizer uma corrida de 10 quilômetros em 43 minutos e 30 segundos, qual #será seu tempo médio por milha? Qual é a sua velocidade média em milhas por hora? (Dica: há 1,61 #quilômetros em uma milha). 

print('Exercício 1:')

m = 1.61
ds = 10/m
dt = 43.5/60

veloc_med = ds/dt
tempm = 1/veloc_med

print('O tempo medio por milha foi de:', tempm)
print('A velocidade media em milhas por hora foi:', veloc_med)


#Segundo Exercício: Desde sua varanda você escuta o som do primeiro fogo artificial do reveillon 3 segundos depois de ver a luz, qual a distância? (o som tem velocidade 343 m/s e a luz %$3\times 10^8$% m/s). 

print('Exercício 2:')

vel_som = 343
vel_luz = 10^8
dt=3

ds = vel_som*dt

print('a distancia eh de:', ds)

#Terceiro Exercício:Ache os zeros da função: y = 3 *x^2 - 4 *x -10 

print('Exercício 3:')

a = 3
b = -4
c = -10

delta = ((b**2) - (4*a*c))
print('valor de delta:',delta)
num_um = -b+math.sqrt(delta)
print(num_um)
num_dois = -b-math.sqrt(delta)
x_um = num_um/(2*a)
x_dois = num_dois/(2*a)

print('a primeira raiz eh:', x_um)
print('a segunda raiz eh:', x_dois)

#Quarto Exercício: Se, ao meiodia, a sombra de um poste de 5 m de altura tem apenas 50 cm de comprimento no chão, qual o ângulo zenital do sol?

print('Exercício 4:')

#math.radians(0.1)
#math.atan(math.radians(0.1))

alt = 5
sombra = 0.5
hipotenusa = sombra/alt

angulo = math.degrees(math.atan(math.radians(hipotenusa)))

print(' O angulo zenital eh:', angulo) 


#Quinto Exercício: Calcule o seu %$IMC = \dfrac{M}{A^2}$% (com a massa em Kg e a altura em metros). Um valor saudável estara --em geral-- entre 20-25. Um bebê de 6 meses "gorducho" tem 70 cm de "comprimento" e 11 kg de massa, qual o IMC dele? 

print('Exercício 5:')

alt_sara = 1.63
peso_sara = 70

alt_bebe = 0.7
peso_bebe = 11

imc_sara = peso_sara/(alt_sara)**2

imc_bebe = peso_bebe/(alt_bebe)**2

print('O imc da Sara eh de:', imc_sara)
print('O imc do bebe eh de:', imc_bebe)

#Sexto Exercício: Calcule a velocidade final de um objeto em queda livre a partir de 3 metros de altura (sem resistencia do ar). Calcule o tempo que esse objeto demora para cair.

print('Exercício 6:')

sini = 0
sfim = 3
g = 9.81

t = math.sqrt((2*(sfim-sini)/g))

print('O tempo que o objeto demora pra cair eh de:',t)














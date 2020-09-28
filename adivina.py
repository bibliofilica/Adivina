import random

intentos = 0
numero = random.randint (1,20)
print ('Estoy pensando un numero entre 1 y 20.')

while intentos < 6:
    print ('Intenta adivinar el número que pense')
    estimacion = int(input ())
    
    intentos=intentos+1
    if estimacion < numero:
        print('tu estimacion es muy baja, intentalo otra vez')
    if estimacion > numero:
        print ('tu estimacion es muy alta, intentalo otra vez')
   
        
         break

if estimacion == numero:
    intentos = str(intentos)
    print('Buen trabajo lo has adivinado en ' + intentos + 'intentos')
   

if estimacion!=numero:
    numero= str(numero)
    print ('pues no adivinaste, el numero era ' + numero + )

      
     

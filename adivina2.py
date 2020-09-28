import random
import math 

intentos = 0
print ('Dime un numero alto')
top = (input())
max=int(top)
numero = random.randint (1,max)
iteraciones = int(math.log2(max))+1
chances=str(iteraciones)
print ('Estoy pensando un numero entre 1 y ' + top +' tienes ' + chances + ' intentos' )




while intentos < iteraciones:
    print ('Intenta adivinar')
    estimacion = (input ())
    estimacion = int (estimacion)
    intentos=intentos+1
    
    if estimacion < numero:
        print('tu estimacion es muy baja, prueba otra vez')
        
    if estimacion > numero:
        print ('tu estimacion es muy alta, prueba otra vez')
        
    if estimacion == numero:
         break


if estimacion == numero:
    intentos = str(intentos)
    print('Buen trabajo, lo has adivinado en ' + intentos + ' intentos')
   

if estimacion!=numero:
    numero= str(numero)
    print ('pues no, el numero era ' + numero)
      
     

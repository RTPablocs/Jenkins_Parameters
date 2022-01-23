from os import getenv
s_one = getenv('STAGE_ONE')
s_two = getenv('STAGE_TWO')

if s_one == True and s_two == True:
    print("El proyecto va viento en popa!!!")
elif s_one == False and s_two == False:
    print( "Esto pinta muy mal")
else:
    print("Alguna de las dos stages ha fallado")
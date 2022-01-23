from os import getenv
s_one = getenv('STAGE_ONE')
s_two = getenv('STAGE_TWO')

if s_one == true and s_two == true:
    print("El proyecto va viento en popa!!!")
elif s_one == false and s_two == false:
    print( "Esto pinta muy mal")
else:
    print("Alguna de las dos stages ha fallado")
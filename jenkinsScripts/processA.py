from sys import argv
from os import system


if int(argv[1])%2 == 0:
    system('export STAGE_ONE=true')
else:
    system('export STAGE_ONE=true')
import os

def output_wrapper():
    os.system('cls')
    return 'mouseless queue v1.0\nwe accept, you play\n'

def output_message(message):
    print(output_wrapper())
    print(message)

#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

def showIP(interface):
    print('IP: ', end='')
    print(netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr'])

def showMAC(interface):
    print('MAC: ', end='')
    print(netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr'])

for i in netifaces.interfaces():
    print('\n************** Details of Interface - ' + i + ' *********************')
    try: # This is a new line, you also need to indent the code below this line by 4 whitespaces
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK])
        print(netifaces.ifaddresses(i)[netifaces.AF_INET])
        print('MAC: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
        print('\n\n')
        showIP(i)
        showMAC(i)
    except:
        print('Could not collect adapter information') # Print an error message





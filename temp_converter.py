#!/usr/bin/env python 
# A simple app to convert fahrenheit to Celsius

def temp_converter():
    print("Welcome to a simple tempature converter. \n")
    get_preference()
    
    conv_another()

def print_redo():
    print("Please choose either a or b. \n")    

def get_preference():
    res = input("Are converting to Fahrenheit or to Celsius? \n[a] Fahrenheit \n[b] Celsius \n> ")
    
    if res == 'a':
        return fahren_conv()
    elif res == 'b':
        return cels_conv()
    else:
        print_redo()
        get_preference()    
        
def fahren_conv():
    fahrenheit = int(input('Enter a tempature in Fahrenheit: '))
    celsius = (fahrenheit - 32) * 5/9
    print(celsius,"°C \n") 
    
def cels_conv():
    celsius = int(input('Enter a tempature in Celsius: '))
    fahrenheit = 9/5 * celsius + 32
    print(fahrenheit,"°F \n")
    

def conv_another():
    res = input("Do you need another conversion? \n[a] Yes \n[b] No \n>")
    
    if res == 'a':
        return get_preference()
    elif res == 'b':
        print('Goodbye')
    else:
        print_redo()
        conv_another()
    


# call the converter

temp_converter()
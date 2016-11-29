#!/usr/bin/env python3
'''
Main class for the program. 

User prompts option of diseases (Measles, Hepatitis_A, Rubella, Poliomyelitis, Smallpox and Mumps) to see
the trend of decreasing number of infective people over time and its relation to the invention of 
vaccines.

Heatmap will plot the number of infected people, measured over 70-somes years and across all states. 

Generally the plot will show a distinctive declined density after vaccines were introduced.

User could enter "quit" to stop the program or by keyboard interrupt.
'''
from plot_heatmap import heatmap_Measles,heatmap_Hepatitis_A,heatmap_Mumps,\
                         heatmap_Poliomyelitis, heatmap_Smallpox,heatmap_Rubella
import sys

def main():
    while True:
        try:
            data = input('Plz enter the name of disease: ').lower()
            data = data.replace(" ", "") #eliminating any space by mistakenly input
            valid_list =['measles','hepatitis_a','rubella','poliomyelitis','smallpox','mumps']
            
            if data == 'quit':
                sys.exit(0)
            if data.isdigit():
                print('Only strings are allowed')
                raise ValueError
            if data not in valid_list:
                print('This is not a existing disease in our dataset, plz re-entry a name. ')
                raise ValueError
            
            if data == 'measles':
                heatmap_Measles()
            if data == 'hepatitis_a':
                heatmap_Hepatitis_A()
            if data == 'rubella':
                heatmap_Rubella()
            if data == 'poliomyelitis':
                heatmap_Poliomyelitis()
            if data == 'smallpox':
                heatmap_Smallpox()
            if data == 'mumps':
                heatmap_Mumps()
            
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except ValueError:
            print('Invalid input!')
      
            

if __name__ == '__main__':
    print('-Enter the disease name to see the heatmap of disease and vaccines')
    print('-Availible diseases are Measles, Hepatitis_A, Rubella, Poliomyelitis, Smallpox and Mumps')
    print('-You can type Quit to interrupt program')
    
    main()
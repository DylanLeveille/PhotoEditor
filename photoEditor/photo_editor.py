# SYSC 1005 A Fall 2017 Lab 7

import sys  # get_image calls exit
from Cimpl import *
from filters import *

def get_image():
    """
    Interactively select an image file and return a Cimpl Image object
    containing the image loaded from the file.
    """

    # Pop up a dialogue box to select a file
    file = choose_file()

    # Exit the program if the Cancel button is clicked.
    if file == "":
        sys.exit("File Open cancelled, exiting program")

    # Open the file containing the image and load it
    img = load_image(file)

    return img

# A bit of code to demonstrate how to use get_image().

if __name__ == "__main__":
    #Set done (for the while loop) to False,
    #and loaded (for a loaded image) to False.
    done = False
    loaded = False
    
    while done != True:
        #Print the user's options
        print("L)oad \nN)egative G)rayscale X)treme contrast S)epia tint", 
        "E)dge detect \nQ)uit")
        
        #assign the variable command to th user's input
        command = input(': ')
        
        #Set loaded to True if L is entered
        if command == 'L':
            img = get_image()
            show(img)
            loaded = True
        
        #Check for the Q command to have the user quit the program
        elif command == 'Q': 
            done = True    
            
        #Printing 'No such command rather than returning an error if an
        #invalid command is inputted
        elif command not in ['N','G', 'X', 'S', 'E']:
            print('No such command') 
           
        #Checking to see if the image is loaded 
        elif loaded == True:
            #If it is loaded, then based on the user's command, the image will 
            #be modified
            if command == 'N': 
                negative(img)
                show(img)
                
            elif command == 'G': 
                grayscale(img)
                show(img)    
                
            elif command == 'X': 
                extreme_contrast(img)
                show(img)   
                
            elif command == 'S': 
                sepia_tint(img)
                show(img)  
                
            elif command == 'E': 
                threshold = float(input('Threshold?: '))
                detect_edges_better(img, threshold)
                show(img)                                 
            
        #Printing 'No image loaded' if command is valid but no image is loaded
        #At this point in the code, we can assure that the input is valid
        #but that no image is loaded.
        else:
            print('No image loaded')
""" SYSC 1005 A Fall 2017.

Filters for a photo-editing application.
"""

from Cimpl import *
from random import randint

def red_channel(image):
    """ (Cimpl.Image) -> (none)
    
    Replace all the green and blue components
    to 0 for every pixel in an image,
    leaving the red components unchanged.
    
    img = load_image(choose_file())
    red_channel(img)
    show(img)
    """
    #we first need to visit every pixel in the Cimpl.Image
    for x, y, (r, g, b) in image:
        #creating a Cimpl.Color object containing
        #the original red component of the pixel
        #and the green and blue components to zero
        red = create_color(r, 0, 0)
        #now we set the new components for every
        #pixel in the image
        set_color(image, x, y, red)
        
def green_channel(image):
    """ (Cimpl.Image) -> (none)
    
    Replace all the red and blue components
    to 0 for every pixel in an image,
    leaving the green components unchanged.
    
    img = load_image(choose_file())
    green_channel(img)
    show(img)
    """
    #we first need to visit every pixel in the Cimpl.Image
    for x, y, (r, g, b) in image:
        #creating a Cimpl.Color object containing
        #the original green component of the pixel
        #and the red and blue components to zero
        green = create_color(0, g, 0)
        #now we set the new components for every
        #pixel in the image
        set_color(image, x, y, green)

def blue_channel(image):
    """ (Cimpl.Image) -> (none)
    
    Replace all the red and green components
    to 0 for every pixel in an image,
    leaving the blue components unchanged.
    
    img = load_image(choose_file())
    red_channel(img)
    show(img)
    """
    #we first need to visit every pixel in the Cimpl.Image
    for x, y, (r, g, b) in image:
        #creating a Cimpl.Color object containing
        #the original blue component of the pixel
        #and the red and green components to zero
        blue = create_color(0, 0, b)
        #now we set the new components for every
        #pixel in the image
        set_color(image, x, y, blue)
	
def reduce_brightness_half(image):
    """ (Cimpl.Image) -> (none)
	
    Reduce each RGB component's brightness 
    by 50% of its original value
    for every pixel in an image.

    >>> img = load_image(choose_image())
    >>> reduce_brigthness(img)
    >>> show(img)

    """
    #we must first visit every pixel 
    #in the image
    for x, y, (r, g, b) in image:
        #here we are creating the Color object
        #containing the RGB components 
        #reduced to 50%
        half = create_color(r * 0.5, g * 0.5, b * 0.5)
        #now we set the new color to
        #the corresponding pixel
        set_color(image, x, y, half)

def reduce_brightness_75(image):
    """ (Cimpl.Image) -> (none)
	
    Reduce each RGB component's brightness 
    by 75% of its original value
    for every pixel in an image.

    >>> img = load_image(choose_image())
    >>> reduce_brigthness_75(img)
    >>> show(img)

    """
    #we must first visit every pixel 
    #in the image  
    for x, y, (r, g ,b) in image:
        #here we are creating the Color object
        #containing the RGB components 
        #reduced to 75%
        new_brightness = create_color(r * 0.75, g * 0.75, b * 0.75)
        #now we set the new color to
        #the corresponding pixel
        set_color(image, x, y, new_brightness)

def reduce_brightness_25(image):
    """ (Cimpl.Image) -> (none)
	
    Reduce each RGB component's brightness 
    by 25% of its original value
    for every pixel in an image.

    >>> img = load_image(choose_image())
    >>> reduce_brigthness_25(img)
    >>> show(img)

    """
    #we must first visit every pixel 
    #in the image  
    for x, y, (r, g ,b) in image:
        #here we are creating the Color object
        #containing the RGB components 
        #reduced to 25%
        new_brightness = create_color(r * 0.25, g * 0.25, b * 0.25)
        #now we set the new color to
        #the corresponding pixel
        set_color(image, x, y, new_brightness)
        
def reduce_brightness(image, multiplier):
    """ (Cimpl.Image, float) -> (none)
	
    Reduce each RGB component's brightness 
    by a multiple of its original value
    for every pixel in an image.
    
    multiplier is a floatvalue in the
    range of 0.0 to 1.0 which will multiply
    each pixel's component in a Cimpl.Image

    >>> img = load_image(choose_image())
    >>> reduce_brigthness(img, 0.33)
    >>> show(img)

    """
    #we must first visit every pixel 
    #in the image  
    for x, y, (r, g ,b) in image:
        #here we are creating the Color object
        #containing the RGB components 
        #reduced by the multiplier
        new_brightness = create_color(r * multiplier, g * multiplier, 
                                      b * multiplier)
        #now we set the new color to
        #the corresponding pixel
        set_color(image, x, y, new_brightness)
        
def swap_red_blue(image):
    """ (Cimpl.Image) -> (none)
	
    Swap each red and blue component
    for every pixel in an Cimpl.Image
    
    multiplier is a floatvalue in the
    range of 0.0 to 1.0 which will multiply
    each pixel's component in a Cimpl.Image

    >>> img = load_image(choose_image())
    >>> swap_red_blue(img)
    >>> show(img)

    """
    #we must first visit every pixel 
    #in the image  
    for x, y, (r, g ,b) in image:
        #here we are creating the Color object
        #containing which swaps the red
        #and blue components
        swap = create_color(b, g, r)
        #now we set the new color to
        #the corresponding pixel
        set_color(image, x, y, swap)
        
def hide_image(image):
    """ (Cimpl.Image) -> (none)
	
    Hide an original image by distorting 
    the red, green, and blue compoenents
    for each pixel.

    >>> img = load_image(choose_image())
    >>> hide_image(img)
    >>> show(img)

    """
    #we must first visit every pixel 
    #in the image  
    for x, y, (r, g ,b) in image:
        #first of all, we need to calculate the
        #average value for the RGB components of the pixel
        #and assign the value to the new red component
        hidden_r = ((r + g + b) // 3) / 10
        #now we need to distort the color of the green 
        #and red components by replacing their comonents with
        #random integer values
        hidden_g = randint(0, 255)
        hidden_b = randint(0, 255)
        #here we create the hidden color object
        hidden = create_color(hidden_r, hidden_g, hidden_b)
        #now we set the new color to
        #the corresponding pixel
        set_color(image, x, y, hidden)  
        
def recover_image(image):
    """ (Cimpl.Image) -> (none)
	
    Recover the original image from the hidden (distorted)
    image caused by the hide_image function

    >>> img = load_image(choose_image())
    >>> recover_image(img)
    >>> show(img)

    """
    #we must first visit every pixel 
    #in the image  
    for x, y, (r, g ,b) in image: 
        #now we need to reverse the green and blue components
        original_g = (((30 * r) - b) - r)
        original_b = (((30 * r) - original_g) - r)
        #next, we need to reverse the red component
        original_r = (((r * 10) * 3) - original_g - original_b)  
        #here we recreate the original image Color Object
        original = create_color(original_r, original_g, original_b)
        #now we set the new color to
        #the corresponding pixel
        set_color(image, x, y, original)  

def grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)    
    """
    for  x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = (r + g + b) // 3
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)

def weighted_grayscale(image):
    """ (Cimpl.Image) -> None
    
    Convert image into shades of gray.
    
    >>> image = load_image(choose_file()) 
    >>> grayscale(image)
    >>> show(image)    
    """
    for  x, y, (r, g, b) in image:

        # Use the shade of gray that has the same brightness as the pixel's
        # original color.
        
        brightness = r * 0.299 + g * 0.587 + b * 0.114
        gray = create_color(brightness, brightness, brightness)
        set_color(image, x, y, gray)

def negative(image):
    """ (Cimpl.Image) -> None
    
    Convert each pixel's red, green, and blue 
    components to their opposite values in Image.
    
    >>> img = load_image(choose_file())
    >>> negative(img)
    >>> show(img)
    """
    for x, y, (r, g, b) in image:
        r = 255 - r
        g = 255 - g
        b = 255 - b
        opposite = create_color(r, g, b)
        set_color(image, x, y, opposite)

def solarize(image, threshold):
    """ (Cimpl.Image, int) -> None
    
    Solarize image, modifying the RGB compoennts that
    have intensities that are less than threshold.
    
    threshold is an int type value that is in the range
    0 <= threshold <= 255. 
    
    >>> image = load_image(choose_file()) 
    >>> solarize(image, 128)
    >>> show(image)     
    """
    for x, y, (red, green, blue) in image:

        # Invert the values of all RGB components that are less than the
        #threshold value, leaving components with higher values unchanged.

        if red < threshold:
            red = threshold - red

        if green < threshold:
            green = threshold - green

        if blue < threshold:
            blue = threshold - blue
            
        #Crete the Color object and set the new colour.
        solarized = create_color(red, green, blue)
        set_color(image, x, y, solarized)


def black_and_white(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white (two-tone) image.
    
    >>> image = load_image(choose_file()) 
    >>> black_and_white(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    # Brightness levels range from 0 to 255.
    # Change the colour of each pixel to black or white, depending on 
    # whether its brightness is in the lower or upper half of this range.       

    for x, y, (red, green, blue) in image:
        brightness = (red + green + blue) // 3      
        
        if brightness < 128:
            set_color(image, x, y, black)
        else:     # brightness is between 128 and 255, inclusive
            set_color(image, x, y, white)


def black_and_white_and_gray(image):
    """ (Cimpl.Image) -> None
    
    Convert image to a black-and-white-and-gray (three-tone) image.

    >>> image = load_image(choose_file()) 
    >>> black_and_white_and_gray(image)
    >>> show(image)     
    """
    black = create_color(0, 0, 0)
    gray = create_color(128, 128, 128)
    white = create_color(255, 255, 255)

    # Brightness levels range from 0 to 255. Change the colours of
    # pixels whose brightness is in the lower third of this range to black,
    # in the upper third to white, and in the middle third to medium-gray.

    for x, y, (red, green, blue) in image:      
        brightness = (red + green + blue) // 3

        if brightness < 85:
            set_color(image, x, y, black)
        elif brightness < 171: # brightness is between 85 and 170, inclusive
            set_color(image, x, y, gray)
        else:                  # brightness is between 171 and 255, inclusive
            set_color(image, x, y, white)

def extreme_contrast(image):
    """ (Cimpl.Image) -> None
    
    Modify Image, maximizing the contrast between the light
    and dark pixels.
    
    >>> image = load_image(choose_file())
    >>> extreme_contrast(image)
    >>> show(img)
    """
    #for each pixel, we check eahc RGB component and set the new component 
    #depending on its brightness.
    for x, y, (r, g, b) in image:
        if r < 128:
            r = 0
        else:
            r = 255
            
        if g < 128:
            g = 0
        else:
            g = 255
            
        if b < 128:
            b = 0
        else:
            b = 255
        contrast = create_color(r, g, b)
        set_color(image, x, y, contrast)
        
        #8 diffreent colours are possible,
        #since each compoenent is one of two
        #possibilities. Therefore, 2 ^ 3 == 8
        
def sepia_tint(image):
    """ (Cimpl.Image) -> (None)
    
    Convert image to sepia tones.
    
    >>> image = load_image(choose_file())
    >>> sepia_tint(image)
    >>> show(image)
    """
    #first thing to do is to turn the image to grayscale
    weighted_grayscale(image)
    
    #Next, we go through each pixel, to find their average colour. 
    #Depending on this average colour value, the colour will be modified.
    for x, y, (r, g, b) in image:
        
        average = (r + g + b) // 3
        
        if average < 63:
            r = r * 1.1
            b = b * 0.9
            
        elif average < 192:
            r = r * 1.15
            b = b * 0.85
        
        else:
            r = r * 1.08
            b = b * 0.93
        
        #Create the Color object and set the pixel's new colour.
        new_color = create_color(r, g, b) 
        set_color(image, x, y, new_color)
        
def _adjust_component(amount):
    """ (int) -> int
    
    Divide the range 0...255 into 4 equal-size quadrants, 
    and return the midpoint of the quadrant in which the
    specified amount lies.
    
    amount is a positive integer representing the value
    of an RGB component in an image's pixel, and is in the range
    0 <= amount <= 255.
    
    >>> _adjust_component(10)
    31
    >>> _adjust_component(85)
    95
    >>> _adjust_component(142)
    159
    >>> _adjust_component(230)
    223
    """
    #The statements which decide what the amount will be based on the argument.
    if amount <= 63:
        amount = 31
    elif amount <= 127:
        amount = 95 
    elif amount <= 191:
        amount = 159
    else:
        amount = 223
    return amount

def posterize(image):
    """ (Cimpl.Image) -> None
    
    "Posterize" the specified image.
    
    >>> img = load_image(choose_file())
    >>> posterize(img)
    >>> show(img)
    """
    #visit each pixel
    for x, y, (r, g, b) in image:
        #Apply the _adjust_component function to adjust each colour
        #component of the pixel
        r = _adjust_component(r)
        g = _adjust_component(g)
        b = _adjust_component(b)
        
        #Create the Color object and set the new colour.
        posterize_color = create_color(r, g, b)
        set_color(image, x, y, posterize_color)
        
def blur(source):
    """ (Cimpl.Image) -> Cimpl.Image
    
    Return a new image that is a blurred copy of source.
    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)    
    """

    # We modify a copy of the original image, because we don't want blurred
    # pixels to affect the blurring of subsequent pixels.
    
    target = copy(source)
    
    # Recall that the x coordinates of an image's pixels range from 0 to
    # get_width() - 1, inclusive, and the y coordinates range from 0 to
    # get_height() - 1.
    #
    # To blur the pixel at location (x, y), we use that pixel's RGB components,
    # as well as the components from the four neighbouring pixels located at
    # coordinates (x - 1, y), (x + 1, y), (x, y - 1) and (x, y + 1).
    #
    # When generating the pixel coordinates, we have to ensure that (x, y)
    # is never the location of pixel on the top, bottom, left or right edges
    # of the image, because those pixels don't have four neighbours.
    #
    # As such, we can't use this loop to generate the x and y coordinates:
    #
    # for y in range(0, get_height(source)):
    #     for x in range(0, get_width(source)):
    #
    # With this loop, when x or y is 0, subtracting 1 from x or y yields -1, 
    # which is not a valid coordinate. Similarly, when x equals get_width() - 1 
    # or y equals get_height() - 1, adding 1 to x or y yields a coordinate that
    # is too large.
    
    for y in range(1, get_height(source) - 1):
        for x in range(1, get_width(source) - 1):

            # Grab the pixel @ (x, y) and its four neighbours

            top_red, top_green, top_blue = get_color(source, x, y - 1)
            left_red, left_green, left_blue = get_color(source, x - 1, y)
            bottom_red, bottom_green, bottom_blue = get_color(source, x, y + 1)
            right_red, right_green, right_blue = get_color(source, x + 1, y)
            top_right_red, top_right_green, top_right_blue = \
                get_color(source, x + 1, y - 1)
            top_left_red, top_left_green, top_left_blue = \
                get_color(source, x - 1, y - 1)
            bottom_right_red, bottom_right_green, bottom_right_blue = \
                get_color(source, x + 1, y + 1)
            bottom_left_red, bottom_left_green, bottom_left_blue = \
                get_color(source, x - 1, y + 1)            
            center_red, center_green, center_blue = get_color(source, x, y)

            # Average the red components of the five pixels
            new_red = (top_red + left_red + bottom_red +
                       right_red + center_red + top_right_red +
                       top_left_red + bottom_right_red +
                       bottom_left_red) // 9

            # Average the green components of the five pixels
            new_green = (top_green + left_green + bottom_green +
                       right_green + center_green + top_right_green +
                       top_left_green + bottom_right_green +
                       bottom_left_green) // 9

            # Average the blue components of the five pixels
            new_blue = (top_blue + left_blue + bottom_blue +
                       right_blue + center_blue + top_right_blue +
                       top_left_blue + bottom_right_blue +
                       bottom_left_blue) // 9

            new_color = create_color(new_red, new_green, new_blue)
            
            # Modify the pixel @ (x, y) in the copy of the image
            set_color(target, x, y, new_color)

    return target

def detect_edges(image, threshold):
    """ (Cimpl.Image, float) -> None
    
    Modify image using edge detection.
    
    >>> image = load_image(choose_file())
    >>> detect_edges(image, 10.0)
    >>> show(image)
    """
    #Create the balck and white Color objects
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)    
    
    #visit every pixel in the image by using the range function, except those 
    #on the bottom border.
    for x in range(0, get_width(image)):
        for y in range(1, get_height(image) - 1):
            
            #Get the colour of the top pixel and find its brightness
            top_r, top_g, top_b = get_color(image, x, y)
            top_brightness = (top_r + top_g + top_b) // 3
            
            #Get the colour of the bottom pixel and find its brightness
            bottom_r, bottom_g, bottom_b = get_color(image, x, y + 1)
            bottom_brightness = (bottom_r + bottom_g + bottom_b) // 3
            
            #Calculate the contrast between the top and bottom pixel's brightness
            contrast = abs(top_brightness - bottom_brightness)
            
            #based on a threshold, the new colour will be set for the pixel.
            if contrast > threshold:
                set_color(image, x, y, black)
                
            else:
                set_color(image, x, y, white)
                
def detect_edges_better(image, threshold):
    """ (Cimpl.Image, float) -> None
    
    Modify image using edge detection.
    
    >>> image = load_image(choose_file())
    >>> detect_edges_better(image, 10.0)
    >>> show(image)
    """
    #create the black and white Coulour objects
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)    
    
    #Use the range function to visit the pixels in the image, expect those on 
    #the bottom border and on the right border 
    for x in range(0, get_width(image) - 1):
        for y in range(0, get_height(image) - 1):
            
            #Get the colour of the top pixel and find its brightness
            top_r, top_g, top_b = get_color(image, x, y)
            top_brightness = (top_r + top_g + top_b) // 3
            
            #Get the colour of the right pixel and find its brightness
            right_r, right_g, right_b = get_color(image, x + 1, y)
            right_brightness = (right_r + right_g + right_b) // 3    
            
            #Get the colour of the bottom pixel and find its brightness
            bottom_r, bottom_g, bottom_b = get_color(image, x, y + 1)
            bottom_brightness = (bottom_r + bottom_g + bottom_b) // 3
            
            #Calculate the contrast between the top and bottom pixel's brightness
            #and the top and right pixel's brightness
            contrast_bottom = abs(top_brightness - bottom_brightness)
            contrast_right = abs(top_brightness - right_brightness)
              
            #based on a threshold, the new colour will be set for the pixel.  
            if contrast_bottom > threshold or contrast_right > threshold:
                set_color(image, x, y, black)
                
            else:
                set_color(image, x, y, white)
                
def flip_vertical(image):
    """ (Cimpl.Image) -> None
    
    Flips an image through the vertical axis.
    
    >>> img = load_image(choose_file())
    >>> flip_vertical(img)
    >>> show(img)
    """
    
    target = copy(image)
    
    for x, y, col in target:
        new_width = get_width(image) - x  - 1
        set_color(image, new_width, y, col)
        
def flip_horizontal(image):
    """ (Cimpl.Image) -> None
    
    Flips an image through the vertical axis.
    
    >>> img = load_image(choose_file())
    >>> flip_vertical(img)
    >>> show(img)
    """
    
    target = copy(image)
    
    for x, y, col in target:
        new_height = get_height(image) - y  - 1
        set_color(image, x, new_height, col)
        
def test_blur():
    """ (None) -> None
    
    Test the blur function
    
    >>> test_blur()
    """    
    original = load_image(choose_file())
    blurred = blur(original)
    show(original)
    show(blurred)
    
    
def make_very_blurry(number_of_blurs):
    """ (int) -> None
    
    Make an image very blurry.
    
    >>> make_very_blurry(10)
    """    
    image = load_image(choose_file())
    
    #Iterate through each of the number of blurs
    for i in range(number_of_blurs):
        image = blur(image)  # Blur the image repeatedly

    show(image)  
    
def black_border(image):
    """ (Cimpl.Image) -> None
    
    Create a black border around the image
    
    >>> image = load_image(choose_file())
    >>> black_border(image)
    >>> show(image)
    """
    #Create the black Color object
    black = create_color(0, 0 ,0)
    
    #visit each pixel
    for x, y, (r, g, b) in image:
        
        #check to see if the pixel is part of the border
        if y not in range (10, get_height(image) - 10) or \
        x not in range (10, get_width(image) - 10):
                
                #If it is part of the border, then we set that pixel to black.
                set_color(image, x, y, black)
# Deep_Scan_Script
This python script utilizes openCV and OCR to scan a picture of an image, (take a picture (optional) and scan it's characters.  
I use scanner.py script to scan a picture of the paper

# I've Used these four steps to build it.

-used threshold to segment the foreground from the background

-used gausian blure to blur out the image.

1-use openCV edge detector to get the outline of the paper.

2-use pyimagesearch imutils module that use openCV contour finder to find contour and draw it using openCV 

3-Apply perspective transform which is grabbed from pyimagesearch module, to get the top-down view of the paper

4-apply OCR to the scan image and read the text from the image.

I use capture_pic.py script to take a picture of the picture using laptop camera
I use optical_character_reader.py script to read texts from scanned image.

I used arrparser to use cmd terminal as an image uploader.
use 'y' to make sure you passed image argument (pass it as -i/--image=image_name.extension
use 'n' if you want to take a picture using your laptop camera

The resulted read text is stored in a text file result.txt
make sure the image is exactly a paper image with four sides and good resolution

credit goes to pyimagesearch for the open resources

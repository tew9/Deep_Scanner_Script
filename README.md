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

# To Run it
1. use python scanner.py --image=<your-image-name" 
2. click <y> if you passed the image name argument
  or <n> if you want to take a picture and press enter
3. The script will run the image through pre-processing, temporarely saving the resulted image
  and convert the characters into text which is written into a text file which should be located
  in the current directory saved as ocr_result.txt
  
I used arrparser to use cmd terminal as an image uploader.
use 'y' to make sure you passed image argument (pass it as -i/--image=image_name.extension)
use 'n' if you want to take a picture using your laptop camera

* The dependencies are listed in requirements.txt file

make sure the image is exactly a paper image with four sides and good resolution

credit goes to pyimagesearch for the open resources

#import the necessary packages
from pyimagesearch.transform import four_point_transform
from optical_character_reader import optical_reader
from skimage.filters import threshold_local
from capture_pic import capture_image
import numpy as np
import argparse
import imutils
import cv2
import os


#construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()

#load the image and compute the ratio of the old height to the
#to the new height, clone it, and resize it
prompt = input("Y/N If you provided the image argument, or take a picture now")

if prompt == 'Y' or prompt == 'y':
    #use cmd console to provide the image name using argument parser
    ap.add_argument("-i", "--image", required = True,
                    help="Path to the image to the scanned")
    args = vars(ap.parse_args())
    image = cv2.imread(args['image'])
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = imutils.resize(image, height=500)

else:
    #using a video to take a picture
    img_name = capture_image(name="capured_img_")
    image = cv2.imread(img_name)


#convert the image into a grayscale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5,5), 0)
edged = cv2.Canny(gray, 75, 200)

# Show the original image and the edge detected image
print("STEP 1: Edge Detection....")

#Find the contour in the edged image, keeping only the largest one
# and initialize the screen contour
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:5]

#loop over the contours
for c in cnts:
    #approximate the contours
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # If our approximated contour has four points, then we
    # can assume that we have found our screen
    if len(approx) == 4:
        screenCnt = approx
        break
    else:
        print("Image-shape-error!!!: The image might not be perfect rectangle or not a paper image\n",
        "please check that you upload the right picture")
        exit()

# show the contour (outline) of the piece of paper
print("Step 2: Find the contour of the paper")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)

#Apply the four point transform to obtain the top-down
# view of the paper.
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

# convert the warped image to gray scale, then threshold it
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method="gaussian")
warped = (warped > T).astype("uint8") * 255


# show the original and scanned images
print("STEP 3: Apply perspective transform")
cv2.imshow("original", imutils.resize(orig, height=650))
cv2.imshow("Scanned", imutils.resize(warped, height=650))
cv2.waitKey(0)
cv2.destroyAllWindows()

#applying the OCR
#write it the warped  or scanned paper to the file temporarly
scanned_name = "{}.png".format(os.getpid())
cv2.imwrite(scanned_name, warped)

print("STEP 4: Apply OCR to the scanned image")
text = optical_reader(scanned_name)

#write it in a text file
with open("ocr_result.txt", "w") as f:
    f.write(text)
f.close()

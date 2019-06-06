from PIL import Image
import pytesseract
import os
import cv2

#load the tesseract.exe path to the system paths
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def optical_reader(img_name):
    '''
    img_name: scanned image name to be loaded
    :write the grayscale image to the disc temporarly and
    :so we can apply ocr to it and then delete it.
    '''
    # load the image and convert it to grayscale
    img = cv2.imread(img_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # temporarly write the gray image to the disc
    tem_file_name = "{}.png".format(os.getpid())
    cv2.imwrite(tem_file_name, gray)

    #Apply the OCR
    text = pytesseract.image_to_string(Image.open(tem_file_name))

    # delete the gray image file to save some disc
    os.remove(tem_file_name)

    #return the result
    return text

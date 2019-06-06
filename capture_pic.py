from pathlib import Path
import cv2

def capture_image(name):
    vid = cv2.VideoCapture(0)
    img_counter = 0

    print("[INFO] press q to close the window and c to capture the picture")

    while True:
        ret, frame = vid.read()
        cv2.imshow("Test", frame)
        if not ret:
            break
        k = cv2.waitKey(1) & 0xFF

        if k == ord("q"):
            print("[Quiting] q key is pressed")
            break
        elif k == ord("c"):
            #c key is for capturing
            img_name = str(name+"{}.png".format(img_counter))
            cv2.imwrite(img_name, frame)
            print(img_name)
            #print("{} written!".format(img_name))
            img_counter += 1

    vid.release()
    cv2.destroyAllWindows()

    return img_name

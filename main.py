import cv2
import numpy as np
from PIL import Image


def main():
    cap = cv2.VideoCapture(0)
    while True:
        # read, flip frame
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        # convert to hsv
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # lower, upper color range
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])

        # in Range
        mask = cv2.inRange(hsv_frame, lower_red, upper_red)

        # pillow image
        mask_ = Image.fromarray(mask)

        # bounding box
        bbox = mask_.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox
            frame = cv2.rectangle(
                frame,
                (
                    x1,
                    y1,
                ),
                (x2, y2),
                (0, 255, 0),
                5,
            )

        # display
        cv2.imshow("frame", frame)

        # break, if q btn pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


main()

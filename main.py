import cv2 as cv
import numpy as np
from numpy import uint8

img = np.zeros((600, 900, 3), dtype=uint8)

# skies
cv.rectangle(img, (0, 0), (900, 500), (255, 255, 85), -1)
cv.rectangle(img, (0, 500), (900, 600), (75, 180, 70), -1)
# sun
cv.circle(img, (200, 150), 60, (0, 255, 255), -1)
cv.circle(img, (200, 150), 75, (220, 255, 255), 10)

# tree stem
cv.line(img, (600, 500), (600, 420), (30, 65, 155), 25)
# tree leafs
triangle = np.array([[500, 440], [700, 440], [600, 75]], dtype=np.int32)
cv.fillPoly(img, [triangle], (75, 200, 70))

# text
font = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(img, "I Love Python", (120, 490), font, 1.5, (255, 255, 255), 2)

cv.imwrite("tree.png",img)
cv.imshow("tree", img)

cv.waitKey(0)
cv.destroyAllWindows()

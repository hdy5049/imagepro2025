import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


img = np.full((500, 500, 3), 255, dtype=np.uint8)

# sans-serif small
cv2.putText(img, "Plain", (50, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
# sans-serif normal
cv2.putText(img, "Simplex", (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
# sans-serif bold
cv2.putText(img, "Duplex", (50, 110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))
# sans-serif normal 크게
cv2.putText(img, "Simplex X 2", (200, 110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0))
# sans-serif small
cv2.putText(img, "Serif plain", (50, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))

cv2.putText(img, "Serif normal", (50, 220), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))
cv2.putText(img, "Serif bold", (50, 260), cv2.FONT_HERSHEY_TRIPLEX, 1, (0,0,0))
cv2.putText(img, "Serif plain", (50, 180), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))
cv2.putText(img, "Serif plain X 2", (200, 260), cv2.FONT_HERSHEY_TRIPLEX, 2, (0,0,0))

#cv2.putText(img, "홍도영 제작", (50, 470), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255))

font_path = "c:/Windows/Fonts/malgun.ttf"
font = ImageFont.truetype(font_path, 40)
img_pil = Image.fromarray(img)
draw = ImageDraw.Draw(img_pil)
draw.text((50, 400), "홍도영제작", font=font, fill=(255, 0, 0))
img = np.array(img_pil)

cv2.imshow("Girl", img)
cv2.waitKey()
cv2.destroyAllWindows()

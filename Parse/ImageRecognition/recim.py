import cv2
import pytesseract

def img_string():
	img = cv2.imread('/home/pin/PythonProg/img.jpg')
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#	ret, threshold_image = cv2.threshold(img, 127, 255, 0)
#	config = r'--oem 3 --psm 6'
	cv2.imshow("img", img)
	cv2.waitKey(0)

	return pytesseract.image_to_string(img, lang="rus")

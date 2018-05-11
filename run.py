import cv2
from LSBSteg import LSBSteg

def forText():
	#encoding
	file = open('abc.txt','rb')
	val = ''
	val = val + file.read()
	steg = LSBSteg(cv2.imread("download.jpeg"))
	img_encoded = steg.encode_text(val)
	cv2.imwrite("my_new_image.png", img_encoded)
	#decoding
	im = cv2.imread("my_new_image.png")
	steg = LSBSteg(im)
	print("Text value:",steg.decode_text())



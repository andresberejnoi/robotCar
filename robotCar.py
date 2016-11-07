import cv2
import time
import numpy as np
from parameter_parser import parser


#This script is written with OpenCV 3 in mind

def setup():
	"""Sets up the conditions for the program to run"""
	filename = input("Enter the filename containing the parameters: ")
	P = parser()
	P.read_file(filename)
	return P.get_params()

def locate_obtacle(frame,numCnts=1):
    """
    This function is supposed to be called for every frame.
    Therefore, it is have unnecessary overhead of function calls.
    I am just writing as a separate piece for clarity right now
    frame: numpy array (the current frame from the video)
    numCnts: int (number of contours that should be recognized)
    """
    _,cnts,_ = cv2.findContours(frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)    #finds all contours in the image
    if numCnts == 1:
        cnts = max(cnts, key = cv2.contourArea)
    else:
        cnts = sorted(cnts,key = cv2.contourArea,reverse=True)[:numCnts]                #leaves only the biggest contours 
    
    
    
    

def main():
	""""""
	params = setup()
	path = params["path"]
	print(params)

	cap = cv2.VideoCapture(path)
	while 1:
	
		grabbed,img = cap.read()
		if not grabbed:
			break
		cv2.imshow("Normal video",img)
		k = cv2.waitKey(40) & 0xFF
		if k==27 or k==ord('q') or k==ord('Q'):
			break

main()

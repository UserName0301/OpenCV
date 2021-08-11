

import cv2
import numpy as np 

def draw_line(event,x,y,flags,param):
		global x1,y1,flag
		if x>=0 and x<=1270 and y>=35 and y<=650:
			if event == cv2.EVENT_LBUTTONDOWN:
				flag = 1
				x1 = x
				y1 = y 
			if flag == 1 and event == cv2.EVENT_MOUSEMOVE:
				cv2.line(img,(x1,y1),(x,y),(255,255,255),1)
				x1 = x
				y1 = y 
			if event == cv2.EVENT_LBUTTONUP:
				flag = 0
			print(x,y)
		else:
			global flag1,save,choose
			if x>=1240 and x<=1270 and y>=0 and y<=30:
				if event == cv2.EVENT_LBUTTONDOWN:
					flag1 = 2
				if event == cv2.EVENT_LBUTTONUP and flag1 ==2:
					flag1 = 1
			if x>=0 and x<=30 and y>=0 and y<=30:
				if event == cv2.EVENT_LBUTTONDOWN:
					save = 2
				if event == cv2.EVENT_LBUTTONUP and save ==2:
					save = 1
			if save == 1 and x>=30 and x<=130 and y>=70 and y<=120:
				if event == cv2.EVENT_LBUTTONDOWN:
					choose = 2
				if event == cv2.EVENT_LBUTTONUP and choose ==2:
					choose = 1

choose = 0
save = 0
flag1 = 0
flag = 0
x1 = 0
y1 = 0
# Create a black image, a window and bind the function to window
img = np.zeros((650,1270,3), np.uint8)
cv2.line(img,(0,30),(1270,30),(255,0,255),3)
cv2.line(img,(1240,0),(1240,30),(255,0,255),1)
cv2.line(img,(30,0),(30,30),(255,0,255),1)
font = cv2.FONT_HERSHEY_SIMPLEX # chon font chu
# viet len anh img dong chu opencv voi chu 'o' dau tien o vi tri tung do 200 va hoanh do 0 voi font nhu tren va do to = 8 cung voi mau (255,0,255) va do day than chu la 100 va type LINE_AA
cv2.putText(img,'x',(1245,25), font, 1,(255,255,255),1,cv2.LINE_AA)
cv2.putText(img,'s',(5,20), font, 1,(255,255,255),1,cv2.LINE_AA)


cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_line)
while True:
	cv2.imshow('image',img)
	if save == 1:
		img1 = np.zeros((150,360,3), np.uint8)
		while True:
			cv2.imshow("IMG",img1)
			cv2.putText(img1,'Do you want to save?',(5,50), font, 1,(255,255,255),1,cv2.LINE_AA)
			cv2.rectangle(img1,(30,70),(130,120),(255,0,0),1)
			cv2.putText(img1,'Yes',(50,105), font, 1,(255,255,255),1,cv2.LINE_AA)
			cv2.rectangle(img1,(220,70),(320,120),(255,0,0),1)
			cv2.putText(img1,'No',(250,105), font, 1,(255,255,255),1,cv2.LINE_AA)
			#cv2.rectangle(img1,(0,0),(512,512),(255,0,0),3)
			#cv2.imwrite("Coppy.jpg", img)
			if choose == 1:
				cv2.imwrite("Coppy.jpg", img)
				break
			k=cv2.waitKey(1)
			if k == ord('b') or flag1 == 1:
				break
		save = 0
	k=cv2.waitKey(1)
	if k == ord('b') or flag1 == 1:
		break
cv2.destroyAllWindows()
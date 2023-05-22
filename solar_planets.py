import cv2
img=cv2.imread("solar-system.jpg")


cv2.putText(img,"Sun",(90,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mercury",(120,240),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(200,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Earth",(295,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mars",(390,240),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Jupiter",(590,370),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Saturn",(760,290),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Uranus",(980,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Neptune",(1130,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.5,color=(255,255,255))
cv2.imshow("Displaying Images",img)
cv2.waitKey(0)
cv2.imwrite("solarsystemwithname.jpg",img)
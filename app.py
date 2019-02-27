import cv2
import numpy as np
import matplotlib.pyplot as plt



#read image through open CV

img=cv2.imread('test.png')


while True:
     cv2.imshow('Test Pic',img)
     
     #Wait for 1 ms and check Esc press or not 

     if cv2.waitKey(1) & 0xFF==27:
         break
          
      


#Close the Image window if any key press happened....

cv2.destroyAllWindows()




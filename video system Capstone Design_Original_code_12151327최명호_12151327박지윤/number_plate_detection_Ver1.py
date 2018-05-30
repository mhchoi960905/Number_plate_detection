import cv2
import numpy as np
import os
import sys

def play_videoFile(filePath,mirror=False):
    
    cap = cv2.VideoCapture(filePath)
    cv2.namedWindow('Video Life2Coding',cv2.WINDOW_AUTOSIZE)
    while True:
        ret_val, frame = cap.read()
        #frame = frame[200:5000,450:1000]
        Gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #Blur = cv2.GaussianBlur(Gray,(3,3),0)
        Canny = cv2.Canny(Gray,100,200)
        if mirror:
            frame = cv2.flip(frame, 1)
        ret, thresh = cv2.threshold(Canny,127,255,0)
        image, contours, hieracy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        #image = cv2.drawContours(frame, contours, -1, (0,255,0) , 1)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
        rects = []
        for c in contours:
             peri = cv2.arcLength(c, True)
             approx = cv2.approxPolyDP(c, 0.02 * peri, True)
             x, y, w, h = cv2.boundingRect(approx)
             #rect = cv2.minAreaRect(approx)
             #box = cv2.boxPoints(rect)
             #box = np.int0(box)
             
    
             if len(approx) == 4 and w/h >= 2.1 and w/h<=2.3 and w>150:
            # if height is enough
            # create rectangle for bounding
                rect = cv2.minAreaRect(approx)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                #rect = (x, y, w, h)
                #rects.append(rect)
                #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 10);
                cv2.drawContours(frame,[box],0,(0,0,255),10)
        cv2.imshow('Video Life2Coding',frame)
 
        if cv2.waitKey(25) == 27:
            break  # esc to quit
    cap.release()
    cv2.destroyAllWindows()
    
    
def main():
    play_videoFile('source.avi',mirror = False)
    
if __name__ == '__main__':
    main()
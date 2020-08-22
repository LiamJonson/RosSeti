import cv2
import os

def nothing(x):
    pass


dir = 'D:\PycharmProject\RosSeti\Sensors\\'
ImgNameList = os.listdir(dir+'images')
print(ImgNameList)

#cv2.namedWindow('result')                                   #// for video
#cv2.createTrackbar('minb', 'result',0, 255, nothing)        #// for video Trackbar
#cv2.createTrackbar('ming', 'result',0, 255, nothing)        #// for video Trackbar
#cv2.createTrackbar('minr', 'result',0, 255, nothing)        #// for video Trackbar
#
#cv2.createTrackbar('maxb', 'result',0, 255, nothing)        #// for video Trackbar
#cv2.createTrackbar('maxg', 'result',0, 255, nothing)        #// for video Trackbar
#cv2.createTrackbar('maxr', 'result',0, 255, nothing)        #// for video Trackbar

for i in ImgNameList:
    img = cv2.imread(dir +'\images\\'+ i)

    #cv2.imshow('image',img)
    #minb = cv2.getTrackbarPos('minb','result')                 #// for video Trackbar
    #ming = cv2.getTrackbarPos('ming', 'result')                #// for video Trackbar
    #minr = cv2.getTrackbarPos('minr', 'result')                #// for video Trackbar

    #maxb = cv2.getTrackbarPos('maxb', 'result')                #// for video Trackbar
    #maxg = cv2.getTrackbarPos('maxb', 'result')                #// for video Trackbar
    #maxr = cv2.getTrackbarPos('maxb', 'result')                #// for video Trackbar

    mask = cv2.inRange(img, (56 , 78, 80), (255, 255, 255))
    cv2.imshow('image', mask)
    #result = cv2.bitwise_and(img, img, mask=mask)              #// for video
    #cv2.imshow('result',result)                                #// for video
    cv2.waitKey(0)
    cv2.destroyAllWindows()
import cv2
import os
import dlib
import xml.etree.cElementTree as pars
import numpy as np

dir = 'D:\PycharmProject\RosSeti\Sensors\\'
images = []
annots = []
ImgNameList = os.listdir(dir+'images')
print(ImgNameList)

for filName in ImgNameList:
    print(filName)
    image = cv2.imread(dir+'/image/'+filName)


    #image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    OnlyFileName = filName.split('.')[0]

    e = pars.parse(dir+'/annots/'+OnlyFileName+'.xml')
    root = e.getroot()
    #an = root.find('object')
    for an in root.findall('object'):
        an = an.find('bndbox')
        x = int(an.find('xmin').text)
        y = int(an.find('ymin').text)
        x2 = int(an.find('xmax').text)
        y2 = int(an.find('ymax').text)
        if (x2 - x) / (y2 - y) < 1:
            images.append(image)
            annots.append([dlib.rectangle(left=x, top=y, right=x2, botton=y2)])  #//warning

            options = dlib.simple_object_detector_training_options
            options.be_verbose = True
            detector = dlib.train_simple_object_detector(images, annots, options)
            detector.save('tld.svm')
            print("detect saved")







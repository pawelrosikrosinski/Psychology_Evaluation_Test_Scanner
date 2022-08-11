#!/bin/python

import cv2
import os


import numpy as np
import math

f = open("images/new", "r")
new = f.readline()

pth = "images/" + new[:-1]
print(pth)




def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage


before = cv2.imread(pth + '/skan-001.png')



from skimage import io
from skimage.transform import rotate
from skimage.color import rgb2gray
from deskew import determine_skew
from matplotlib import pyplot as plt

def deskew(img):
    image = img
    grayscale = rgb2gray(image)
    angle = determine_skew(grayscale)
    rotated = rotate(image, angle, resize=False) * 255
    return rotated.astype(np.uint8)

im_mod = deskew(before)


cv2.imwrite("test4.png", im_mod)



cv2.imwrite("bufor.png", im_mod)
after = cv2.imread('wzory/wzor-skan-001.png')
before = cv2.imread("bufor.png")


before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)

thresh1 = cv2.threshold(before_gray, 100, 255, cv2.THRESH_TOZERO_INV)[1]

blurred = cv2.GaussianBlur(thresh1, (5, 5), 0)

thresh = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

thresh = np.invert(thresh)



cv2.imwrite("bufor_mask1.png", thresh)


height, width = thresh.shape

cut_start_wid = round(width * 0.8037)
cut_stop_wid = round(width * 0.93)



cut_start_hei = round(height * 0.2842)
cut_stop_hei = round(height * 0.8915)


cropped_image = thresh[cut_start_hei:cut_stop_hei, cut_start_wid:cut_stop_wid]


contours = cv2.findContours(cropped_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

mask = np.zeros(cropped_image.shape, dtype='uint8')
test = np.zeros(cropped_image.shape, dtype='uint8')
filled_after = after.copy()
print("kontury = " + str(len(contours)))

for c in contours:
    area = cv2.contourArea(c)
    if area > 2:

        if len(c) >= 5:

            ellipse = cv2.fitEllipse(c)


            A = ellipse[1][0] * ellipse[1][1]

            if A > 300 and A < 7500:

                cv2.ellipse(mask, ellipse,  (255,0, 255), -1, -1)

cv2.imwrite("testdiff2.png", mask)

new_high = cut_stop_hei - cut_start_hei
new_wid = cut_stop_wid - cut_start_wid

new_high_part = math.floor(new_high / 20)
new_wid_part = math.floor(new_wid / 4)

cropped_image = mask

for x in range(20):

    cropped_image1 = cropped_image[x*new_high_part:(x+1)*new_high_part, 0:new_wid_part]
    cropped_image2 = cropped_image[x*new_high_part:(x+1)*new_high_part, new_wid_part:new_wid_part*2]
    cropped_image3 = cropped_image[x*new_high_part:(x+1)*new_high_part, new_wid_part*2:new_wid_part*3]
    cropped_image4 = cropped_image[x*new_high_part:(x+1)*new_high_part, new_wid_part*3:new_wid_part*4]

    average_color_row1 = np.average(cropped_image1, axis=0)
    average_color1 = np.average(average_color_row1, axis=0)
    average_color1 = average_color1


    average_color_row2 = np.average(cropped_image2, axis=0)
    average_color2 = np.average(average_color_row2, axis=0)
    average_color2 = average_color2

    average_color_row3 = np.average(cropped_image3, axis=0)
    average_color3 = np.average(average_color_row3, axis=0)
    average_color3 = average_color3

    average_color_row4 = np.average(cropped_image4, axis=0)
    average_color4 = np.average(average_color_row4, axis=0)
    average_color4 = average_color4



    data = {
        '1': average_color1,
        '2': average_color2,
        '3': average_color3,
        '4': average_color4
    }
    print(max(data, key=data.get))

    f = open(pth + "/stai.txt", "a")
    f.write(max(data, key=data.get) + '\n')
os.remove(pth + "/skan-001.png")


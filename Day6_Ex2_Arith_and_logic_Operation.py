#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 23:09:40 2020

@author: Asst. Prof. Apicharti Hajaturus
 การประมวลผลเพื่อทำการ ลบภาพ 
 ตัวอย่างการ น่ำภาพมาบวก
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # ถอดภาพจาก กล้องเว็บแคม เป็นภาพนิ่งที่ละภาพ เก็บในตัวแปร frame
    _, frame = cap.read()

    # แปลงภาพ จาก BGR รูปแบบ ไปเป็น รูปแบบ  RGB
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # แปลงภาพ จาก BGR รูปแบบ ไปเป็น รูปแบบ  HSV
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # แปลงภาพ จาก BGR รูปแบบ ไปเป็น รูปแบบ  GRAY
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    


    # ขั้นตอนการกำหนด threshold value 50 - 255 ให้มีค่าเป็น  255    
    ret, mask = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
   
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    cv2.imshow('mask',mask_inv)
    #cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
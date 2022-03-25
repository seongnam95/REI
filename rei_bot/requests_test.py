from PySide6.QtCore import QThread, QObject, Signal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
from seleniumrequests import Chrome
from PIL import Image

import time
import webbrowser
import json
import requests
import base64
from pathlib import Path
from urllib import parse
import cv2
import numpy as np
from PIL import Image

headers = {
    "Host": "cloud.eais.go.kr",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"
}
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('headless')  # 크롬 화면 숨기기
# chrome_options.add_argument("no-sandbox")  #
# chrome_options.add_argument('window-size=1920x1080')  # 해상도 설정
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("disable-gpu")  # 가속 사용 x
# chrome_options.add_argument("lang=ko_KR")  # 가짜 플러그인 탑재
# chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
#                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")  # user-agent 이름 설정
#
# driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# driver.get(url)
# driver.implicitly_wait(5)

# a = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/table/tbody/tr/td/div/nobr')
# print(a.get_attribute("innerText"))

# base64_image = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/canvas').screenshot_as_base64
# output_image = base64.b64decode(base64_image)
# with open("test.txt") as f:
#     content = f.read().encode('utf-8')


def detect_box(image, line_min_width=15):
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    th1, img_bin = cv2.threshold(gray_scale, 150, 225, cv2.THRESH_BINARY)
    kernal_h = np.ones((1, line_min_width), np.uint8)
    kernal_v = np.ones((line_min_width,1), np.uint8)
    img_bin_h = cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal_h)
    img_bin_v = cv2.morphologyEx(~img_bin, cv2.MORPH_OPEN, kernal_v)
    img_bin_final = img_bin_h | img_bin_v
    final_kernel = np.ones((3, 3), np.uint8)
    img_bin_final = cv2.dilate(img_bin_final, final_kernel, iterations=1)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)

    cv2.imshow('img', img_bin_final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(labels)
    return stats, labels


image_path = 'tab.png'
image = cv2.imread(image_path)

img = detect_box(image)

# img = np.full(shape=(512,512,3),fill_value=255,dtype=np.uint8)
# text="Hello OpenCV!(한글)"
# org=(50,100)
# font=cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,text,org,font,1,(255,0,0),2)
# size, BaseLine=cv2.getTextSize(text,font,1,2)
# cv2.rectangle(img,org,(org[0]+size[0],org[1]-size[1]),(0,0,255))
# cv2.circle(img,org,3,(255,0,255),2)
# cv2.imshow("A",img)
# cv2.waitKey()
# cv2.destroyAllWindows()


#
# image = cv2.imread(image_path)
#
# gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# th1, img_bin = cv2.threshold(gray_scale, 150, 225, cv2.THRESH_BINARY)
# img_bin = ~img_bin
#
# line_min_width = 15
# kernal_h = np.ones((1, line_min_width), np.uint8)
# kernal_v = np.ones((line_min_width, 1), np.uint8)
#
# img_bin_final = kernal_h|kernal_v
#
# print(img_bin_final)
# image = Image.open('tab.png')
# scale = cv2.cvtColor('tab.png', cv2.COLOR_BGR2GRAY)
# _, img_bin = cv2.threshold(scale, 150, 225, cv2.THRESH_BINARY)
# img_bin = ~ img_bin

# print(content['d'][2]['b'][0][0][6][0][6][0][0][2][0][0])
# with open("tests.png", 'wb') as f:
#     f.write(output_image)


# data = parse.unquote(output_image)
# res = data.replace('+', ' ')
# print(res)
#
# img = Image.open('test1.png')
# img_rgb = img.convert('RGB')
# img_rgb.save('aa.pdf')
#
# with open("test.txt", 'wb') as f:
#     f.write(output_image)
#
# with open("test.pdf", 'wb') as f:
#     f.write(output_image)

#
# driver.find_element(By.ID, 'membId').send_keys('haul1115')
# driver.find_element(By.ID, 'pwd').send_keys('ks05090818@')
# driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div/div[1]/div[1]/button').click()

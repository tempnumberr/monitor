import requests
import base64
import cv2 as cv
# encoding:utf-8

import requests
import base64
import cv2 as cv
import json
from datetime import datetime
'''
车型识别
'''
import time

def delay(seconds):
    time.sleep(seconds)
def chexing(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/car"
    # 二进制方式打开图片文件
    #f = open('车辆属性识别.jpg', 'rb')

    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)

    #img = base64.b64encode(f.read())
    #params = {"image":img,"top_num":5}

    params = {"image": base64_image}
    access_token = '24.4469483ddc529dc083d91297adf54bc1.2592000.1722760346.282335-89943115'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    delay(0.5)
    # if response:
    #     print (response.json())
    if response:
            data = response.json()
            print(data)
            result = data['result']
            print(result)
            # text1 = result[0]['name']
            # delay(0.4)
            # return text1
            # 生成带时间戳的文件名
            now = datetime.now()
            timestamp = now.strftime("%Y%m%d_%H%M%S")
            filename = f"result_{timestamp}.txt"

            # 将 data 写入文本文件
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print("a")
            text1=""
            for i in result:
                text1+=i["name"]
                text1+="\n"
                print(i )
            #text1 = result[0]['name']
            return str(text1)
    return str(" ")
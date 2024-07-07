import requests
import base64
import cv2 as cv
from ai.car2 import chexing

# opencv 图片
def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image)
    params = {"image":base64_image}
    access_token = '24.4469483ddc529dc083d91297adf54bc1.2592000.1722760346.282335-89943115'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    #type1=chexing(img)
    if response:
        data = response.json()
        num = data['vehicle_num']['car']
        for item in data['vehicle_info']:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
        # 定义要绘制的文字
            text = item['type']
            position = (x1, y1-2)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 255, 255)  # 红色
            thickness = 1

            # brand = chexing(img)
            # text=text+brand


            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
            # cv.imshow('Rectangle', img)
            # return img
    return img, num
    # # 等待按键，然后关闭窗口
    # cv.waitKey(0)
    # cv.destroyAllWindows()

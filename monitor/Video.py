from PyQt5.QtCore import QThread
import cv2 as cv
from PyQt5.QtCore import pyqtSignal
from ai.car import vehicle_detect
from ai.car2 import chexing
# 重写run()方法: 线程执行的内容
# Thread的实例对象.start()  run()就会自动执行
class Video(QThread):
    # 使用信号与槽槽函数向外传递数据
    #    发送者   Video
    #    信号类型  自定义信号类型(参数信号所能传递的数据)
    #    接收者   （线程所在的Dialog）
    #    槽函数   （接收者类：功能方法）
    send = pyqtSignal(int, int, int, bytes,int,int,str) #emit
    def __init__(self,video_id):
        super().__init__()
        # 准备工作
        self.th_id = 0
        if video_id == 'data/vd1.mp4':
            self.th_id = 1
        if video_id == 'data/vd2.mp4':
            self.th_id = 2
        self.dev = cv.VideoCapture(video_id)
        self.dev.open(video_id)

    def run(self):
        # 耗时操作
        while True:
            ret, frame = self.dev.read()
            result = chexing(frame)
            print("re")
            frame, num = vehicle_detect(frame)

            if not ret:
                print('no')
            # car
            h, w, c = frame.shape
            img_bytes = frame.tobytes()
            print("b")
            self.send.emit(h, w, c, img_bytes,self.th_id,num,result)
            print("c")
            QThread.usleep(100000)




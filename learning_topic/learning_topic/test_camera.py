#!/usr/bin/env python3
# coding=utf-8
import cv2
import time

cv2.namedWindow("camera", 1)
# 开启ip摄像头
video = "http://192.168.31.219:8080/greet.html"  # 此处@后的ipv4 地址需要修改为自己的地址
#！！！！划重点了！！！！这个地址就是上面记下来的局域网IP
capture = cv2.VideoCapture(video)

num = 0
while True:

    success, img = capture.read()
    if not success:
        print('error')
        break
    # 不进行旋转
#     cv2.imshow("camera", img)


    # 获取长宽
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    # 进行旋转
    M = cv2.getRotationMatrix2D(center, -90, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))
    # 若不关参数，参数也会被旋转，影响效果
    
     # !!!处理帧函数
    img = process_frame(rotated)
    
    cv2.imshow("camera", img)
    
    # 按键处理，注意，焦点应当在摄像头窗口，不是在终端命令行窗口
    key = cv2.waitKey(10)

    if key == 27:
        # 按esc键退出
        print("esc break...")
        break
    if key == ord(' '):
        # 按空格 保存一张图像 图片的路径就在下面的filename里面
        num = num + 1
        filename = "./img/frames_%s.jpg" % num
        cv2.imwrite(filename, img)

capture.release()
cv2.destroyWindow("camera")

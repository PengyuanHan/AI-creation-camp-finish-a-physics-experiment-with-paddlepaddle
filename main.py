import paddlehub as hub
import matplotlib.pylab as plt
from analysis_movement import *
from get_total_time import *
from get_center_point import *

#len_object = input('please input object length:')
#len_object = float(len_object)
len_object = 0.045
#variable_distance = input('please input variable_distance:')  #40
#variable_distance = int(variable_distance)
variable_distance = 10
#vedio_path = input('please input vedio_path:')
vedio_path = 'VID_20210307_154439.mp4'
#input_object = input('please input the object name:') #'bottle'
input_object = 'bottle'

object_detector = hub.Module(name = 'yolov3_resnet34_coco2017')
cap = cv2.VideoCapture(vedio_path)
#获取视频的时间和每帧的时间
print('获取视频的时间和每帧的时间')
total_second, cost_eachfra, fraNum = get_total_time(vedio_path)

location = []
recall_points = []
recall_points_new = []
move_fra = 0
img_size = (224, 224, 3)
rate = 0
count = 0

while 1:
    ret, img = cap.read()
    count += 1
    if ret == True:
        img_size = img.shape
        result = object_detector.object_detection(images=[img])
        center_points, img_object_h = get_center_point(result, input_object) #获得中心点
        if move_fra == 2:
            rate = len_object / img_object_h
        location.append(center_points)
        print('location is:{}'.format(location))
        print('recall_points is :{}'.format(recall_points))
        if len(location) == 2:
            if location[0] != location[1]:
                move_fra += 1
                recall_points.append(location[0])
                recall_points.append(center_points)
                location.remove(location[0])
                #move
            else:
                location.remove(location[0])
                #print("---object is not move---")
        else:
            #print('---location is not enough---')
            continue
    else:
        #print('---not read the vedio---')
        continue
    print('正在处理第{}帧......'.format(count))
    if count == fraNum:
        break
#图像大小：
print('图像大小：')
print(img_size)
#运动时间的计算
print('计算运动时间')
move_time = move_fra * cost_eachfra
#求平均速度
print('求平均速度')
all_ = len(recall_points)
x, y = recall_points[0][0]
x_, y_ = recall_points[all_ - 1][0]
aver_speed = ((y_ - y) * rate) / move_time
#重写recall_points
for point in recall_points:
    recall_points_new.append(point[0])
#获得加速度
print('获得加速度')
aver_accelebration = processing_data(recall_points_new, cost_eachfra, variable_distance, rate)
#分析物体运动
print('分析物体的运动')
move_img = analysis_movement(img_size, recall_points_new)
plt.imshow(move_img)
print(' aver_speed is :{} m/s \n aver_acecelebration is :{} m/s*2\n total_move_time is :{} s \n'.format(aver_speed, aver_accelebration, move_time))
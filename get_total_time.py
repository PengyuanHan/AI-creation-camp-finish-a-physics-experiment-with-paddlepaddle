import cv2

def get_total_time(vedio_path):
    cap = cv2.VideoCapture(vedio_path)
    if cap.isOpened():
        rate = cap.get(5)  # 获取帧率
        fraNum = cap.get(7)  # 获取帧数
        print(fraNum)
        duration = fraNum / rate
        total_second = 0
        total_second += duration
        cost_eachfra = total_second / fraNum
        return total_second, cost_eachfra, fraNum
    else:
        print('---can not open the vedio_path----')
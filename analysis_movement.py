import numpy as np
import cv2

def analysis_movement(img_size, points):
    img = np.zeros(img_size)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for point in points:
        x, y = point
        x = int(x)
        y = int(y)
        point = (x, y)
        cv2.circle(img, point, 2, (0, 255, 0))
    #cv2.putText(img, "aver_a= %.5f" % (aver_accelebration), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    #cv2.putText(img, "aver_v= %.5f" % (aver_speed), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0))
    return img
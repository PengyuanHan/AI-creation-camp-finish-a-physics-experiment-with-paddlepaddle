def get_center_point(result, input_object):
    img_object_h = 0
    center_points = []
    for dictionary in result:
        data = dictionary['data']
        for each in data:
            if each['label'] == input_object:
                center_w = (each['right'] - each['left']) / 2 + each['left']
                center_h = (each['bottom'] - each['top']) / 2 + each['top']
                img_object_h = each['bottom'] - each['top']
                center_point = (center_w, center_h)
                center_points.append(center_point)
    return center_points, img_object_h
def processing_data(center_points, cost_eachfra, variable_distance, rate): #variable_distance位移变化量

    recall_change_pixel = [] #记录改变的pixel
    recall_changed = []
    accelebration_list = []
    sum_accelebration = 0
    changed_move_time = cost_eachfra * variable_distance
    len_points = len(center_points)
    print(len_points)
    times = int(len_points / variable_distance)
    new_len = times * variable_distance
    print(new_len)
    if len_points != new_len:
        for i in range(new_len, len_points):
            center_points.pop()
    else:
        pass
    flag = 0
    print('center_points:')
    print(center_points)
    for point in center_points:
        if flag == 0:
            x, center_point_s = point
        flag += 1
        if flag == variable_distance:
            x_, center_point_f = point
            a_team = center_point_s -  center_point_f
            recall_change_pixel.append(a_team)
            flag = 0
    print('recall_change_pixel is:{}'.format(recall_change_pixel))
    lag = 0
    for change_pixel in recall_change_pixel:
        if lag == 0:
            distance_b = change_pixel
        lag = lag + 1
        if lag == 2:
            distance_a = change_pixel
            team_a = distance_b - distance_a
            recall_changed.append(team_a)
            lag = 0
    print('recall_changed is:{}'.format(recall_changed))
    for recall in recall_changed:
        accelebration = (recall * rate) / (changed_move_time * changed_move_time)
        accelebration_list.append(accelebration)
    print('accelebration_list is {}:'.format(accelebration_list))
    for accelebrate in accelebration_list:
        sum_accelebration += accelebrate
    aver_accelebration = sum_accelebration / len(accelebration_list)

    return aver_accelebration
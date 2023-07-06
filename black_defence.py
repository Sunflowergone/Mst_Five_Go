import numpy as np


# 存在的问题：有些情况下只需下一子就能够封堵多处危险，如01011010，算两个活三，但是其实只用一个子就能堵住

def boardevaluate_for_black(root, color):
    c = 0
    if color == 'white':
        c = 2
    elif color == 'black':
        c = 1
    points = 0
    fives = []
    live_fours = []
    chong_fours = []
    live_threes = []
    sleep_threes = []
    live_twos = []
    sleep_twos = []
    pos_point = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                 [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
                 [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
                 [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
                 [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                 [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0],
                 [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                 [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 4, 3, 2, 1, 0],
                 [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
                 [0, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 1, 0],
                 [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # 返回以给定点为中心的长度为9的列表，若超出棋盘范围，则超出的部分全部用对手的棋代替
    def hor_list(root, pos):
        """返回水平方向的列表"""
        x = pos[1]
        y = pos[0]
        left = x - 4
        right = x + 4
        if x - 4 < 0:
            comp = np.zeros((4 - x,))
            comp += 3 - c
            return np.hstack((comp, root[y, 0:right + 1]))
        elif x + 4 > 14:
            comp = np.zeros((x - 10,))
            comp += 3 - c
            return np.hstack((root[y, left:15], comp))
        else:
            return root[y, left:right + 1]

    def ver_list(root, pos):
        """返回竖直方向的列表"""
        x = pos[1]
        y = pos[0]
        up = y - 4
        down = y + 4
        if y - 4 < 0:
            comp = np.zeros((4 - y,))
            comp += 3 - c
            return np.hstack((comp, root[0:down + 1, x]))
        elif y + 4 > 14:
            comp = np.zeros((y - 10,))
            comp += 3 - c
            return np.hstack((root[up:15, x], comp))
        else:
            return root[up:down + 1, x]

    def lefttop_rightdown_list(root, pos):
        """返回左上到右下的列表"""
        x = pos[1]
        y = pos[0]
        left = max(0, x - 4)
        right = min(15, x + 5)
        up = max(0, y - 4)
        down = min(15, y + 5)
        lefttop_dis = min(x - left, y - up)
        rightdown_dis = min(right - x - 1, down - y - 1)
        x_start = x - lefttop_dis
        y_start = y - lefttop_dis
        x_ = x_start
        y_ = y_start
        list = []
        for i in range(rightdown_dis + lefttop_dis + 1):
            list.append(root[y_][x_])
            x_ += 1
            y_ += 1
        comp1 = np.array(list)
        if lefttop_dis < 4 and rightdown_dis < 4:
            comp2 = np.zeros((4 - lefttop_dis,))
            comp2 += 3 - c
            comp3 = np.zeros((4 - rightdown_dis,))
            comp3 += 3 - c
            return np.hstack((comp2, comp1, comp3))
        elif lefttop_dis < 4:
            comp2 = np.zeros((4 - lefttop_dis,))
            comp2 += 3 - c
            return np.hstack((comp2, comp1))
        elif rightdown_dis < 4:
            comp3 = np.zeros((4 - rightdown_dis,))
            comp3 += 3 - c
            return np.hstack((comp1, comp3))
        else:
            return comp1

    def leftdown_righttop_list(root, pos):
        """返回从左下到右上的列表"""
        x = pos[1]
        y = pos[0]
        left = max(0, x - 4)
        right = min(15, x + 5)
        up = max(0, y - 4)
        down = min(15, y + 5)
        leftdown_dis = min(x - left, down - y - 1)
        righttop_dis = min(right - x - 1, y - up)
        x_start = x - leftdown_dis
        y_start = y + leftdown_dis
        x_ = x_start
        y_ = y_start
        list = []
        for i in range(leftdown_dis + righttop_dis + 1):
            list.append(root[y_][x_])
            x_ += 1
            y_ -= 1
        comp1 = np.array(list)
        if leftdown_dis < 4 and righttop_dis < 4:
            comp2 = np.zeros((4 - leftdown_dis,))
            comp2 += 3 - c
            comp3 = np.zeros((4 - righttop_dis,))
            comp3 += 3 - c
            return np.hstack((comp2, comp1, comp3))
        elif leftdown_dis < 4:
            comp2 = np.zeros((4 - leftdown_dis,))
            comp2 += 3 - c
            return np.hstack((comp2, comp1))
        elif righttop_dis < 4:
            comp3 = np.zeros((4 - righttop_dis,))
            comp3 += 3 - c
            return np.hstack((comp1, comp3))
        else:
            return comp1

    # 计算分数,list是长度固定为9的列表，位于list正中的那一个（即list[4]）即为考察的棋子
    def part_point(pos, dir, list):
        """返回某个棋子沿某个方向所得的分数"""
        # 先算出考察的棋子相连的相同棋子有多少个，再算分
        i = pos[0]
        j = pos[1]
        left_connected = 0
        right_connected = 0
        while list[3 - left_connected] == c:
            left_connected += 1
            if left_connected == 4:
                break
        while list[5 + right_connected] == c:
            right_connected += 1
            if right_connected == 4:
                break

        # 算分
        if left_connected + right_connected >= 4:  # 左右相连的棋子数大于等于4，即有大于等于5个子连在一起
            fives.append(1)


        elif left_connected + right_connected == 3:  # 左右相连的棋子数等于3，可能为活四或者冲四
            if list[3 - left_connected] == 0 and list[5 + right_connected] == 0:  # 活四
                if dir == 'hor':
                    if ((i, j - left_connected), (i, j + right_connected)) not in live_fours:
                        live_fours.append(((i, j - left_connected), (i, j + right_connected)))
                elif dir == 'ver':
                    if ((i - left_connected, j), (i + right_connected, j)) not in live_fours:
                        live_fours.append(((i - left_connected, j), (i + right_connected, j)))
                elif dir == 'lefttop':
                    if ((i - left_connected, j - left_connected),
                        (i + right_connected, j + right_connected)) not in live_fours:
                        live_fours.append(
                            ((i - left_connected, j - left_connected), (i + right_connected, j + right_connected)))
                elif dir == 'leftdown':
                    if ((i + left_connected, j - left_connected),
                        (i - right_connected, j + right_connected)) not in live_fours:
                        live_fours.append(
                            ((i + left_connected, j - left_connected), (i - right_connected, j + right_connected)))

            elif (list[3 - left_connected] == 0 and list[5 + right_connected] == 3 - c) or \
                    (list[3 - left_connected] == 3 - c and list[5 + right_connected] == 0):  # 冲四
                if dir == 'hor':
                    if ((i, j - left_connected), (i, j + right_connected)) not in chong_fours:
                        chong_fours.append(((i, j - left_connected), (i, j + right_connected)))
                elif dir == 'ver':
                    if ((i - left_connected, j), (i + right_connected, j)) not in chong_fours:
                        chong_fours.append(((i - left_connected, j), (i + right_connected, j)))
                elif dir == 'lefttop':
                    if ((i - left_connected, j - left_connected),
                        (i + right_connected, j + right_connected)) not in chong_fours:
                        chong_fours.append(
                            ((i - left_connected, j - left_connected), (i + right_connected, j + right_connected)))
                elif dir == 'leftdown':
                    if ((i + left_connected, j - left_connected),
                        (i - right_connected, j + right_connected)) not in chong_fours:
                        chong_fours.append(
                            ((i + left_connected, j - left_connected), (i - right_connected, j + right_connected)))
            else:
                pass

        elif left_connected + right_connected == 2:  # 左右相连的棋子数等于2，可能为冲四，活三，眠三
            if list[3 - left_connected] == 3 - c and list[5 + right_connected] == 3 - c:
                pass
            elif list[3 - left_connected] == 0 and list[5 + right_connected] == 3 - c:
                if list[3 - left_connected - 1] == 0:  # 眠三
                    if dir == 'hor':
                        if ((i, j - left_connected), (i, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(((i, j - left_connected), (i, j + right_connected)))
                    elif dir == 'ver':
                        if ((i - left_connected, j), (i + right_connected, j)) not in sleep_threes:
                            sleep_threes.append(((i - left_connected, j), (i + right_connected, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected, j - left_connected), \
                            (i + right_connected, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(
                                ((i - left_connected, j - left_connected), (i + right_connected, j + right_connected)))
                    elif dir == 'leftdown':
                        if ((i + left_connected, j - left_connected), \
                            (i - right_connected, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(
                                ((i + left_connected, j - left_connected), (i - right_connected, j + right_connected)))
                elif list[3 - left_connected - 1] == c:  # 冲四
                    if dir == 'hor':
                        if ((i, j - left_connected - 2), (i, j + right_connected)) not in chong_fours:
                            chong_fours.append(((i, j - left_connected - 2), (i, j + right_connected)))
                    elif dir == 'ver':
                        if ((i - left_connected - 2, j), (i + right_connected, j)) not in chong_fours:
                            chong_fours.append(((i - left_connected - 2, j), (i + right_connected, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected - 2, j - left_connected - 2), \
                            (i + right_connected, j + right_connected)) not in chong_fours:
                            chong_fours.append(((i - left_connected - 2, j - left_connected - 2),
                                                (i + right_connected, j + right_connected)))
                    elif dir == 'leftdown':
                        if ((i + left_connected + 2, j - left_connected - 2), \
                            (i + right_connected, j - right_connected)) not in chong_fours:
                            chong_fours.append(((i + left_connected + 2, j - left_connected - 2),
                                                (i + right_connected, j - right_connected)))
                elif list[3 - left_connected - 1] == 3 - c:
                    pass
            elif list[3 - left_connected] == 3 - c and list[5 + right_connected] == 0:
                if list[5 + right_connected + 1] == 0:  # 眠三
                    if dir == 'hor':
                        if ((i, j - left_connected), (i, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(((i, j - left_connected), (i, j + right_connected)))
                    elif dir == 'ver':
                        if ((i - left_connected, j), (i + right_connected, j)) not in sleep_threes:
                            sleep_threes.append(((i - left_connected, j), (i + right_connected, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected, j - left_connected), \
                            (i + right_connected, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(
                                ((i - left_connected, j - left_connected), (i + right_connected, j + right_connected)))
                    elif dir == 'leftdown':
                        if ((i + left_connected, j - left_connected), \
                            (i - right_connected, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(
                                ((i + left_connected, j - left_connected), (i - right_connected, j + right_connected)))
                elif list[5 + right_connected + 1] == c:  # 冲四
                    if dir == 'hor':
                        if ((i, j - left_connected), (i, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i, j - left_connected), (i, j + right_connected + 2)))
                    elif dir == 'ver':
                        if ((i - left_connected, j), (i + right_connected + 2, j)) not in chong_fours:
                            chong_fours.append(((i - left_connected, j), (i + right_connected + 2, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected, j - left_connected), \
                            (i + right_connected + 2, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i - left_connected, j - left_connected),
                                                (i + right_connected + 2, j + right_connected + 2)))
                    elif dir == 'leftdown':
                        if ((i + left_connected, j - left_connected), \
                            (i - right_connected - 2, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i + left_connected, j - left_connected),
                                                (i - right_connected - 2, j + right_connected + 2)))
                elif list[5 + right_connected + 1] == 3 - c:
                    pass
            elif list[3 - left_connected] == 0 and list[5 + right_connected] == 0:  # 均有可能
                if (list[3 - left_connected - 1] == 0 and list[5 + right_connected + 1] == 0) \
                        or (list[3 - left_connected - 1] == 3 - c and list[5 + right_connected + 1] == 0) \
                        or (list[3 - left_connected - 1] == 0 and list[5 + right_connected + 1] == 3 - c):  # 活三
                    if dir == 'hor':
                        if ((i, j - left_connected), (i, j + right_connected)) not in live_threes:
                            live_threes.append(((i, j - left_connected), (i, j + right_connected)))
                    elif dir == 'ver':
                        if ((i - left_connected, j), (i + right_connected, j)) not in live_threes:
                            live_threes.append(((i - left_connected, j), (i + right_connected, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected, j - left_connected), \
                            (i + right_connected, j + right_connected)) not in live_threes:
                            live_threes.append(
                                ((i - left_connected, j - left_connected), (i + right_connected, j + right_connected)))
                    elif dir == 'leftdown':
                        if ((i + left_connected, j - left_connected), \
                            (i - right_connected, j + right_connected)) not in live_threes:
                            live_threes.append(
                                ((i + left_connected, j - left_connected), (i - right_connected, j + right_connected)))
                elif list[3 - left_connected - 1] == 3 - c and list[5 + right_connected + 1] == 3 - c:  # 眠三
                    if dir == 'hor':
                        if ((i, j - left_connected), (i, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(((i, j - left_connected), (i, j + right_connected)))
                    elif dir == 'ver':
                        if ((i - left_connected, j), (i + right_connected, j)) not in sleep_threes:
                            sleep_threes.append(((i - left_connected, j), (i + right_connected, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected, j - left_connected), \
                            (i + right_connected, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(
                                ((i - left_connected, j - left_connected), (i + right_connected, j + right_connected)))
                    elif dir == 'leftdown':
                        if ((i + left_connected, j - left_connected), \
                            (i - right_connected, j + right_connected)) not in sleep_threes:
                            sleep_threes.append(
                                ((i + left_connected, j - left_connected), (i - right_connected, j + right_connected)))
                elif list[3 - left_connected - 1] == c and list[5 + right_connected + 1] != c:  # 冲四
                    if dir == 'hor':
                        if ((i, j - left_connected - 2), (i, j + right_connected)) not in chong_fours:
                            chong_fours.append(((i, j - left_connected - 2), (i, j + right_connected)))
                    elif dir == 'ver':
                        if ((i - left_connected - 2, j), (i + right_connected, j)) not in chong_fours:
                            chong_fours.append(((i - left_connected - 2, j), (i + right_connected, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected - 2, j - left_connected - 2), \
                            (i + right_connected, j + right_connected)) not in chong_fours:
                            chong_fours.append(((i - left_connected - 2, j - left_connected - 2),
                                                (i + right_connected, j + right_connected)))
                    elif dir == 'leftdown':
                        if ((i + left_connected + 2, j - left_connected - 2), \
                            (i - right_connected, j + right_connected)) not in chong_fours:
                            chong_fours.append(((i + left_connected + 2, j - left_connected - 2),
                                                (i - right_connected, j + right_connected)))
                elif list[3 - left_connected - 1] != c and list[5 + right_connected + 1] == c:  # 冲四
                    if dir == 'hor':
                        if ((i, j - left_connected), (i, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i, j - left_connected), (i, j + right_connected + 2)))
                    elif dir == 'ver':
                        if ((i - left_connected, j), (i + right_connected + 2, j)) not in chong_fours:
                            chong_fours.append(((i - left_connected, j), (i + right_connected + 2, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected, j - left_connected), \
                            (i + right_connected + 2, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i - left_connected, j - left_connected),
                                                (i + right_connected + 2, j + right_connected + 2)))
                    elif dir == 'leftdown':
                        if ((i + left_connected, j - left_connected), \
                            (i - right_connected - 2, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i + left_connected, j - left_connected),
                                                (i - right_connected - 2, j + right_connected + 2)))
                elif list[3 - left_connected - 1] == c and list[5 + right_connected + 1] == c:  # 冲四
                    if dir == 'hor':
                        if ((i, j - left_connected), (i, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i, j - left_connected), (i, j + right_connected + 2)))
                        if ((i, j - left_connected - 2), (i, j + right_connected)) not in chong_fours:
                            chong_fours.append(((i, j - left_connected - 2), (i, j + right_connected)))
                    elif dir == 'ver':
                        if ((i - left_connected, j), (i + right_connected + 2, j)) not in chong_fours:
                            chong_fours.append(((i - left_connected, j), (i + right_connected + 2, j)))
                        if ((i - left_connected - 2, j), (i + right_connected, j)) not in chong_fours:
                            chong_fours.append(((i - left_connected - 2, j), (i + right_connected, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected, j - left_connected), \
                            (i + right_connected + 2, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i - left_connected, j - left_connected),
                                                (i + right_connected + 2, j + right_connected + 2)))
                        if ((i - left_connected - 2, j - left_connected - 2), \
                            (i + right_connected, j + right_connected)) not in chong_fours:
                            chong_fours.append(((i - left_connected - 2, j - left_connected - 2),
                                                (i + right_connected, j + right_connected)))
                    elif dir == 'leftdown':
                        if ((i + left_connected, j - left_connected), \
                            (i - right_connected - 2, j + right_connected + 2)) not in chong_fours:
                            chong_fours.append(((i + left_connected, j - left_connected),
                                                (i - right_connected - 2, j + right_connected + 2)))
                        if ((i + left_connected + 2, j - left_connected - 2), \
                            (i - right_connected, j + right_connected)) not in chong_fours:
                            chong_fours.append(((i + left_connected + 2, j - left_connected - 2),
                                                (i - right_connected, j + right_connected)))
        elif left_connected + right_connected == 1:  # 可能为冲四，活三，眠三，活二，眠二
            if list[3 - left_connected] == 3 - c and list[5 + right_connected] == 3 - c:
                pass
            elif list[3 - left_connected] == 0 and list[5 + right_connected] == 3 - c:
                if list[3 - left_connected - 1] == 3 - c:
                    pass
                elif list[3 - left_connected - 1] == 0:
                    if list[3 - left_connected - 2] == 0:  # 眠二
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected)) not in sleep_twos:
                                sleep_twos.append(((i, j - left_connected), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected, j)) not in sleep_twos:
                                sleep_twos.append(((i - left_connected, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected, j + right_connected)) not in sleep_twos:
                                sleep_twos.append(
                                    ((i - left_connected, j - left_connected),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected, j + right_connected)) not in sleep_twos:
                                sleep_twos.append(
                                    ((i + left_connected, j - left_connected),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == c:  # 眠三
                        if dir == 'hor':
                            if ((i, j - left_connected - 3), (i, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected - 3), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected - 3, j), (i + right_connected, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected - 3, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 3, j - left_connected - 3), \
                                (i + right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected - 3, j - left_connected - 3),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 3, j - left_connected - 3), \
                                (i - right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected + 3, j - left_connected - 3),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == 3 - c:
                        pass
                elif list[3 - left_connected - 1] == c:
                    if list[3 - left_connected - 2] == 0:  # 眠三
                        if dir == 'hor':
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == c:  # 冲四
                        if dir == 'hor':
                            if ((i, j - left_connected - 3), (i, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected - 3), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected - 3, j), (i + right_connected, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 3, j - left_connected - 3), \
                                (i + right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j - left_connected - 3),
                                                    (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 3, j - left_connected - 3), \
                                (i - right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i + left_connected + 3, j - left_connected - 3),
                                                    (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == 3 - c:
                        pass
            elif list[3 - left_connected] == 3 - c and list[5 + right_connected] == 0:
                if list[5 + right_connected + 1] == 3 - c:
                    pass
                elif list[5 + right_connected + 1] == 0:
                    if list[5 + right_connected + 2] == 0:  # 眠二
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected)) not in sleep_twos:
                                sleep_twos.append(((i, j - left_connected), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected, j)) not in sleep_twos:
                                sleep_twos.append(((i - left_connected, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected, j + right_connected)) not in sleep_twos:
                                sleep_twos.append(
                                    ((i - left_connected, j - left_connected),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected, j + right_connected)) not in sleep_twos:
                                sleep_twos.append(
                                    ((i + left_connected, j - left_connected),
                                     (i - right_connected, j + right_connected)))
                    elif list[5 + right_connected + 2] == c:  # 眠三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 3)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected), (i, j + right_connected + 3)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 3, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j), (i + right_connected + 3, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 3, j + right_connected + 3)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected, j - left_connected),
                                     (i + right_connected + 3, j + right_connected + 3)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 3, j + right_connected + 3)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected, j - left_connected),
                                     (i - right_connected - 3, j + right_connected + 3)))
                    elif list[5 + right_connected + 2] == 3 - c:
                        pass
                elif list[5 + right_connected + 1] == c:
                    if list[5 + right_connected + 2] == 0:  # 眠三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected, j - left_connected),
                                     (i + right_connected + 2, j + right_connected + 2)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected, j - left_connected),
                                     (i - right_connected - 2, j + right_connected + 2)))
                    elif list[5 + right_connected + 2] == c:  # 冲四
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected), (i, j + right_connected + 3)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 3, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected, j), (i + right_connected + 3, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 3, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i - left_connected, j - left_connected),
                                                    (i + right_connected + 3, j + right_connected + 3)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 3, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i + left_connected, j - left_connected),
                                                    (i - right_connected - 3, j + right_connected + 3)))
                    elif list[5 + right_connected + 2] == 3 - c:
                        pass
            elif list[3 - left_connected] == 0 and list[5 + right_connected] == 0:
                if list[3 - left_connected - 1] == 3 - c and list[5 + right_connected + 1] == 3 - c:
                    pass
                elif (list[3 - left_connected - 1] == 3 - c and list[5 + right_connected + 1] == 0) or \
                        (list[3 - left_connected - 1] == 0 and list[5 + right_connected + 1] == 3 - c) or \
                        (list[3 - left_connected - 1] == 0 and list[5 + right_connected + 1] == 0):  # 活二
                    if dir == 'hor':
                        if ((i, j - left_connected), (i, j + right_connected)) not in live_twos:
                            live_twos.append(((i, j - left_connected), (i, j + right_connected)))
                    elif dir == 'ver':
                        if ((i - left_connected, j), (i + right_connected, j)) not in live_twos:
                            live_twos.append(((i - left_connected, j), (i + right_connected, j)))
                    elif dir == 'lefttop':
                        if ((i - left_connected, j - left_connected), \
                            (i + right_connected, j + right_connected)) not in live_twos:
                            live_twos.append(
                                ((i - left_connected, j - left_connected),
                                 (i + right_connected, j + right_connected)))
                    elif dir == 'leftdown':
                        if ((i + left_connected, j - left_connected), \
                            (i - right_connected, j + right_connected)) not in live_twos:
                            live_twos.append(
                                ((i + left_connected, j - left_connected),
                                 (i - right_connected, j + right_connected)))
                elif list[3 - left_connected - 1] == c and list[5 + right_connected + 1] != c:
                    if list[3 - left_connected - 2] == c:  # 冲四
                        if dir == 'hor':
                            if ((i, j - left_connected - 3), (i, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected - 3), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected - 3, j), (i + right_connected, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 3, j - left_connected - 3), \
                                (i + right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j - left_connected - 3),
                                                    (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 3, j - left_connected - 3), \
                                (i - right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i + left_connected + 3, j - left_connected - 3),
                                                    (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == 3 - c:  # 眠三
                        if dir == 'hor':
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == 0:  # 活三
                        if dir == 'hor':
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in live_threes:
                                live_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in live_threes:
                                live_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in live_threes:
                                live_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in live_threes:
                                live_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                elif list[3 - left_connected - 1] != c and list[5 + right_connected + 1] == c:
                    if list[5 + right_connected + 2] == c:  # 冲四
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected), (i, j + right_connected + 3)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 3, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected, j), (i + right_connected + 3, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 3, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i - left_connected, j - left_connected),
                                                    (i + right_connected + 3, j + right_connected + 3)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 3, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i + left_connected, j - left_connected),
                                                    (i - right_connected - 3, j + right_connected + 3)))
                    elif list[5 + right_connected + 2] == 3 - c:  # 眠三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j - left_connected),
                                                     (i + right_connected + 2, j + right_connected + 2)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i + left_connected, j - left_connected),
                                                     (i - right_connected - 2, j + right_connected + 2)))
                    elif list[5 + right_connected + 2] == 0:  # 活三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in live_threes:
                                live_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i - left_connected, j - left_connected),
                                                    (i + right_connected + 2, j + right_connected + 2)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i + left_connected, j - left_connected),
                                                    (i - right_connected - 2, j + right_connected + 2)))
                elif list[3 - left_connected - 1] == c and list[5 + right_connected + 1] == c:
                    if list[3 - left_connected - 2] == 0 and list[5 + right_connected + 2] == 0:  # 两个活三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in live_threes:
                                live_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in live_threes:
                                live_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in live_threes:
                                live_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i - left_connected, j - left_connected),
                                                    (i + right_connected + 2, j + right_connected + 2)))
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in live_threes:
                                live_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i + left_connected, j - left_connected),
                                                    (i - right_connected - 2, j + right_connected + 2)))
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in live_threes:
                                live_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == 0 and list[5 + right_connected + 2] == 3 - c:  # 活三和眠三
                        if dir == 'hor':
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in live_threes:
                                live_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                        elif dir == 'ver':
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in live_threes:
                                live_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in live_threes:
                                live_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j - left_connected),
                                                     (i + right_connected + 2, j + right_connected + 2)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in live_threes:
                                live_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i + left_connected, j - left_connected),
                                                     (i - right_connected - 2, j + right_connected + 2)))
                    elif list[3 - left_connected - 2] == 3 - c and list[5 + right_connected + 2] == c:  # 活三和眠三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in live_threes:
                                live_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i - left_connected, j - left_connected),
                                                    (i + right_connected + 2, j + right_connected + 2)))
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i + left_connected, j - left_connected),
                                                    (i - right_connected - 2, j + right_connected + 2)))
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == 3 - c and list[5 + right_connected + 2] == 3 - c:  # 两个眠三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j - left_connected),
                                                     (i + right_connected + 2, j + right_connected + 2)))
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i + left_connected, j - left_connected),
                                                     (i - right_connected - 2, j + right_connected + 2)))
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == c and list[5 + right_connected + 2] == 0:  # 冲四和活三
                        if dir == 'hor':
                            if ((i, j - left_connected - 3), (i, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected - 3), (i, j + right_connected)))
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in live_threes:
                                live_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                        elif dir == 'ver':
                            if ((i - left_connected - 3, j), (i + right_connected, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j), (i + right_connected, j)))
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in live_threes:
                                live_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 3, j - left_connected - 3), \
                                (i + right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j - left_connected - 3),
                                                    (i + right_connected, j + right_connected)))
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in live_threes:
                                live_threes.append(
                                    ((i - left_connected, j - left_connected),
                                     (i + right_connected + 2, j + right_connected + 2)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 3, j - left_connected - 3), \
                                (i - right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i + left_connected + 3, j - left_connected - 3),
                                                    (i - right_connected, j + right_connected)))
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in live_threes:
                                live_threes.append(
                                    ((i + left_connected, j - left_connected),
                                     (i - right_connected - 2, j + right_connected + 2)))
                    elif list[3 - left_connected - 2] == 0 and list[5 + right_connected + 2] == c:  # 冲四和活三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected), (i, j + right_connected + 3)))
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in live_threes:
                                live_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 3, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected, j), (i + right_connected + 3, j)))
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in live_threes:
                                live_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 3, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i - left_connected, j - left_connected),
                                                    (i + right_connected + 3, j + right_connected + 3)))
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in live_threes:
                                live_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 3, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i + left_connected, j - left_connected),
                                                    (i - right_connected - 3, j + right_connected + 3)))
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in live_threes:
                                live_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == c and list[5 + right_connected + 2] == 3 - c:  # 冲四和眠三
                        if dir == 'hor':
                            if ((i, j - left_connected - 3), (i, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected - 3), (i, j + right_connected)))
                            if ((i, j - left_connected), (i, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected), (i, j + right_connected + 2)))
                        elif dir == 'ver':
                            if ((i - left_connected - 3, j), (i + right_connected, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j), (i + right_connected, j)))
                            if ((i - left_connected, j), (i + right_connected + 2, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected, j), (i + right_connected + 2, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 3, j - left_connected - 3), \
                                (i + right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j - left_connected - 3),
                                                    (i + right_connected, j + right_connected)))
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected, j - left_connected),
                                     (i + right_connected + 2, j + right_connected + 2)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 3, j - left_connected - 3), \
                                (i - right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i + left_connected + 3, j - left_connected - 3),
                                                    (i - right_connected, j + right_connected)))
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 2, j + right_connected + 2)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected, j - left_connected),
                                     (i - right_connected - 2, j + right_connected + 2)))
                    elif list[3 - left_connected - 2] == 3 - c and list[5 + right_connected + 2] == c:  # 冲四和眠三
                        if dir == 'hor':
                            if ((i, j - left_connected), (i, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected), (i, j + right_connected + 3)))
                            if ((i, j - left_connected - 2), (i, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(((i, j - left_connected - 2), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected, j), (i + right_connected + 3, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected, j), (i + right_connected + 3, j)))
                            if ((i - left_connected - 2, j), (i + right_connected, j)) not in sleep_threes:
                                sleep_threes.append(((i - left_connected - 2, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected, j - left_connected), \
                                (i + right_connected + 3, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i - left_connected, j - left_connected),
                                                    (i + right_connected + 3, j + right_connected + 3)))
                            if ((i - left_connected - 2, j - left_connected - 2), \
                                (i + right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i - left_connected - 2, j - left_connected - 2),
                                     (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected, j - left_connected), \
                                (i - right_connected - 3, j + right_connected + 3)) not in chong_fours:
                                chong_fours.append(((i + left_connected, j - left_connected),
                                                    (i - right_connected - 3, j + right_connected + 3)))
                            if ((i + left_connected + 2, j - left_connected - 2), \
                                (i - right_connected, j + right_connected)) not in sleep_threes:
                                sleep_threes.append(
                                    ((i + left_connected + 2, j - left_connected - 2),
                                     (i - right_connected, j + right_connected)))
                    elif list[3 - left_connected - 2] == c and list[5 + right_connected + 2] == c:  # 两个冲四,只用算左边
                        if dir == 'hor':
                            if ((i, j - left_connected - 3), (i, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i, j - left_connected - 3), (i, j + right_connected)))
                        elif dir == 'ver':
                            if ((i - left_connected - 3, j), (i + right_connected, j)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j), (i + right_connected, j)))
                        elif dir == 'lefttop':
                            if ((i - left_connected - 3, j - left_connected - 3), \
                                (i + right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i - left_connected - 3, j - left_connected - 3),
                                                    (i + right_connected, j + right_connected)))
                        elif dir == 'leftdown':
                            if ((i + left_connected + 3, j - left_connected - 3), \
                                (i - right_connected, j + right_connected)) not in chong_fours:
                                chong_fours.append(((i + left_connected + 3, j - left_connected - 3),
                                                    (i - right_connected, j + right_connected)))
        elif left_connected + right_connected == 0:  # 可能为眠三，活二，眠二
            if list[3] == 3 - c and list[5] == 3 - c:
                pass
            elif list[3] == 0 and list[5] == 3 - c:  # 只用检查左边即可
                if list[2] == 3 - c:
                    pass
                elif list[2] == 0:
                    if list[1] == 3 - c:
                        pass
                    elif list[1] == 0:
                        if list[0] == 0 or list[0] == 3 - c:
                            pass
                        elif list[0] == c:  # 眠二
                            if dir == 'hor':
                                if ((i, j - 4), (i, j)) not in sleep_twos:
                                    sleep_twos.append(((i, j - 4), (i, j)))
                            elif dir == 'ver':
                                if ((i - 4, j), (i, j)) not in sleep_twos:
                                    sleep_twos.append(((i - 4, j), (i, j)))
                            elif dir == 'lefttop':
                                if ((i - 4, j - 4), \
                                    (i, j)) not in sleep_twos:
                                    sleep_twos.append(((i - 4, j - 4),
                                                       (i, j)))
                            elif dir == 'leftdown':
                                if ((i + 4, j - 4), \
                                    (i, j)) not in sleep_twos:
                                    sleep_twos.append(((i + 4, j - 4),
                                                       (i, j)))
                    elif list[1] == c:
                        if list[0] != 0:
                            pass
                        else:  # 眠二
                            if dir == 'hor':
                                if ((i, j - 3), (i, j)) not in sleep_twos:
                                    sleep_twos.append(((i, j - 3), (i, j)))
                            elif dir == 'ver':
                                if ((i - 3, j), (i, j)) not in sleep_twos:
                                    sleep_twos.append(((i - 3, j), (i, j)))
                            elif dir == 'lefttop':
                                if ((i - 3, j - 3), \
                                    (i, j)) not in sleep_twos:
                                    sleep_twos.append(((i - 3, j - 3),
                                                       (i, j)))
                            elif dir == 'leftdown':
                                if ((i + 3, j - 3), \
                                    (i, j)) not in sleep_twos:
                                    sleep_twos.append(((i + 3, j - 3),
                                                       (i, j)))
                elif list[2] == c:
                    if list[1] == 0 and list[0] == 0:  # 眠二
                        if dir == 'hor':
                            if ((i, j - 2), (i, j)) not in sleep_twos:
                                sleep_twos.append(((i, j - 2), (i, j)))
                        elif dir == 'ver':
                            if ((i - 2, j), (i, j)) not in sleep_twos:
                                sleep_twos.append(((i - 2, j), (i, j)))
                        elif dir == 'lefttop':
                            if ((i - 2, j - 2), \
                                (i, j)) not in sleep_twos:
                                sleep_twos.append(((i - 2, j - 2),
                                                   (i, j)))
                        elif dir == 'leftdown':
                            if ((i + 2, j - 2), \
                                (i, j)) not in sleep_twos:
                                sleep_twos.append(((i + 2, j - 2),
                                                   (i, j)))
                    elif list[1] == 0 and list[0] == c:  # 眠三
                        if dir == 'hor':
                            if ((i, j - 4), (i, j)) not in sleep_threes:
                                sleep_threes.append(((i, j - 4), (i, j)))
                        elif dir == 'ver':
                            if ((i - 4, j), (i, j)) not in sleep_threes:
                                sleep_threes.append(((i - 4, j), (i, j)))
                        elif dir == 'lefttop':
                            if ((i - 4, j - 4), \
                                (i, j)) not in sleep_threes:
                                sleep_threes.append(((i - 4, j - 4),
                                                     (i, j)))
                        elif dir == 'leftdown':
                            if ((i + 4, j - 4), \
                                (i, j)) not in sleep_threes:
                                sleep_threes.append(((i + 4, j - 4),
                                                     (i, j)))
            elif list[3] == 0 and list[5] == 0:
                if list[0] == c and list[1] == 0 and list[2] == 0:  # 眠二
                    if dir == 'hor':
                        if ((i, j - 4), (i, j)) not in sleep_twos:
                            sleep_twos.append(((i, j - 4), (i, j)))
                    elif dir == 'ver':
                        if ((i - 4, j), (i, j)) not in sleep_twos:
                            sleep_twos.append(((i - 4, j), (i, j)))
                    elif dir == 'lefttop':
                        if ((i - 4, j - 4), \
                            (i, j)) not in sleep_twos:
                            sleep_twos.append(((i - 4, j - 4),
                                               (i, j)))
                    elif dir == 'leftdown':
                        if ((i + 4, j - 4), \
                            (i, j)) not in sleep_twos:
                            sleep_twos.append(((i + 4, j - 4),
                                               (i, j)))
                elif list[0] == 0 and list[1] == c and list[2] == 0:  # 活二
                    if dir == 'hor':
                        if ((i, j - 3), (i, j)) not in live_twos:
                            live_twos.append(((i, j - 3), (i, j)))
                    elif dir == 'ver':
                        if ((i - 3, j), (i, j)) not in live_twos:
                            live_twos.append(((i - 3, j), (i, j)))
                    elif dir == 'lefttop':
                        if ((i - 3, j - 3), \
                            (i, j)) not in live_twos:
                            live_twos.append(((i - 3, j - 3),
                                              (i, j)))
                    elif dir == 'leftdown':
                        if ((i + 3, j - 3), \
                            (i, j)) not in live_twos:
                            live_twos.append(((i + 3, j - 3),
                                              (i, j)))
                elif list[0] == 0 and list[1] == 0 and list[2] == c:  # 活二
                    if dir == 'hor':
                        if ((i, j - 2), (i, j)) not in live_twos:
                            live_twos.append(((i, j - 2), (i, j)))
                    elif dir == 'ver':
                        if ((i - 2, j), (i, j)) not in live_twos:
                            live_twos.append(((i - 2, j), (i, j)))
                    elif dir == 'lefttop':
                        if ((i - 2, j - 2), \
                            (i, j)) not in live_twos:
                            live_twos.append(((i - 2, j - 2),
                                              (i, j)))
                    elif dir == 'leftdown':
                        if ((i + 2, j - 2), \
                            (i, j)) not in live_twos:
                            live_twos.append(((i + 2, j - 2),
                                              (i, j)))
                elif list[0] == c and list[1] == 0 and list[2] == c:  # 眠三
                    if dir == 'hor':
                        if ((i, j - 4), (i, j)) not in sleep_threes:
                            sleep_threes.append(((i, j - 4), (i, j)))
                    elif dir == 'ver':
                        if ((i - 4, j), (i, j)) not in sleep_threes:
                            sleep_threes.append(((i - 4, j), (i, j)))
                    elif dir == 'lefttop':
                        if ((i - 4, j - 4), \
                            (i, j)) not in sleep_threes:
                            sleep_threes.append(((i - 4, j - 4),
                                                 (i, j)))
                    elif dir == 'leftdown':
                        if ((i + 4, j - 4), \
                            (i, j)) not in sleep_threes:
                            sleep_threes.append(((i + 4, j - 4),
                                                 (i, j)))
                elif list[0] == 3-c:
                    if list[1]==0 and list[2]==c and list[6]==3-c:#眠二
                        if dir == 'hor':
                            if ((i, j - 2), (i, j)) not in sleep_twos:
                                sleep_twos.append(((i, j - 2), (i, j)))
                        elif dir == 'ver':
                            if ((i - 2, j), (i, j)) not in sleep_twos:
                                sleep_twos.append(((i - 2, j), (i, j)))
                        elif dir == 'lefttop':
                            if ((i - 2, j - 2), \
                                (i, j)) not in sleep_twos:
                                sleep_twos.append(((i - 2, j - 2),
                                                   (i, j)))
                        elif dir == 'leftdown':
                            if ((i + 2, j - 2), \
                                (i, j)) not in sleep_twos:
                                sleep_twos.append(((i + 2, j - 2),
                                                   (i, j)))
                    elif list[1]==0 and list[2]==c and list[6]==0:#活二
                        if dir == 'hor':
                            if ((i, j - 2), (i, j)) not in live_twos:
                                live_twos.append(((i, j - 2), (i, j)))
                        elif dir == 'ver':
                            if ((i - 2, j), (i, j)) not in live_twos:
                                live_twos.append(((i - 2, j), (i, j)))
                        elif dir == 'lefttop':
                            if ((i - 2, j - 2),\
                                (i, j)) not in live_twos:
                                live_twos.append(((i - 2, j - 2),
                                                  (i, j)))
                        elif dir == 'leftdown':
                            if ((i + 2, j - 2),\
                                (i, j)) not in live_twos:
                                live_twos.append(((i + 2, j - 2),
                                                  (i, j)))
                    elif list[1]==c and list[2]==0:#眠二
                        if dir == 'hor':
                            if ((i, j - 3), (i, j)) not in sleep_twos:
                                sleep_twos.append(((i, j - 3), (i, j)))
                        elif dir == 'ver':
                            if ((i - 3, j), (i, j)) not in sleep_twos:
                                sleep_twos.append(((i - 3, j), (i, j)))
                        elif dir == 'lefttop':
                            if ((i - 3, j - 3),\
                                (i, j)) not in sleep_twos:
                                sleep_twos.append(((i - 3, j - 3),
                                                   (i, j)))
                        elif dir == 'leftdown':
                            if ((i + 3, j - 3),\
                                (i, j)) not in sleep_twos:
                                sleep_twos.append(((i + 3, j - 3),
                                                   (i, j)))
                    else:
                        pass

                elif list[1]==3-c and list[2]==c:
                    if list[6]==0:#眠二
                        if dir == 'hor':
                            if ((i, j - 2), (i, j)) not in sleep_twos:
                                sleep_twos.append(((i, j - 2), (i, j)))
                        elif dir == 'ver':
                            if ((i - 2, j), (i, j)) not in sleep_twos:
                                sleep_twos.append(((i - 2, j), (i, j)))
                        elif dir == 'lefttop':
                            if ((i - 2, j - 2), \
                                (i, j)) not in sleep_twos:
                                sleep_twos.append(((i - 2, j - 2),
                                                   (i, j)))
                        elif dir == 'leftdown':
                            if ((i + 2, j - 2), \
                                (i, j)) not in sleep_twos:
                                sleep_twos.append(((i + 2, j - 2),
                                                   (i, j)))
                    else:
                        pass
                else:
                    pass

    for i in range(root.shape[0]):
        for j in range(root.shape[1]):
            if root[i][j] != c:
                pass
            else:
                points+=pos_point[i][j]
                hor = hor_list(root, (i, j))
                ver = ver_list(root, (i, j))
                lefttop = lefttop_rightdown_list(root, (i, j))
                leftdown = leftdown_righttop_list(root, (i, j))
                part_point((i, j), 'hor', hor)
                part_point((i, j), 'ver', ver)
                part_point((i, j), 'lefttop', lefttop)
                part_point((i, j), 'leftdown', leftdown)

    five_nums = 0
    if fives:
        five_nums = 1
    live_four_nums = len(live_fours)
    chong_four_nums = len(chong_fours)
    live_three_nums = len(live_threes)
    sleep_three_nums = len(sleep_threes)
    live_two_nums = len(live_twos)
    sleep_two_nums = len(sleep_twos)
    if color=='black':
        points+=2000000*five_nums+100000*live_four_nums+10000*chong_four_nums+8000*live_three_nums+3000*sleep_three_nums+2500*live_two_nums+1000*sleep_two_nums
    elif color=='white':
        points+=5000000*five_nums+1000000*live_four_nums+200000*chong_four_nums+50000*live_three_nums+3000*sleep_three_nums+3000*live_two_nums+1000*sleep_two_nums

    return points

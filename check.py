#检查是否达成游戏结束的条件

def check(chess_pos,ai):

    width=ai.chessboard_lattice_width
    width_all=ai.chessboard_lattice_width*ai.chessboard_num_of_lattice_per_line

    def check_hor(chess_pos):
        """检查是否有水平的五个子连成一条线"""

        for i in range(len(chess_pos)):
            left = max(width/2, chess_pos[i][0] - 4 * width)
            right = min(width_all-width/2, chess_pos[i][0] + 4 * width)
            x = left
            y = chess_pos[i][1]
            for i in range(int((right - left) / width - 3)):
                count = 0
                x_ = x
                for i in range(5):
                    if (x_, y) in chess_pos:
                        count += 1
                    if count == 5:
                        return True
                    x_ += width
                x += width

    def check_ver(chess_pos):
        """检查是否有竖直的五个子连成一条线"""

        for i in range(len(chess_pos)):
            up = max(width/2, chess_pos[i][1] - 4 * width)
            down = min(width_all-width/2, chess_pos[i][1] + 4 * width)
            x = chess_pos[i][0]
            y = up
            for i in range(int((down - up) / width - 3)):
                count = 0
                y_ = y
                for i in range(5):
                    if (x, y_) in chess_pos:
                        count += 1
                    if count == 5:
                        return True
                    y_ += width
                y += width

        return False

    def check_lefttop_rightdown(chess_pos):
        """检查是否有从左上到右下的五个子连成一条线"""

        for i in range(len(chess_pos)):
            left = max(width/2, chess_pos[i][0] - 4 * width)
            right = min(width_all-width/2, chess_pos[i][0] + 4 * width)
            up = max(width/2, chess_pos[i][1] - 4 * width)
            down = min(width_all-width/2, chess_pos[i][1] + 4 * width)
            lefttop_dis = int(min(chess_pos[i][0] - left, chess_pos[i][1] - up) // width)
            rightdown_dis = int(min(right - chess_pos[i][0], down - chess_pos[i][1]) // width)
            x = chess_pos[i][0] - lefttop_dis * width
            y = chess_pos[i][1] - lefttop_dis * width
            if lefttop_dis + rightdown_dis < 4:
                return False
            else:
                for i in range(int(lefttop_dis + rightdown_dis - 3)):
                    count = 0
                    x_ = x
                    y_ = y
                    for i in range(5):
                        if (x_, y_) in chess_pos:
                            count += 1
                        if count == 5:
                            return True
                        x_ += width
                        y_ += width
                    x += width
                    y += width
        return False

    def check_leftdown_righttop(chess_pos):
        """检查是否有从左下到右上的五个子连成一条线"""

        for i in range(len(chess_pos)):
            left = max(width/2, chess_pos[i][0] - 4 * width)
            right = min(width_all-width/2, chess_pos[i][0] + 4 * width)
            up = max(width/2, chess_pos[i][1] - 4 * width)
            down = min(width_all-width/2, chess_pos[i][1] + 4 * width)
            leftdown_dis = int(min(chess_pos[i][0] - left, down - chess_pos[i][1]) // width)
            righttop_dis = int(min(right - chess_pos[i][0], chess_pos[i][1] - up) // width)
            x = chess_pos[i][0] - leftdown_dis * width
            y = chess_pos[i][1] + leftdown_dis * width
            if leftdown_dis + righttop_dis < 4:
                return False
            else:
                for i in range(int(leftdown_dis + righttop_dis - 3)):
                    count = 0
                    x_ = x
                    y_ = y
                    for i in range(5):
                        if (x_, y_) in chess_pos:
                            count += 1
                        if count == 5:
                            return True
                        x_ += width
                        y_ -= width
                    x += width
                    y -= width

        return False

    if check_hor(chess_pos) \
            or check_ver(chess_pos) \
            or check_lefttop_rightdown(chess_pos) \
            or check_leftdown_righttop(chess_pos):
        return True
    else:
        return False



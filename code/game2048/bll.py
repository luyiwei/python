"""
2048 游戏核心算法
"""
from mode import DirectionModel
from mode import Location
import random
class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [
            [2, 0, 0, 2],
            [4, 4, 2, 2],
            [2, 4, 0, 4],
            [0, 0, 2, 2]
        ]
    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for i in range(-1,-len(self.__list_merge)-1,-1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)


    def __merge(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i+1]:
                self.__list_merge[i] *=2
                del self.__list_merge[i+1]
                self.__list_merge.append(0)


    def __move_left(self):
        for line in self.__map:
            self.__list_merge = line
            self.__merge()

    def __move_right(self):
        for line in self.__map:
            self.__list_merge = line[::-1]
            self.__merge()
            print(self.__list_merge)
            line[::-1] = self.__list_merge

    def __move_up(self):
        self.__squre_matrix_transpose()
        self.move_left()
        self.__squre_matrix_transpose()

    def __move_down(self):
        self.__squre_matrix_transpose()
        self.__move_right()
        self.__squre_matrix_transpose()
    def __squre_matrix_transpose(self):
        for c in range(1,len(self.__map)):
            for r in range(c,len(self.__map)):
                self.__map[r][c - 1],self.__map[c - 1][r] = self.__map[c - 1][r],self.__map[r][c - 1]

    def move(self,dir):
        if dir == DirectionModel.UP:
            self.__move_up()
        elif dir == DirectionModel.DOWN:
            self.__move_down()
        elif dir == DirectionModel.LEFT:
            self.__move_left()
        elif dir == DirectionModel.RIGHT:
            self.__move_right()
    # def genreate_new_number(self):
    #     list_empty_location = []
    #     for r in range(len(self.__map)):
    #         for c in range(len(self.__map[r])):
    #             if self.__map[r][c] == 0:
    #                 list_empty_location.append((r,c))
    #     loc = random.choice(list_empty_location)
    #     if random.randint(1,10) == 1:
    #         self.__map[loc[0]][loc[1]] = 4
    #     else:
    #         self.__map[loc[0]][loc[1]] = 2
    def genreate_new_number(self):
        list_empty_location = self.__get_empty_location()
        if len(list_empty_location) == 0:
            return
        loc = random.choice(list_empty_location)
        if random.randint(1,10) == 1:
            self.__map[loc.r_index][loc.c_index]= 4
        else:
            self.__map[loc.r_index][loc.c_index] = 2

    def __get_empty_location(self):
        list_empty_location = []
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    list_empty_location.append(Location(r,c))
        return list_empty_location

    def is_game_over(self):
        if len(self.__get_empty_location()) > 0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r]) -1):
                if self.__map[r][c] == self.__map[r][c+1]:
                    return False

        for c in range(4):
            for r in range(3):
                if self.__map[r][c] == self.__map[r+1][c]:
                    return False
        return True
if __name__ == "__main__":
    controller = GameCoreController()
    # controller.move_left()
    # print(controller.map)
    controller.move(DirectionModel.LEFT)
    print(controller.map)

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
# import double_list_helper
# re = double_list_helper.DoubleListHelper.get_elements(list01,double_list_helper.Vector2(1, 0),double_list_helper.Vector2.left(), 3)

# from double_list_helper import DoubleListHelper
# from double_list_helper import  Vector2
# re = DoubleListHelper.get_elements(list01,Vector2(1, 0),Vector2.left(), 3)

from  double_list_helper import *
re = DoubleListHelper.get_elements(list01,Vector2(1, 0),Vector2.left(), 3)
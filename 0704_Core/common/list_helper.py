"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素,生成器类型.
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, func_condition):
        """
            通用的查找某个条件的单个元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件,函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item
    @staticmethod
    def find_sum(list_target,func_condition):
        """

        :param list_target:
        :param func_condition:
        :return:
        """
        sum_value = 0
        for item in list_target:
            sum_value += func_condition(item)
        return sum_value
    @staticmethod
    def find_all(list_target,func_condition):
        """

        :param list_target:
        :param func_condition:
        :return:
        """
        list01 = []
        for item in list_target:
            list01.append(func_condition(item))
        return list01
    @staticmethod
    def find_select(list_target,func_condition):
        for item in list_target:
            yield func_condition(item)

    @staticmethod
    def get_max(list_target,func_condition):
        max_value = list_target[0]
        for i in range(1,len(list_target)):
            # if max_value.atk < list_target[i].atk:
            if func_condition(max_value) < func_condition(list_target[i]):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def get_up(list_target,func_condition):
        for r in range(len(list_target) - 1):
            for c in range(r+1,len(list_target)):
                if func_condition(list_target[r]) > func_condition(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]

    @staticmethod
    def get_min(list_target,func_condition):
        min_value = list_target[0]
        for item in range(1,len(list_target)):
            if func_condition(min_value) > func_condition(list_target[item]):
                min_value = list_target[item]
        return min_value

    @staticmethod
    def order_by_descending(list_target,func_condition):
        for r in range(len(list_target) -1 ):
            for c in range(r+1,len(list_target)):
                if func_condition(list_target[r]) < func_condition(list_target[c]):
                    list_target[r],list_target[c] = list_target[c],list_target[r]

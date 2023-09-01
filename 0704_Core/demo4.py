import time

def get_week(year,month,day):
    """

    :param year: 年
    :param month: 月
    :param day: 天
    :return: 星期几
    """
    tuple_time = time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
    # print(tuple_time[6])
    dict_weeks = {
        0:"一",
        1: "二",
        2: "三",
        3: "四",
        4: "五",
        5: "六",
        6: "日",
    }
    return  dict_weeks[tuple_time[6]]
re = get_week(2023,7,10)
print(re)

def life_days(year,month,day):
    """

    :param year:
    :param month:
    :param day:
    :return: 活得天数
    """
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    life_second = time.time() - time.mktime(tuple_time)
    return int(life_second /60 /60 //24)
print(life_days(1990,2,16))
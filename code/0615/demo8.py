dict_commodity_info = {
    101: {"name": "aa","price": 10000},
    102: {"name": "bb","price": 10000},
    103: {"name": "cc","price": 8000},
    104: {"name": "dd","price": 9000},
    105: {"name": "ee","price": 8000},
    106: {"name": "ff","price": 10000}
}
list_order = []


def gou_wu():
    """
    :param
    :return:
    """
    while True:
        item = input("1键购买,2键结算。")
        if item == "1":
            for key, value in dict_commodity_info.items():
                print("编号:%d,名称:%s,单价:%d。" % (key, value["name"], value["price"]))
            while True:
                cid = int(input("输入商品编号:"))
                if cid in dict_commodity_info:
                    break
                else:
                    print("商品不存在")
            count = int(input("数量:"))
            list_order.append({"cid": cid, "count": count})
            print("添加购物车成功.")
        elif item == "2":
            zong_jia = 0
            for item in list_order:
                shang_pin = dict_commodity_info[item["cid"]]
                print("商品:%s,单价:%d,数量:%d." % (shang_pin["name"], shang_pin["price"], item["count"]))
                zong_jia += shang_pin['price'] * item["count"]
            while True:
                qian = float(input("总价%d,请输入金额" % (zong_jia)))
                if qian >= zong_jia:
                    print("够物成功,找回:%d元。" % (qian - zong_jia))
                    list_order.clear()
                    break
                else:
                    print("金额不足")


gou_wu()

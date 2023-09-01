def attack_repeat(r_count,c_count,char):
    """
    :param count: 次数

    """
    for r in range(r_count):
        for c in range(c_count):
            print(char,end =" ")
        print()

attack_repeat(3,2,"#")
class SkillImpactEffect:
    """
    技能影响效果
    """
    def impact(self):
        raise NotImplementedError()
class DamageEffect(SkillImpactEffect):
    """
    伤害生命效果
    """
    def __init__(self,value):
        self.value = value
    def impact(self):
        print("掉血%d" % self.value)
class LowerDeffnessEffect(SkillImpactEffect):
    """
    降低防御
    """
    def __init__(self,value,time):
        self.value = value
        self.time = time
    def impact(self):
        print("掉血%d,持续时间%d秒" % (self.value,self.time))

class DizzinessEffect(SkillImpactEffect):
    """
    眩晕
    """
    def __init__(self,time):
        self.time = time
    def impact(self):
        print("眩晕%d秒" % (self.time))

class SkillDeployer:
    """
    技能释放器
    """
    # 加载配置文件 {技能名称:[效果1，效果2..],...}
    #创建效果对象
    #生成技能(执行效果)
    def __init__(self,name):
        self.name = name
        # 加载配置文件 {技能名称:[效果1，效果2..],...}
        self.__dict_skill_config = self.__load_config_file()
        # 创建效果对象
        self.__effect_objects = self.__create_effect_objects()
    def __load_config_file(self):
        #加载配置文件.....
        return {
            "天蚕": ["DamageEffect(200)","LowerDeffnessEffect(-10,5)","DizzinessEffect(6)"],
            "天蚕aa": ["DamageEffect(100)", "LowerDeffnessEffect(-1,4)", "DizzinessEffect(3)"],
        }
    def __create_effect_objects(self):
        #根据name创建相应的技能对象
        #天蚕--->[技能1，技能2]
        list_effect_name = self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            effect_object = eval(item)
            list_effect_object.append(effect_object)
        return list_effect_object

    #生产技能(执行效果)
    def generate_skill(self):
        print(self.name,"技能释放了")
        for item in self.__effect_objects:
            item.impact()


xl = SkillDeployer("天蚕")
xl.generate_skill()

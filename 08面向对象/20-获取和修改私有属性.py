#父类Master
class Master(object):
    def __init__(self):
        self.kongfu="白马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")

#父类School
class School(object):
    def __init__(self):
        self.kongfu="黑马煎饼果子配方"

    def makeCake(self):
        print(f"使用{self.kongfu}制作果子")


class Prentice(Master,School):
    def __init__(self):
        self.kongfu="独创煎饼果子配方"
        #私有属性
        self.__money=20000000000

    #定义私有方法
    def __infoPrint(self):
        print("私有方法")

    #获取私有属性
    def getMoney(self):
        return self.__money

    #修改私有属性
    def setMoney(self):
        self.__money=10


    def makeCake(self):
        self.__init__()
        print(f"使用{self.kongfu}制作果子")


    #调用父类Master的同名的方法和属性
    def makeMasterCake(self):
        Master.__init__(self)
        Master.makeCake(self)
    #调用父类School的同名的方法和属性
    def makeSchoolCake(self):
        School.__init__(self)
        School.makeCake(self)


#创建孙类
class Sun(Prentice):
    pass

#创建对象xiaoqiu
xiaoqiu=Sun()

#获取私有属性
print(xiaoqiu.getMoney())

#修改私有属性
xiaoqiu.setMoney()

#再次打印私有属性值，查看是否修改成功
print(xiaoqiu.getMoney())





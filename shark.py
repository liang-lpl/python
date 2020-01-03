'''
import random
class Fish:
    def __init__(self):
        self.x = random.randint(0,20)
        self.y = random.randint(0,20)
    def move(self):
        self.x -= 1
        print('我现在的位置是',self.x,self.y)
class Goldfish(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('我非常的饿，我要吃吃吃!!!^_^')
            self.hungry = False
        else:
            print('我已经吃饱了，我要睡觉了！')
            self.hungry = True



class CountList:
    
    def __init__(self,*args):    #*args有外部传进多个数，用来创建列表
        #创建列表
        self.values = [x for x in args]
        #创建字典，存放列表中元素被访问的次数，列表的下标为键，值默认为0
        self.count = {}.fromkeys(range(len(self.values)),0)

    #定义一个不可变容器
    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        #元素被访问后，值加1
        self.count[key] += 1
        return self.values[key]
'''
import urllib.request
req = urllib.request.Request('http://placekitten.com/g/300/500')
response = urllib.request.urlopen(req)
cat_img = response.read()
with open ('E:\\python\\photo\\cat_300_500.jpg','wb') as f:
    f.write(cat_img)

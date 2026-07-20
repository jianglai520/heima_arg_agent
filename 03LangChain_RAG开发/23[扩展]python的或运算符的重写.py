# MySequence 就是把多个零散的对象组织成一个有序队列，然后可以统一操作它们。
class Test(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Test({self.name})"    # 定义打印时的显示格式

    def __or__(self, other):
        return MySequence(self ,other)   # __or__方法返回的是MySequence类对象



class MySequence(object):
    def __init__(self, *args):   # *args表示接受任意数量的参数--可变参数
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)   # 把传入的参数都加入列表list中

    def __or__(self, other):
        self.sequence.append(other)
        return self    # 返回自己，实现链式操作

    def run(self):
        for i in self.sequence:
            print(i)


if __name__ == '__main__':
    a = Test('a')
    b = Test('b')
    c = Test('c')
    # print(a == b)

    d = a | b | c  # a.__or__(b)
    d.run()
    print(type(d))


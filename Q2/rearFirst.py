#coding=utf-8

class rearFirst:
    def __init__(self):  # 定義初始值等於空的List。
        self.items = []

    def isEmpty(self):  # 定義isEmpty函數，用以查看List是否是空的，並回傳結果，達成Queue的isEmpty效果。
        if len(self.items) == 0:
            return True
        else:
            return False

    def enqueue(self, value):  # 定義enqueue函數，用以加入item至List最尾端，達成Queue的enqueue效果。
        self.items.insert(0,value)

    def dequeue(self):
        return self.items.pop()  # 定義dequeue函數，用以pop出List的第一個item，達成Queue的dequeue效果。

    def size(self):  # 定義siez函數，用以查看List的長度，並回傳數值，達成Queue的size效果。
        return len(self.items)
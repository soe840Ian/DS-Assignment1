#coding=utf-8

class rearLast: #建立類別rearLast。

    def __init__(self): #定義初始值等於空的List。
        self.items = []

    def isEmpty(self): #定義isEmpty函數，用以查看List是否是空的，並回傳結果，達成Queue的isEmpty效果。
        if len(self.items) == 0 :
            return True
        else :
            return False

    def enqueue(self, value): #定義enqueue函數，用以加入item至List最尾端，達成Queue的enqueue效果。
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0) #定義dequeue函數，用以pop出List的第一個item，達成Queue的dequeue效果。

    def size(self): #定義siez函數，用以查看List的長度，並回傳數值，達成Queue的size效果。
        return len(self.items)



def test() :
    List = rearLast()
    List.enqueue(5)
    List.enqueue(2)
    List.enqueue("A")
    print (List.isEmpty())
    print (List.size())
    List.dequeue()
    print (List.size())
    List.dequeue()
    print (List.size())
    print (List.isEmpty())
    List.dequeue()
    print (List.isEmpty())

def main() :
    test()
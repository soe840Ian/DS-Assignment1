#coding=utf-8

class Node: #定義類別Node。
    def __init__(self,initdata): #定義初始值self.data = initdata，self.next = None。
        self.data = initdata
        self.next = None

    def getData(self): #定義getData函數，回傳self.data。
        return self.data

    def getNext(self): #定義getNext函數，回傳self.next。
        return self.next

    def setData(self,newdata): #setData函數，將self.data指派為newdata。
        self.data = newdata

    def setNext(self,newnext): #定義setNext函數，將selfnext指派為newnext。
        self.next = newnext


class UnorderedList: #定義類別UnorderedList。
    def __init__(self): #定義初始值self.head = None。
        self.head = None

    def isEmpty(self): #定義isEmpty函數，回傳True or False 。
        if self.head == None :
            return self.head == None
        else :
            return self.head == None

    def add(self, item): #定義add函數，指派temp為Node(item)，設定temp.next為self.head，指派self.head為temp。藉此達成插入item在最前端的效果。
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self): #定義size函數，指派current為self.head、count為0。
        current = self.head
        count = 0
        while current != None: #當current不是空的時，count加一，current指派為current.getNext()，重複至getNext為None，藉此達成數數效果。
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item): #定義search函數，指派current為self.head、found為False。
        current = self.head
        found = False
        while current != None and not found: #當current不是空的且found為False，若self.data等於輸入的item，則指派found為True，中斷迴圈。
            if current.getData() == item:     #否則指派current為current.getNext()，直到current等於輸入item或None。
                found = True
            else:
                current = current.getNext()
        return found #回傳found的數值。


    def remove(self, item): #定義remove函數，用以移除指定item。
        current = self.head
        previous = None
        found = False #指派found為Fals，用以操作迴圈e。
        while not found: #當found為False
            if current.getData() == item: #若self.data等於輸入的item，則指派found為True，中斷迴圈。
                found = True
            else:                         #否則指派previous為current、current為current.getNext()，用以繼續尋找item。
                previous = current
                current = current.getNext()

        if previous == None: #若previous等於None，則指派self.head為current.getNext()。
            self.head = current.getNext()
        else:                #否則設定previous的self.next為current的self.next。
            previous.setNext(current.getNext())

    def append(self,item): #定義append函數，用以將item插入至最後端。
        current = self.head
        previous = None
        while current != None: #當current不等於None。
            previous = current
            current = current.getNext() #指派current為current的self.next，持續替換直至self.next為None，便是找到最尾端。
        temp = Node(item)
        if previous == None:
            self.head = temp
        else:
            previous.setNext(temp)

    def index(self,item) : #定義index函數，用以尋找item的位置。
        current = self.head
        found = False #指派found為False，用以操作迴圈。
        index = 0 #指派index為0，用以尋找位置。
        while current != None and not found: #當current不是空的且found為false:
            if current.getData() == item: #若current的self.data等於輸入的item(找到item):
                found = True #指派found為True，中斷迴圈。
            else:
                current = current.getNext() #指派current為current的self.next。
                index += 1 #指派index等於index+1。
        if found == True :
            return index
        else : #若是沒有找到item:
            return "item doesn't exist" #顯示item doesn't exist。

    def insert(self,pos,item) : #定義insert函數，用以插入item至指定位置。
        local = 0 #指派local為0，用以尋找插入點。
        temp = Node(item)
        previous = None
        current = self.head
        while local < pos and current != None : #當local小於輸入的pos且current不是空的 :
            local +=1 #local加一，產生迴圈效果。
            previous = current
            current = current.getNext()
        if current == None : #若current是空的，直接插入item。
            temp.setNext(self.head)
            self.head = temp
        else :
            temp.setNext(current)
            previous.setNext(temp)

    def pop(self, pos = -1)  : # 定義pop函數，用以彈出、回傳指定位置或最後一個item。
        local = 1 # 指派local為1，用以尋找指定位置。
        previous = None
        current = self.head

        while local < pos + 1 : #若local小於指定位置pos+1:
            previous = current
            current = current.getNext()
            local += 1

        if pos != 0 and previous == None :  #若pos不等於0且previous等於None(結合上下程式即為pos欄位是空的狀況):
            temp = 0 #指派temp為0，用以尋找(self.size)-1的數字，以便消去item。
            len = self.size() #指派len為self.size
            while current != None and temp < len - 1 :
                previous = current
                current = current.getNext()
                temp += 1
            previous.setNext(current.getNext()) #設定previous的next為current的next(用於將最後一個item消去)。

        elif pos == 0 and previous == None : #若pos等於0且previous等於None(結合上面則為pos欄位為0的狀況):
            self.head = current.getNext()
            return current.getData()

        else:
            previous.setNext(current.getNext())
            return current.getData()




sample = UnorderedList()
print (sample.isEmpty())
sample.add(5)
sample.append(500)
sample.append(5000)
sample.insert(1,50)
print (sample.size())
print (sample.search(1000))
print (sample.search(5000))
sample.remove(5000)
print (sample.search(5000))

print (sample.index(5))
print (sample.index(50))
print (sample.index(500))
sample.pop(1)
print (sample.index(5))
print (sample.index(50))
print (sample.index(500))
sample.pop()
print (sample.index(5))
print (sample.index(500))
print (sample.isEmpty())









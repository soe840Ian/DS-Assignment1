#coding=utf-8

class Stack: # 定義類別Stack
    def __init__(self): #定義初始值=空的List
        self.items = []

    def isEmpty(self): #定義isEmpty函數，用以查看List是否是空的。
        return self.items == []

    def push(self, item): #定義push函數，將item插入至List的最後。
        self.items.append(item)

    def pop(self): #定義pop函數，將List的最後一個item彈出且回傳。
        return self.items.pop()

    def peek(self): #定義peek函數，回傳List的最後一個item。
        return self.items[len(self.items) - 1]

    def size(self): #定義size函數，回傳List的長度。
        return len(self.items)


def parChecker(HTMLString): #定義parChecker函數，用以查看括號是否對稱。
    opList = [] #指派opList為空的List。
    otherList = [] #指派otherList為空的List。
    CutList = [] #指派CutList為空的List。
    tokenList = HTMLString #指派tokenList為HTMLString。

    for token in tokenList: #將英數字、括號、其餘不及備載之各項分類，過濾tokenList中的item。
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789" or token in "abcdefghijklmnopqrstuvwxyz": #若token是大、小寫英文及數字則插入至CutList。
            CutList.append(token)
        elif token == '<': #若token是'<'則插入至opList的最尾端。
            opList.append(token)
        elif token == '>': #若token是'>'則插入至opList的最尾端。
            opList.append(token)
        else: #若token以上皆非，則插入至otherList。
            otherList.append(token)
    print(tokenList) #顯示tokenList。
    print(opList) #opList。

    s = Stack() #指派s為Stack()。
    balanced = True #指派balanced為Trur。
    index = 0 #指派index為0。
    while index < len(opList) and balanced : #當index小於opList的長度且balanced為True時:
        symbol = opList[index] #指派symbol為opList第index項item。
        if symbol == "<": #若symbol是'<'，則push進s。
            s.push(symbol)
        else:
            if s.isEmpty(): #若s是空的，則指派balanced為False。
                balanced = False
            else: #因opList過濾過，故此處應只有在symbol='>'發生，發生時pop出s的item。。
                s.pop()

        index = index + 1 #指派index = index + 1，藉此達成循環效果。

    if balanced and s.isEmpty(): #若balanced為True且s為空的時候:
        return True #回傳True，html括號正確。
    else:
        return False #回傳False，html括號錯誤。


print(parChecker("<html>")) #顯示判斷<html>的結果。
print(parChecker("<<body>          </body>")) #顯示判斷<<body>          </body>的結果
print(parChecker("<html>    <head>       <title>          Example       </title>    </head>    <body>       <h1>Hello, world</h1>    </body> </html>"))
#顯示判斷<html>    <head>       <title>          Example       </title>    </head>    <body>       <h1>Hello, world</h1>    </body> </html>的結果。
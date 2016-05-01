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

def infixToPrefix(infixexpr): #定義infixToPrefix函數，用以將輸入的值infixexpr轉換至Prefix。
    prec = {} #指派prec是一個空的str。
    prec["*"] = 3 #指派符號的權重，以下四個相同。
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1
    opStack = Stack() #指派opStack為一個Stack
    prefixList = [] #指派prefixList為一個空的List。
    tempList = [] #指派tempList為一個空的List。
    tokenList = infixexpr.split() #指派tokenList等於infixexpr.split()，infixexpr.split()用以將infixexpr的每個字符分開。

    for token in tokenList: #將tokenList中的item依序insert至tempList的0位置，達成item的順序顛倒。
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            tempList.insert(0,token)

        elif token == '(':
            tempList.insert(0,token)

        elif token == ')':
            tempList.insert(0,token)

        elif token == '+':
            tempList.insert(0,token)

        elif token == '-':
            tempList.insert(0,token)

        elif token == '*':
            tempList.insert(0,token)

        elif token == '/':
            tempList.insert(0,token)

    tokenList = tempList #指派tokenList等於tempList。

    for token in tokenList: #將infix轉換至Prefix。
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789": #若token(item)為大寫英文或數字，則insert至prefixList的0位置。
            prefixList.insert(0,token)
        elif token == ')': #若token(item)為後括號')'，則push進opStack。
            opStack.push(token)
        elif token == '(': #若token(item)為前括號'('，則topToken的值指派為opStack所pop的item。
            topToken = opStack.pop()
            while topToken != ')': #若topToken(item)的值不等於後括號')'，則insert至prefixList的0位置，再將topToken的值指派為opStack所pop的item，
                prefixList.insert(0,topToken) #重複進行直到topToken等於後括號')'。
                topToken = opStack.pop()
        else: #若上述情況皆不符合，則在opStack不是空的情況且opStack所peek出的item的權重值大於token的權重值的情況下，將opStack所pop出的item插入至prefixList的0位置。
            if (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] > prec[token]):
                prefixList.insert(0,opStack.pop())
            opStack.push(token) #若不符合上述情況則將token(item)push進opStack。

    while not opStack.isEmpty(): #若opStack不是空的，則將opStack所pop出的item插入至prefixList的0位置，直到opStack是空的。
        prefixList.insert(0,opStack.pop())
    return " ".join(prefixList) #回傳prefixList，並在prefixList的每個item間回傳" "，達成空格效果。


print(infixToPrefix("A * B + C * D")) #顯示A * B + C * D的轉換結果
print(infixToPrefix("( A + B ) * C - ( D - E ) * ( F + G )")) #顯示( A + B ) * C - ( D - E ) * ( F + G )的轉換結果
print(infixToPrefix("A + B * C + D")) #顯示A + B * C + D的轉換結果
print(infixToPrefix("( A + B ) * ( C + D )")) #顯示( A + B ) * ( C + D )的轉換結果
print(infixToPrefix(" A + B + C + D ")) #顯示A + B + C + D的轉換結果
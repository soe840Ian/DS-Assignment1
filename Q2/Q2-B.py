#coding=utf-8
from Q2A import rearLast
from rearFirst import rearFirst
import time

start = time.time()
'''code you want to time goes here'''
R = rearLast()
for i in range(0,10000) : #加入10001個item至rearLast，查看它的執行速度。
    R.enqueue(i)
end = time.time()
elapsed = end - start
print "rearLast Time taken: ", elapsed, "seconds."

start = time.time()
L = rearFirst()
for i in range(0,10000) : #加入10001個item至rearFirst，查看它的執行速度。
    L.enqueue(i)
end = time.time()
elapsed = end - start
print "rearFirst Time taken: ", elapsed, "seconds."

start = time.time()
R = rearLast()
for i in range(0,10000) :
    R.enqueue(i)
while not R.isEmpty(): #持續pop出item，直到reaLast是空的，查看它的執行速度。
    R.dequeue()
end = time.time()
elapsed = end - start
print "rearLast Time taken: ", elapsed, "seconds."

start = time.time()
L = rearFirst()
for i in range(0,10000) :
    L.enqueue(i)
while not L.isEmpty() : #持續pop出item，直到First是空的，查看它的執行速度。
    L.dequeue()
end = time.time()
elapsed = end - start
print "rearFirst Time taken: ", elapsed, "seconds."








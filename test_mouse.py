#_*_coding:utf-8_*_
from pymouse import PyMouse
import time

if __name__ == "__main__":
    m = PyMouse()
    for i in range(0,1000):
        m.move(i,i)
        print "move sleep 5"
        time.sleep(5)

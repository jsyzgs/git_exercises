from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,word):
        super(MyThread, self).__init__()
        self.word = word

    def run(self):
        for i in range(10):
            print('This is ',self.word)
            time.sleep(2)

class MyThread1(Thread):
    def __init__(self,word):
        super(MyThread1, self).__init__()
        self.word = word

    def run(self):
        for i in range(10):
            print('This is ',self.word)
            time.sleep(1)


if __name__=="__main__":
    t = MyThread("pycharm")
    t1 = MyThread1('Th')
    t.start()
    t1.start()
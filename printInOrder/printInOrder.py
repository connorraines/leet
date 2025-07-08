import threading

class Foo(object):
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst):
        printFirst()
        self.first_done.set()  # Signal that first() is done

    def second(self, printSecond):
        self.first_done.wait()  # Wait for first() to finish
        printSecond()
        self.second_done.set()  # Signal that second() is done

    def third(self, printThird):
        self.second_done.wait()  # Wait for second() to finish
        printThird()
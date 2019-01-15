import threading
from time import sleep


def main():
    LedMotor = Component()
    LedMotor.go()
    try:
        join_threads(LedMotor.threads)
    except KeyboardInterrupt:
        print "\nKeyboardInterrupt catched."
        print "Terminate main thread."
        print "If only daemonic threads are left, terminate whole program."


class Component(object):
    def __init__(self):
        self.running = True
        self.threads = []

    def LED(self):
        print 'LED LIGHTING'


    def MOTOR(self):
        print 'MOTOR WORKING'


    def go(self):
        LedMotor1 = threading.Thread(target=self.LED)
        LedMotor2 = threading.Thread(target=self.MOTOR)
        # Make threads daemonic, i.e. terminate them when main thread
        # terminates. From: http://stackoverflow.com/a/3788243/145400
        LedMotor1.daemon = True
        LedMotor2.daemon = True
        LedMotor1.start()
        LedMotor2.start()
        self.threads.append(LedMotor1)
        self.threads.append(LedMotor2)

def join_threads(threads):
        for t in threads:
            while t.isAlive():
                t.join(5)

if __name__ == "__main__":
    while True:
        main()
import logging
import sys
import time
from connector import *
from yeelight import *
import thread
import requests

def push_data(gateway, xiaomi, data):
	r = requests.post(str(sys.argv[1]) + '&type=' + str(xiaomi) + '&gateway=' + str(gateway), json=data, timeout=(0.5, 120), verify=False)

cb = lambda g, t, d: push_data(g, t, d)

class myThread (threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print "Starting thread " + self.name
        if self.name == 'Xiaomi' :
            xiaomiconnector()
        else :
            yeelightconnector()
        print "Exiting thread " + self.name

def xiaomiconnector() :
    connector = XiaomiConnector(data_callback=cb)
    while True:
        connector.check_incoming()
        time.sleep(0.05)

def yeelightconnector() :
    yeelight = YeelightConnector(data_callback=cb)
    while True:
        yeelight.check_incoming()
        time.sleep(0.05)

# Create new threads
thread1 = myThread(1, "Xiaomi")
thread2 = myThread(2, "Yeelight")

# Start new Threads
thread1.start()
thread2.start()

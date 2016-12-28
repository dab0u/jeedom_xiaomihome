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

connector = XiaomiConnector(data_callback=cb)
yeelight = YeelightConnector(data_callback=cb)
while True:
    connector.check_incoming()
    yeelight.check_incoming()
    time.sleep(0.05)
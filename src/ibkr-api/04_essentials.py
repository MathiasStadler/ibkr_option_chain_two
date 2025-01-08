# FROM HERE
# https://www.interactivebrokers.com/campus/trading-lessons/essential-components-of-tws-api-programs/

from ibapi.client import *
from ibapi.wrapper import *
import time
import threading


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    # def nextvalidid(self, orderId):
    #    self.orderId = orderId

    def nextValidId(self, orderId: int):
         super().nextValidId(orderId)
         self.nextorderId = orderId
         print('The next valid order id is: ', self.nextorderId)

    def nextid(self):
        self.orderId +=1
        # self.orderId += 1
        return self.orderId

    def currentTime(self, time):
        print(f"Time {time}")

    def error(self, reqId, errorCode, errorString):

        print(
            f"reqID=>{reqId},errorCode=>{errorCode},errorString=>{errorString}")


app = TestApp()
app.connect("127.0.0.1", 7496, 0)

threading.Thread(target=app.run).start()
time.sleep(1)

for i in range(0, 5):
    print(app.nextid())
   # app.reqCurrentTime()

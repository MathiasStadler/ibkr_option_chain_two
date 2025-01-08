# FROM HERE
# https://www.interactivebrokers.com/campus/trading-lessons/python-receiving-market-data/

from ibapi.client import *
from ibapi.wrapper import *
import datetime
import time
import threading
from ibapi.ticktype import TickTypeEnum

port = 7496


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: OrderId):
        self.orderId = orderId
    
    def nextId(self):
        self.orderId += 1
        return self.orderId
    
    def error(self, reqId, errorCode, errorString, advancedOrderReject=""):
        print(f"reqId: {reqId}, errorCode: {errorCode}, errorString: {errorString}, orderReject: {advancedOrderReject}")
    
    def headTimestamp(self, reqId, headTimeStamp):
        print(headTimeStamp)
        print(datetime.datetime.fromtimestamp(int(headTimeStamp)))
        self.cancelHeadTimeStamp(reqId)

    def tickPrice(self,reqId,tickerTyp,price,attrib):
        print("reqId:{reqId}, tickerType: {TickTypeEnum.toStr(tickType)},price:{price},attrib: {attrib} ")

    def tickSize( self, reqId, tickType,size):
         print("reqId:{reqId}, tickerType: {TickTypeEnum.toStr(tickType)},size:{size}")
         




app = TestApp()
app.connect("127.0.0.1", port, 0)
threading.Thread(target=app.run).start()
time.sleep(1)

mycontract = Contract()
mycontract.symbol = "AAPL"
mycontract.secType = "STK"
mycontract.exchange = "SMART"
mycontract.currency = "USD"

app.reqMarketDataType(3)

# app.reqHeadTimeStamp(app.nextId(), mycontract, "TRADES", 1, 2)

#Request Market Data
#app.reqMktData(3, mycontract, '', False, False, [])

time.sleep(3)
print('disconnect')
app.disconnect()
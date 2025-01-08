# https://gist.githubusercontent.com/sravzpublic/5f2ea43249751cef01d61f06e88f18b1/raw/ff79ebb2e359fb9dea1707be5054ff6b0d287812/options_contract.py
# https://docs.sravz.com/docs/tech/ibkr/ibkr-python-api/

from ibapi.client import *
from ibapi.wrapper import *
import time
import signal


class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def contractDetails(self, reqId, contractDetails):
        print(f"contract details: {contractDetails}")

    def contractDetailsEnd(self, reqId):
        print("End of contractDetails")
        self.disconnect()

    def handler(self, signum, frame):
        # print("Signal received! exiting!")
        if self.isConnected():
            self.disconnect()

def main():
    app = TestApp()
 
    signal.signal(signal.SIGINT, app.handler)


# https://stackoverflow.com/questions/20552095/tws-interactive-brokers-api-how-to-fix-no-security-definition-has-been-found
# ERROR 1 200 No security definition has been found for the request

    # app.connect("ibkr", 8888, 1001)
    # connect
    app.connect("127.0.0.1", 7496, clientId=3)  # clientID identifies our application

    mycontract = Contract()
    mycontract.symbol = "ALV"
    mycontract.secType = "OPT"
    mycontract.exchange = "IBIS"
    mycontract.currency = "EUR"
    mycontract.right = "C"
    # Get all call options by not specifying below properties
    mycontract.lastTradeDateOrContractMonth = "20250117"
    mycontract.strike = 55

    # Sleep until IBKR API connection is complete
    # while not app.isConnected():
    time.sleep(3)

    app.reqContractDetails(1, mycontract)

    app.run()

if __name__ == "__main__":
    main()
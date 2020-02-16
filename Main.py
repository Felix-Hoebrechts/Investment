# imports
from datetime import datetime, timezone
import pytz
import time
import requests
import _thread

# initialising
starttime = time.time()
global_current_value = ["","",""]

bought_items = 0
buy_price = 0

low_buyprice = 0
last_measured = 0
list=[]

pre_average1 = 0

# defines
def collecting_current_data(finance_yahoo_link):
    global global_current_value
    while 1:
        responce = requests.get(finance_yahoo_link)
        if "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px)" in responce.content.decode():
            current_price = responce.content.decode().split("Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px)")[1].split(">")[1].split("<")[0]
            global_current_value = finance_yahoo_link.split("=")[1], ": ", current_price


# websites used for testing
link1 = "https://finance.yahoo.com/quote/TSLA?p=TSLA"   #Tesla

linkCode1 = link1.split("=")[1]
# threads starting
_thread.start_new_thread(collecting_current_data, (link1,))

# main
while 1:
    CurrentTime = datetime.now().replace(microsecond=0)
    MarketTime = datetime.now(pytz.timezone('EST')).replace(microsecond=0, tzinfo=None)
    print("Local time:", CurrentTime, "\t \t Market time:", MarketTime, "\t \t Value:", global_current_value[2])

    time.sleep(1)

    # collecting external data

    # list construction

    # predicting


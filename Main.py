#imports
from datetime import datetime
import time
import requests
import _thread

#initialising
starttime = time.time()
global_current_value = ""

bought_items = 0
buy_price = 0

low_buyprice = 0
last_measured = 0
list=[]

pre_average1 = 0

#defines
def collecting_current_data(finance_yahoo_link):
    global global_current_value
    while 1:
        responce = requests.get(finance_yahoo_link)
        if "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px)" in responce.content.decode():
            current_price = responce.content.decode().split("Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px)")[1].split(">")[1].split("<")[0]
            global_current_value = finance_yahoo_link.split("=")[1], ": ", current_price


def average(list):
    sum=0
    teller=0
    for i in list:
        sum+=i
        teller+=1
    gemiddelde = sum/teller
    return gemiddelde


#websites used for testing
link1 = "https://finance.yahoo.com/quote/TSLA?p=TSLA"   #Tesla

linkCode1 = link1.split("=")[1]
#main
_thread.start_new_thread(collecting_current_data, (link1,))
while 1:
    CurrentTime=datetime.now().replace(microsecond=0)
    #last_measured= int(input("geef een getal: "))

    #collecting external data

    #list construction
    if len(list) >= 10:
        del list[0]
    list.append(last_measured)

    #predicting
    if buy_price < pre_average1:
        profit = True
    else:
        profit = False

    if time.time()-starttime > 1:
        if len(global_current_value) == 3:
            print(global_current_value[2])
        else:
            print("global_current_value isn't filled in yet")

        starttime = time.time()

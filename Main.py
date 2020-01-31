#imports
from datetime import datetime
import time
import requests
import _thread

#initialising
current_price = 0

bought_items = 0
buy_price = 0

low_buyprice = 0

list=[]

pre_average1 = 0

#defines
def collecting_current_data():
    global current_price
    while 1:
        responce = requests.get("https://finance.yahoo.com/quote/TSLA?p=TSLA")
        if "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px)" in responce.content.decode():
            current_price = responce.content.decode().split("Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px)")[1].split(">")[1].split("<")[0]
            print(current_price)

def average(list):
    sum=0
    teller=0
    for i in list:
        sum+=i
        teller+=1
    gemiddelde = sum/teller
    return gemiddelde


#websites used for testing
#https://finance.yahoo.com/quote/TSLA?p=TSLA

#main
_thread.start_new_thread(collecting_current_data, ())

while 1:
    CurrentTime=datetime.now().replace(microsecond=0)
    last_measured= int(input("geef een getal: "))

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

    pre_average1 = average(list)

    #selling
    if profit:
        print("sell")

    #buying
    if current_price < low_point:
        pass



    #testprints
    print(list)
    print(average(list))

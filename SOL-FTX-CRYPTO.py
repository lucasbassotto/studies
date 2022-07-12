#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import requests
import time
import pygsheets
import time
gc = pygsheets.authorize(service_file="C:\\Users\\lucas\\arbimulti.json")
sh = gc.open("FUTURESPREAD")


# In[16]:


r_fut1 = requests.get("https://ftx.com/api/markets/SOL-PERP").json()['result']
r_fut2 = requests.get("https://deriv-api.crypto.com/v1/public/get-tickers?instrument_name=ETHUSD-PERP").json()['result']['data']


# In[19]:


timestamp = float(r_fut2[0]['t'])
fut1_bid = r_fut1['bid']
fut1_bidamount = 0
fut1_ask = r_fut1['ask']
fut1_askamount = 0
fut2_bid = float(r_fut2[0]['b'])
fut2_bidamount = 0
fut2_ask = float(r_fut2[0]['k'])
fut2_askamount = 0
fut1_bid, fut1_ask


# In[ ]:


timestamp_list = []
fut1_bidlist = []
fut1_asklist = []
fut2_bidlist = []
fut2_asklist = []
fut1_askamountlist = []
fut1_bidamountlist = []
fut2_askamountlist = []
fut2_bidamountlist = []

while True:
    r_fut1 = requests.get("https://ftx.com/api/markets/SOL-PERP").json()['result']
    r_fut2 = requests.get("https://deriv-api.crypto.com/v1/public/get-tickers?instrument_name=SOLUSD-PERP").json()['result']['data']
    
    timestamp = float(r_fut2[0]['t'])
    fut1_bid = r_fut1['bid']
    fut1_bidamount = 0
    fut1_ask = r_fut1['ask']
    fut1_askamount = 0
    fut2_bid = float(r_fut2[0]['b'])
    fut2_bidamount = 0
    fut2_ask = float(r_fut2[0]['k'])
    fut2_askamount = 0
    
    timestamp_list.append(timestamp)
    fut1_bidlist.append(fut1_bid)
    fut1_asklist.append(fut1_ask)
    fut2_bidlist.append(fut2_bid)
    fut2_asklist.append(fut2_ask)
    fut1_bidamountlist.append(fut1_bidamount)
    fut1_askamountlist.append(fut1_askamount)
    fut2_bidamountlist.append(fut2_bidamount)
    fut2_askamountlist.append(fut2_askamount)
    
    trading_data = {'timestamp': timestamp_list, 'fut1_bid': fut1_bidlist, 'fut1_ask': fut1_asklist, 
                'fut2_bid': fut2_bidlist, 'fut2_ask': fut2_asklist,
                'fut1_bidamount': fut1_bidamountlist, 'fut1_askamount': fut1_askamountlist,
                'fut2_bidamount': fut2_bidamountlist, 'fut2_askamount': fut2_askamountlist}
    
    df = pd.DataFrame(trading_data)
    
    sh[2].set_dataframe(df,(1,1))
    print('spreadbuy', (fut2_bid/fut1_bid-1)*100, 'spreadsell', (fut2_ask/fut1_ask-1)*100,'spreadbuy_at', (fut2_ask/fut1_bid-1)*100, 'spreadsell_at', (fut2_bid/fut1_ask-1)*100)
    time.sleep(1)


# In[ ]:





# In[44]:


r_crypto=requests.get("https://deriv-api.crypto.com/v1/public/get-tickers?instrument_name=BTCUSD-PERP").json()['result']['data']


# In[55]:


r_crypto[0]['b']


# In[ ]:





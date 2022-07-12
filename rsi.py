#!/usr/bin/env python
# coding: utf-8

# In[592]:


import numpy as np
import statistics


# In[603]:


p = [18911.04,18903.68,18886.44,18901.22,18894.81,18890.86,
         18888.48,18876.13,18888.51,18882.75,18879.9,18869.45,18843.38, 18861.39]
#price = prices[-14:]
rsi_list = []
def rsi(prices, n=14):
    up = []
    down = []
    for i in range(0, n-1):
        diff = prices[i+1]-prices[i]
        if diff < 0:
            down.append(abs(diff))
            up.append(0)
        
        if diff > 0:
            up.append(diff)
            down.append(0)
            
        if diff == 0:
            up.append(0)
            down.append(0)
            
    up_avg = (sum(up))/n
    down_avg = (sum(down))/n
    rs = up_avg/abs(down_avg)
    rsi = 100-(100/(1+rs))
    return rsi, up, down, up_avg, down_avg


# In[604]:


rsi, up, down, up_avg, down_avg = rsi(p)
print(rsi, up, down, up_avg, down_avg)


# In[605]:


a = [18911.04,18903.68,18886.44,18901.22,18894.81,18890.86,
         18888.48,18876.13,18888.51,18882.75,18879.9,18869.45,18843.38, 18861.39]
diff1 = a[-1] - a[-2]
up_avg_list = [up_avg]
down_avg_list = [down_avg]

if diff1 < 0:
    down.append(abs(diff))
    up.append(0)
    
if diff1 > 0:
    up.append(diff1)
    down.append(0)

up_avg1 = (13*up_avg_list[0]+abs(up[-1]))/14
down_avg1 = (13*down_avg_list[0]+abs(down[-1]))/14
rs = up_avg1/abs(down_avg1)
rsi = 100-(100/(1+rs))    


# In[606]:


rsi


# In[595]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[545]:





# In[546]:





# In[ ]:





# In[ ]:





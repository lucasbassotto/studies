import hmac
import hashlib
import json
import requests
import time
import pandas as pd
import pygsheets
import ccxt

deribit = ccxt.deribit({
    'enableRateLimit': True,
    'apiKey': 'kJX3pS_y',
    'secret': 'y8DbJBBOwGlcumxUM41KsKBHjRVSTPomGbQdEFZYgFw'})

def cryptocom(method,p):
    API_KEY = "bL4NrTo1kkRfPzzqK2yfWW"
    SECRET_KEY = "MAg7p8sS5Z35xJu36bPHQK"
    base_url = "https://deriv-api.crypto.com/v1/"
    req = {
      "id": 11,
      "method": method,
      "api_key": API_KEY,
      "params": p,
      "nonce": int(time.time() * 1000)
    }

    # First ensure the params are alphabetically sorted by key
    paramString = ""

    if "params" in req:
      for key in sorted(req['params']):
        paramString += key
        value = req['params'][key]
        if value is None:
          paramString += 'null'
        elif isinstance(value, list):
          paramString += ','.join(value)
        else:
          paramString += str(value)

    sigPayload = req['method'] + str(req['id']) + req['api_key'] + paramString + str(req['nonce'])

    req['sig'] = hmac.new(
      bytes(str(SECRET_KEY), 'utf-8'),
      msg=bytes(sigPayload, 'utf-8'),
      digestmod=hashlib.sha256
    ).hexdigest()
    r = requests.post(base_url+req['method'], json=req).json()
    return r

while True:
    gc = pygsheets.authorize(service_file="future-arbitrage.json")
    sh = gc.open("FUTURESPREAD")
    positions = cryptocom("private/get-positions",{})['result']['data']
    balances = cryptocom("private/user-balance",{})['result']['data']
    trades = cryptocom("private/get-trades",{})['result']['data']
    
    #dataframe cryptocom
    df_trades = pd.DataFrame(trades)
    df_balances = pd.DataFrame(balances)
    df_positions = pd.DataFrame(positions)
    
    #deri_positions
    deri_positionsdata = deribit.fetchPositions()
    deribit_bal = deribit.fetchBalance()['info']['result']
    deri_positions = []
    for x in deri_positionsdata:
        deri_positions.append(x['info'])
    
    df_positions_deribit = pd.DataFrame(deri_positions)
    df_balances_deribit = pd.DataFrame(deribit_bal)

    #deri_balances
    
    sh[1].set_dataframe(df_balances, (1,1))
    sh[2].set_dataframe(df_positions, (1,1))
    sh[3].set_dataframe(df_trades, (1,1))
    sh[4].set_dataframe(df_balances_deribit, (1,1))
    sh[5].set_dataframe(df_positions_deribit, (1,1))
    
    print('ok')
    time.sleep(10)

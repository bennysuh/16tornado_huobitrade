#coding=utf-8

import time

import requests

from Util import *


'''
获取账号详情
'''
def getAccountInfo(method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"method":method}
    sign=signature(params)
    params['sign']=sign

    del params['secret_key']

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None

'''
下单接口
@param coinType
@param price
@param amount
@param tradePassword
@param tradeid
@param method
'''
def buy(coinType,price,amount,tradePassword,tradeid,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"price":price,"coin_type":coinType,"amount":amount,"method":method}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']
    if tradePassword:
        params['trade_password']=tradePassword
    if tradeid:
        params['trade_id']=tradeid

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None

'''
提交市价单接口
@param coinType
@param amount
@param tradePassword
@param tradeid
'''

def buyMarket(coinType,amount,tradePassword,tradeid,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"coin_type":coinType,"amount":amount,"method":method}
    sign=signature(params)
    params['sign']=sign
    if tradePassword:
        params['trade_password']=tradePassword
    if tradeid:
        params['trade_id']=tradeid

    del params['secret_key']

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None


'''
撤销订单
@param coinType
@param id
'''

def cancelOrder(coinType,id,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"coin_type":coinType,"id":id,"method":method}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None

'''
查询个人最新10条成交订单
@param coinType
'''
def getNewDealOrders(coinType,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"coin_type":coinType,"method":method}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None

'''
根据trade_id查询oder_id
@param coinType
@param tradeid
'''
def getOrderIdByTradeId(coinType,tradeid,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"coin_type":coinType,"method":method,"trade_id":tradeid}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None

'''
获取所有正在进行的委托
@param coinType
'''
def getOrders(coinType,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"coin_type":coinType,"method":method}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None

'''
获取订单详情
@param coinType
@param id
'''
def getOrderInfo(coinType,id,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"coin_type":coinType,"method":method,"id":id}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None

'''
限价卖出
@param coinType
@param price
@param amount
@param tradePassword
@param tradeid
'''
def sell(coinType,price,amount,tradePassword,tradeid,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"price":price,"coin_type":coinType,"amount":amount,"method":method}
    sign=signature(params)
    params['sign']=sign
    del params['secret_key']
    if tradePassword:
        params['trade_password']=tradePassword
    if tradeid:
        params['trade_id']=tradeid

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None

'''
市价卖出
@param coinType
@param amount
@param tradePassword
@param tradeid
'''
def sellMarket(coinType,amount,tradePassword,tradeid,method,access_key,secret_key):
    timestamp = long(time.time())
    params = {"access_key": access_key,"secret_key": secret_key, "created": timestamp,"coin_type":coinType,"amount":amount,"method":method}
    sign=signature(params)
    params['sign']=sign
    if tradePassword:
        params['trade_password']=tradePassword
    if tradeid:
        params['trade_id']=tradeid

    del params['secret_key']

    payload = urllib.urlencode(params)
    try:
        r = requests.post(HUOBI_SERVICE_API, params=payload,timeout=5)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return None
    except:
        return None


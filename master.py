"""
python3 /Users/joshuatrinhnguyen/Documents/Bot/master.py
python3.10 /Users/joshuatrinhnguyen/Documents/Bot/master.py
cd '' && '/usr/local/bin/python3'  '/Users/joshuatrinhnguyen/Documents/Bot/master.py'  && echo Exit status: $? && type(exit)
python3 -m pip install ccxt

In this buy setup  entry is at the MACD crossover  and the stop loss is below the pullback of the trend. your profit target should be more than the risk you are taking on the trade. so if you lose one and win one  you will still be in profit. there are different ways to set profit targets. personally  i will take 25 percent off the trade when the trade reaches 1 times the risk  and will move the stop loss to break even. then  i will set a second profit target of 2 times the risk i originally took on the trade. so even if the trade never reaches my second profit target  i have already taken 25 percent off the trade in profit  and will not lose money.

In win_or_lose or long_trade/short_trade I have to get my test 10k$ and write it to the beginning of the line to keep a running count
"""

# coding=utf-8
import ccxt
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import time
from datetime import datetime
from pycoingecko import CoinGeckoAPI
import json






#with open('logs.txt','a') as logs: #works
#    fetch_open_orders = ndax.fetch_open_orders(symbol='BTC/CAD', since=None, limit=None,params={})
#    logs.write(str(fetch_open_orders)+"\n") #works
"""
fetch all unfilled currently open orders
:param str|None symbol: unified market symbol
:param int|None since: the earliest time in ms to fetch open orders for
:param int|None limit: the maximum number of  open orders structures to retrieve
:param dict params: extra parameters specific to the ndax api endpoint
:returns [dict]: a list of `order structures <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
"""

#with open('logs.txt','a') as logs: #works
#    fetch_order = ndax.fetch_order(19996977010, symbol=None, params={})
#    logs.write(str(fetch_order)+"\n") #works

#with open('logs.txt','a') as logs: #works
#    fetch_balance = ndax.fetch_balance()
#    logs.write(str(fetch_balance)+"\n") #works


"""
if structure that asks if the buy signal is triggered. if yes, then do 1.5 r/r ratio. when one of these are hit, trigger a p/l count. 1 buy/sell trigger is needed and we stop the loop so we dont spam the logs with so many signals that are really just 1 signal.
"""

#print(tradingview_ta.__version__)
cg = CoinGeckoAPI()
long_trade = False
short_trade = False

stock_higher_timeframe = TA_Handler(
    symbol="BTCUSD", #TSLA
    screener="crypto", #america
    exchange="BITSTAMP", #NASDAQ
    interval=Interval.INTERVAL_1_MINUTE,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
#timeframe = (60*1)+1
timeframe = (60*1)+1
stock_timeframe = TA_Handler(
    symbol="BTCUSD", #TSLA
    screener="crypto", #america
    exchange="BITSTAMP", #NASDAQ
    interval=Interval.INTERVAL_15_MINUTES,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
#print(stock_higher_timeframe.get_analysis().summary) # Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}
"""
INTERVAL_1_MINUTE = "1m"
INTERVAL_5_MINUTES = "5m"
INTERVAL_15_MINUTES = "15m"
INTERVAL_30_MINUTES = "30m"
INTERVAL_1_HOUR = "1h"
INTERVAL_2_HOURS = "2h"
INTERVAL_4_HOURS = "4h"
INTERVAL_1_DAY = "1d"
INTERVAL_1_WEEK = "1W"
INTERVAL_1_MONTH = "1M"
"""

def risk_reward(trade_type,price):
    """
    Reward	Risk	Gain	Loss
    1.50%	1.000%	101.50%	99.00%
    1.45%	0.967%	101.45%	99.03%
    1.40%	0.933%	101.40%	99.07%
    1.35%	0.900%	101.35%	99.10%
    1.30%	0.867%	101.30%	99.13%
    1.25%	0.833%	101.25%	99.17%
    1.20%	0.800%	101.20%	99.20%
    1.15%	0.767%	101.15%	99.23%
    1.10%	0.733%	101.10%	99.27%
    1.05%	0.700%	101.05%	99.30%
    1.00%	0.667%	101.00%	99.33% $
    0.95%	0.633%	100.95%	99.37%
    0.90%	0.600%	100.90%	99.40%
    0.85%	0.567%	100.85%	99.43%
    0.80%	0.533%	100.80%	99.47%
    0.75%	0.500%	100.75%	99.50%
    0.70%	0.467%	100.70%	99.53%
    0.65%	0.433%	100.65%	99.57%
    0.60%	0.400%	100.60%	99.60%
    0.55%	0.367%	100.55%	99.63%
    0.50%	0.333%	100.50%	99.67%
    0.45%	0.300%	100.45%	99.70%
    0.40%	0.267%	100.40%	99.73%
    0.35%	0.233%	100.35%	99.77%
    0.30%	0.200%	100.30%	99.80%
    0.25%	0.167%	100.25%	99.83%
    0.20%	0.133%	100.20%	99.87%
    0.15%	0.100%	100.15%	99.90%
    0.10%	0.067%	100.10%	99.93%
    0.05%	0.033%	100.05%	99.97%
    0.00%	0.000%	100.00%	100.00%
    """
    high=1.01
    low=0.9933

    """
    price = str(price)
    price_dict = price.split()

    #price
    price = price_dict[2].replace(',', '')
    price = float(price)
    print(price)
    """

    if(trade_type=='Long'):
        w_price = high*price
        l_price = low*price
    elif(trade_type=='Short'):
        w_price = low*price
        l_price = high*price

    return w_price,l_price

def price(stock):
    return stock.get_analysis().indicators["close"]

def market():
    #higher timeframes
    ema = stock_timeframe.get_analysis().indicators["EMA200"]
    current_price = price(stock_timeframe)
    if (current_price > ema):
        return "Bull"
    else:
        return "Bear"

def macd(stock):
    macd = stock.get_analysis().indicators["MACD.macd"]
    signal = stock.get_analysis().indicators["MACD.signal"]

    if(macd > signal and macd < 0 and signal < 0): #buy signal
        return "MACD_Buy"
    #elif(macd > signal and macd > 0 and signal > 0): #uptrend continuation
    #    return "Uptrend continuation"
    elif(macd < signal and macd > 0 and signal > 0): #sell signal
        return "MACD_Sell"
    #elif(macd < signal and macd < 0 and signal < 0): #downtrend continuation
    #    return "Downtrend continuation"
    else:
        return None

def connect_account():
    #ndax     = ccxt.ndax({
    #    'apiKey': '68f94f30b27a1f121146c9b99871dc59',
    #    'secret': 'a5b4a4e8c922ee237090cb529f83e42c',
    #    'uid': '181668',
    #    'login': 'nguy1920',
    #    'password': 'Bdhsu8q72g,geusy',
    #})
    return

def remove_trade(timestamp):
    #checks trades.txt and removes the exact trade by identifying the timestamp
    return

def parse_cg(cg):
    #timestamp
    #trade type,coin gecko quote,price to win,price to lose
    #Long,cg,high price (win),low price (lose)
    #Short,cg,low price (win),high price(lose)

    cg = str(cg)
    cg_dict = cg.split()

    #security
    sec = cg_dict[0].replace("'", '')
    sec = sec.replace("{", '')
    sec = sec.replace(":", '')

    #base currency
    base = cg_dict[1].replace("'", '')
    base = base.replace("{", '')
    base = base.replace(":", '')

    #price
    price = cg_dict[2].replace(',', '')
    price = float(price)

    #timestamp
    timestamp = cg_dict[4].replace('}', '')

    return sec,base,price,timestamp

def parse_file(filename):
    with open(filename, "r") as file:
        last_line = file.readlines()[-1]
    line_dict = last_line.split(",")

    trade = line_dict[0] #trade position (short/long)
    date = line_dict[1] #date
    timestamp = line_dict[2] #cg timestamp
    stock = line_dict[3] #stock
    base_currency = line_dict[4] #base currency
    current_price = float(line_dict[5]) #current price
    w_price = float(line_dict[6]) #win price
    l_price = float(line_dict[7]) #lose price

    return trade,date,timestamp,stock,base_currency,current_price,w_price,l_price

def go_long():
    #trades.txt         "LONG - timestampe - current price"
    """
    repeat the same line in trades.txt. we will use each line as active trades and also keywords for logs.txt. in main, main will check if go_long returns true, if so, it will stop the loop. another loop will begin where it will see if the price can complete the trade. only 1 trade can be active. only 3 outcomes, win, lose, null. once it fulfills a win or lose (but not null), then can the entry in trades.txt can be removed. trades.txt should only ever have 0-2 lines: 1 short and 1 long or none.
    """

    if(go_aux()==True):
        now = datetime.now()
        price = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=False, include_24hr_vol=False, include_24hr_change=False, include_last_updated_at=True)
        sec,base,price,timestamp = parse_cg(price)
        w_price,l_price = risk_reward('Long',price)
        with open('logs.txt','a') as logs:
            logs.write('Long,{},{},{},{},{},{},{}\n'.format(str(now),timestamp,sec,base,price,w_price,l_price))
        with open('trades.txt','a') as logs:
            logs.write('Long,{},{},{},{},{},{},{}\n'.format(str(now),timestamp,sec,base,price,w_price,l_price))
        #connect_account()
        #with open('logs.txt','a') as logs: #works
        #    buy = ndax.create_order('BTC/CAD',"limit","buy",0.0001,10,)
        #    logs.write(str(buy)+"\n") #works
        """
        create a trade order
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market' or 'limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float|None price: the price at which the order is to be fullfilled, in units of the quote currency, ignored in market orders
        :param dict params: extra parameters specific to the ndax api endpoint
        :returns dict: an `order structure <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        long_trade = True
    return w_price,l_price

def go_aux():
    time.sleep(timeframe)

    if(market()=="Bull" and macd(stock_timeframe)=="MACD_Buy" and long_trade==False):
        print("aux bull...")
        return True
    elif(market()=="Bear" and macd(stock_timeframe)=="MACD_Sell" and short_trade==False):
        print("aux bear...")
        #check_short()
        return True
    else:
        print("aux null...")
        null_trade()
        return False


def go_short():
    if(go_aux()==True):
        now = datetime.now()
        price = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=False, include_24hr_vol=False, include_24hr_change=False, include_last_updated_at=True)
        sec,base,price,timestamp = parse_cg(price)
        w_price,l_price = risk_reward('Short',price)
        with open('logs.txt','a') as logs:
            logs.write('Short,{},{},{},{},{},{},{}\n'.format(str(now),timestamp,sec,base,price,w_price,l_price))
        with open('trades.txt','a') as logs:
            logs.write('Short,{},{},{},{},{},{},{}\n'.format(str(now),timestamp,sec,base,price,w_price,l_price))
        #connect_account()
        short_trade = True
    return w_price,l_price

def win_or_lose(trade_position):
    #determines if the current trades in play have hit the target price or stop loss or none
    #I need win price and loss price
    #the below code is just for the last line, need to do with for the existing long trade and the other short trade at a time. i need to make an nested if statement that asks if im checking the long trade or short trade and THEN does the calculation.


    price = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=False, include_24hr_vol=False,include_24hr_change=False,include_last_updated_at=True)

    sec,base,price,timestamp = parse_cg(price)
    price = float(price)

    position,date,timestamp,stock,base,current_price,w_price,l_price = parse_file("trades.txt")
    now = datetime.now()

    if(position == "Long"):
        if(price >= w_price):
            with open('win_lose.txt','a') as logs:
                logs.write('{}, Long win\n'.format(str(now),price))
            with open("target.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                    if i != "Long": #might have to put the whole line
                        f.write(i)
                f.truncate()
            long_trade = False
        elif(price <= l_price):
            with open('win_lose.txt','a') as logs:
                logs.write('{}, Long lose\n'.format(str(now),price))
            long_trade = False

        else:
            print('Long win lose else')
    elif(position == "Short"):
        if(price <= w_price):
            with open('win_lose.txt','a') as logs:
                logs.write('{}, Short win\n'.format(str(now),price))
            short_trade = False
        elif(price >= l_price):
            with open('win_lose.txt','a') as logs:
                logs.write('{}, Short lose\n'.format(str(now),price))
            short_trade = False
        else:
            print('Short win lose else')

    return

def null_trade():
    #null              "NULL - timestampe - current price"
    now = datetime.now()
    price = cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=False, include_24hr_vol=False, include_24hr_change=False, include_last_updated_at=True)
    sec,base,price,timestamp = parse_cg(price)
    with open('logs.txt','a') as logs:
        logs.write('Null,{},0,0,0,{},0,0\n'.format(str(now),price))
    return

def check_long():

    return

def check_short():
    return

def main():
    #print(macd(stock_higher_timeframe))
    #print(macd(stock_timeframe))
    #Code for backtest isn't possible. macd() function is live only. The only way to test is testing 100 trades

    """
    Code for live trading
    """
    long_trade=False
    short_trade=True

    print("stock timefram inter: {}".format(stock_timeframe.interval))

    while True:
        print(market())
        print(macd(stock_timeframe))
        if(market()=="Bull" and macd(stock_timeframe)=="MACD_Buy" and long_trade==False):
            print("bull...")
            w_price,l_price = go_long()
        elif(market()=="Bear" and macd(stock_timeframe)=="MACD_Sell" and short_trade==False):
            print("bear...")
            #check_short()
            w_price,l_price = go_short()
        else:
            print("null...")
            null_trade()

        if(long_trade==True):
            win_or_lose("Long")
        elif(short_trade==True):
            win_or_lose("Short")


        time.sleep(10)


if __name__ == "__main__":
    main()

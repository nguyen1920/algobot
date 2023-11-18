"""
NEXT STEPS:
-Minimum profit and more: If I hit my target level, then my stop loss is at break even (buy point) (or crossover) and my new target level is 2:1 RR (or crossover). If I hit my target level at 2:1 RR and not a crossover, then my stop loss is at original 1.5/1 RR profit level  (or crossover) and my last target level is crossover.

Reward1	Risk1	Profit1   	Loss1	Reward2	Risk2	Profit2	   Loss2
1.500%	1.000%	101.500%	99.000%	2.000%	0.000%	102.000%	100.000%
1.450%	0.967%	101.450%	99.033%	2.000%	0.000%	102.000%	100.000%
1.400%	0.933%	101.400%	99.067%	2.000%	0.000%	102.000%	100.000%
1.350%	0.900%	101.350%	99.100%	2.000%	0.000%	102.000%	100.000%
1.300%	0.867%	101.300%	99.133%	2.000%	0.000%	102.000%	100.000%
1.250%	0.833%	101.250%	99.167%	2.000%	0.000%	102.000%	100.000%
1.200%	0.800%	101.200%	99.200%	2.000%	0.000%	102.000%	100.000%
1.150%	0.767%	101.150%	99.233%	2.000%	0.000%	102.000%	100.000%
1.100%	0.733%	101.100%	99.267%	2.000%	0.000%	102.000%	100.000%
1.050%	0.700%	101.050%	99.300%	2.000%	0.000%	102.000%	100.000%
1.000%	0.667%	101.000%	99.333%	2.000%	0.000%	102.000%	100.000% $
0.950%	0.633%	100.950%	99.367%	2.000%	0.000%	102.000%	100.000%
0.900%	0.600%	100.900%	99.400%	2.000%	0.000%	102.000%	100.000%
0.850%	0.567%	100.850%	99.433%	2.000%	0.000%	102.000%	100.000%
0.800%	0.533%	100.800%	99.467%	2.000%	0.000%	102.000%	100.000%
0.750%	0.500%	100.750%	99.500%	2.000%	0.000%	102.000%	100.000%
0.700%	0.467%	100.700%	99.533%	2.000%	0.000%	102.000%	100.000%
0.650%	0.433%	100.650%	99.567%	2.000%	0.000%	102.000%	100.000%
0.600%	0.400%	100.600%	99.600%	2.000%	0.000%	102.000%	100.000%
0.550%	0.367%	100.550%	99.633%	2.000%	0.000%	102.000%	100.000%
0.500%	0.333%	100.500%	99.667%	2.000%	0.000%	102.000%	100.000%
0.450%	0.300%	100.450%	99.700%	2.000%	0.000%	102.000%	100.000%
0.400%	0.267%	100.400%	99.733%	2.000%	0.000%	102.000%	100.000%
0.350%	0.233%	100.350%	99.767%	2.000%	0.000%	102.000%	100.000%
0.300%	0.200%	100.300%	99.800%	2.000%	0.000%	102.000%	100.000%
0.250%	0.167%	100.250%	99.833%	2.000%	0.000%	102.000%	100.000%
0.200%	0.133%	100.200%	99.867%	2.000%	0.000%	102.000%	100.000%
0.150%	0.100%	100.150%	99.900%	2.000%	0.000%	102.000%	100.000%
0.100%	0.067%	100.100%	99.933%	2.000%	0.000%	102.000%	100.000%
0.050%	0.033%	100.050%	99.967%	2.000%	0.000%	102.000%	100.000%


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
from tradingview_ta import TA_Handler, Interval, Exchange
import tradingview_ta
import time
from datetime import datetime
import config

stock_ETHUSD = TA_Handler(
    symbol="ETHUSD", #TSLA
    screener="crypto", #america
    exchange="BITSTAMP", #NASDAQ
    interval=Interval.INTERVAL_1_MINUTE,
    timeout=3600,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
'''
stock_BTCUSD = TA_Handler(
    symbol="BTCUSD", #TSLA
    screener="crypto", #america
    exchange="BITSTAMP", #NASDAQ
    interval=Interval.INTERVAL_15_MINUTES,
    timeout=3600,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)

stock_HQD = TA_Handler(
    symbol="HQD", #TSLA
    screener="canada", #america
    exchange="TSX", #NASDAQ
    interval=Interval.INTERVAL_15_MINUTES,
    timeout=3600,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)

stock_HOU = TA_Handler(
    symbol="HOU", #TSLA
    screener="canada", #america
    exchange="TSX", #NASDAQ
    interval=Interval.INTERVAL_1_MINUTE,
    timeout=3600,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)

stock_HNU = TA_Handler(
    symbol="HNU", #TSLA
    screener="canada", #america
    exchange="TSX", #NASDAQ
    interval=Interval.INTERVAL_1_MINUTE,
    timeout=3600,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)

stock_HND = TA_Handler(
    symbol="HND", #TSLA
    screener="canada", #america
    exchange="TSX", #NASDAQ
    interval=Interval.INTERVAL_30_MINUTES,
    timeout=3600,
    # proxies={'http': 'http://example.com:8080'} # Uncomment to enable proxy (replace the URL).
)
'''
def risk_reward(target,price):
    if(int(target) == 1):
        high=1.01
        low=0.9933
        price = float(price)
        w_price = high*price
        l_price = low*price
    elif(int(target) == 2):
            high=1.02
            low=1
            price = float(price)
            w_price = high*price
            l_price = low*price
    return w_price,l_price

def current_price(stock):
    return stock.get_analysis().indicators["close"]

def ema200(stock):
    ema = stock.get_analysis().indicators["EMA200"]
    price = current_price(stock)
    if (price > ema):
        return True
    else:
        return False

def macd(stock):
    macd = stock.get_analysis().indicators["MACD.macd"]
    signal = stock.get_analysis().indicators["MACD.signal"]
    if(macd > signal and signal <= 0): #buy signal
        return True
    else:
        return False

def write_csv(target,file,stock,price,win_price,lose_price):
    now = datetime.now()
    stock_symbol = stock.symbol
    stock_interval = stock.interval
    with open(file,'a') as f:
        f.write('Long,{},{},{},{},{},{},{}\n'.format(target,stock_symbol,stock_interval,str(now),str(price),win_price,lose_price))
    return

def completed_trades_csv(target,file_trade,file_complete,stock,win_lose,price,end_price):
    now = datetime.now()
    stock_symbol = stock.symbol
    stock_interval = stock.interval
    with open(file_complete,'a') as f:
        f.write('Long,{},{},{},{},{},{},{}\n'.format(target,win_lose,stock_symbol,stock_interval,str(now),str(price),end_price))
    open(file_trade, 'w').close()
    return

def check_existing_trade_csv(file):
    with open(file) as f:
        if 'Long' in f.read():
            return True
        else:
            return False

def confirm_indicator(stock):
    print("Confirming trade...")
    if(stock.interval == "1m"):
        time.sleep(60)
    elif(stock.interval == "5m"):
        time.sleep(300)
    elif(stock.interval == "15m"):
        time.sleep(900)
    elif(stock.interval == "30m"):
        time.sleep(1800)
    elif(stock.interval == "1h"):
        time.sleep(3600)
    elif(stock.interval == "2h"):
        time.sleep(7200)
    elif(stock.interval == "4h"):
        time.sleep(14400)
    elif(stock.interval == "1d"):
        time.sleep(86400)
    elif(stock.interval == "1W"):
        time.sleep(604800)
    elif(stock.interval == "1M"):
        time.sleep(2600000)

    return macd(stock)

def parse_trades_csv(filename):
    with open(filename, "r") as file:
        last_line = file.readlines()[-1]
    line_dict = last_line.split(",")

    trade = line_dict[0] #trade position (short/long)
    target = line_dict[1]
    stock_symbol = line_dict[2]
    stock_interval = line_dict[3]
    time = line_dict[4]
    price = line_dict[5]
    win_price = line_dict[6]
    lose_price = line_dict[7].replace("\n", "")

    return trade,target,stock_symbol,stock_interval,time,price,win_price,lose_price

def main():
    while True:
        stock = stock_ETHUSD
        file = '/Users/joshuatrinhnguyen/Documents/Bot/trades_tv.csv'
        file_complete = '/Users/joshuatrinhnguyen/Documents/Bot/trades_complete_tv.csv'

        is_market_bullish = ema200(stock)
        has_macd_crossed = macd(stock)
        does_trade_exist = check_existing_trade_csv(file)
        now = datetime.now()
        print("{}, {}, bull: {}, macd: {}, exist: {}".format(str(now),stock.symbol,is_market_bullish,has_macd_crossed,does_trade_exist))

        if(is_market_bullish == True and has_macd_crossed == True and does_trade_exist == False): #is the price over 200 EMA, MACD bullish cross and does a long trade already exist?
            if(confirm_indicator(stock) == True):
                price = current_price(stock)
                win_price,lose_price = risk_reward(1,price)
                write_csv(1,file,stock,price,win_price,lose_price)

        does_trade_exist = check_existing_trade_csv(file)
        if(does_trade_exist == True): #if the trade already exists and the trade has not hit the price targets both win or lose yet
        #trade_status is makes an api call to make sure the order closed or not.
            trade,target,stock_symbol,stock_interval,timestamp,price,target_price,stop_loss = parse_trades_csv(file)
            price = current_price(stock)
            if(float(price) >= float(target_price) and int(target) == 1):
                target_price,stop_loss = risk_reward(2,price)
                write_csv(2,file,stock,price,target_price,stop_loss)
            elif(float(price) <= float(stop_loss) and int(target) == 1):
                completed_trades_csv(1,file,file_complete,stock,"Lose",price,stop_loss)
            elif(float(price) >= float(target_price) and int(target) == 2):
                completed_trades_csv(2,file,file_complete,stock,"Win",price,target_price)
            elif(float(price) <= float(stop_loss) and int(target) == 2):
                completed_trades_csv(1,file,file_complete,stock,"Win",price,stop_loss)

        time.sleep(10)

if __name__ == "__main__":
    main()

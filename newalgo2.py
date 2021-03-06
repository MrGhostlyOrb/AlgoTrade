import alpaca_trade_api as tradeapi
import time
import random
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from flask import Flask

#app = Flask(__name__)
#
#@app.route("/")
#def hello():
#    return "Hello World"
#
#if __name__ == "__main__":
#    app.run()



api = tradeapi.REST(
    key_id='PKZSURYWNDUU9OJ3CIMW',
    secret_key='4jInsvPoI0BgBJiuzPFwBw4pQP1WEPhE3EvEGTkV',
    base_url='https://paper-api.alpaca.markets'
)

def weekday_check():
    current_time = datetime.now()
    print(str(current_time))
    current_weekday = current_time.weekday()
    if int(time.strftime("%H")) > 21 and int(time.strftime("%H")) < 13:
        print("Waiting till next trade day")
        time.sleep(60)
        weekday_check()
    elif current_weekday == 5 or current_weekday == 6:
        print("It is currently the weekend")
        time.sleep(10)
        weekday_check()
    else:
        print("Returning to Algo")
        main_alt()


def choose_company_random():

    Universe = ['AAL', 'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'ALXN', 'AMAT', 'AMGN', 'AMZN', 'ASML', 'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'BMRN', 'CA', 'CDNS', 'CELG', 'CERN', 'CHKP', 'CHTR', 'CMCSA', 'COST', 'CSCO', 'CSX', 'CTAS', 'CTRP', 'CTSH', 'CTXS', 'DISH', 'DLTR', 'EA', 'EBAY', 'ESRX', 'EXPE', 'FAST', 'FB', 'FISV', 'FOX', 'FOXA', 'GILD', 'GOOG', 'GOOGL', 'HAS', 'HOLX', 'HSIC', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JBHT', 'JD', 'KHC', 'KLAC', 'LBTYA', 'LBTYK', 'LRCX', 'MAR', 'MCHP', 'MDLZ', 'MELI', 'MNST', 'MSFT', 'MU', 'MXIM', 'MYL', 'NFLX', 'NTES', 'NVDA', 'ORLY', 'PAYX', 'PCAR', 'PYPL', 'QCOM', 'QRTEA', 'REGN', 'ROST', 'SBUX', 'SHPG', 'SIRI', 'SNPS', 'STX', 'SWKS', 'SYMC', 'TMUS', 'TSLA', 'TTWO', 'TXN', 'ULTA', 'VOD', 'VRSK', 'VRTX', 'WBA', 'WDAY', 'WDC', 'WYNN', 'XLNX', 'XRAY']
    len_universe = len(Universe)
    rand_company = random.randrange(0, len_universe)
    chosen_company = Universe[rand_company]
    print("Chosen company is: " + chosen_company)
    return chosen_company

def choose_company_alt():

    best_companies = []

    Universe = ['AAL', 'AAPL', 'ADBE', 'ADI', 'ADP', 'ADSK', 'ALGN', 'ALXN', 'AMAT', 'AMGN', 'AMZN', 'ASML', 'ATVI', 'AVGO', 'BIDU', 'BIIB', 'BKNG', 'BMRN', 'CA', 'CDNS', 'CELG', 'CERN', 'CHKP', 'CHTR', 'CMCSA', 'COST', 'CSCO', 'CSX', 'CTAS', 'CTRP', 'CTSH', 'CTXS', 'DISH', 'DLTR', 'EA', 'EBAY', 'ESRX', 'EXPE', 'FAST', 'FB', 'FISV', 'FOX', 'FOXA', 'GILD', 'GOOG', 'GOOGL', 'HAS', 'HOLX', 'HSIC', 'IDXX', 'ILMN', 'INCY', 'INTC', 'INTU', 'ISRG', 'JBHT', 'JD', 'KHC', 'KLAC', 'LBTYA', 'LBTYK', 'LRCX', 'MAR', 'MCHP', 'MDLZ', 'MELI', 'MNST', 'MSFT', 'MU', 'MXIM', 'MYL', 'NFLX', 'NTES', 'NVDA', 'ORLY', 'PAYX', 'PCAR', 'PYPL', 'QCOM', 'QRTEA', 'REGN', 'ROST', 'SBUX', 'SHPG', 'SIRI', 'SNPS', 'STX', 'SWKS', 'SYMC', 'TMUS', 'TSLA', 'TTWO', 'TXN', 'ULTA', 'VOD', 'VRSK', 'VRTX', 'WBA', 'WDAY', 'WDC', 'WYNN', 'XLNX', 'XRAY']
    
    timeframe = "1Min" # 1Min, 5Min, 15Min, 1H, 1D
     # Start date for the market data in ISO8601 format
    ctime = datetime.now
    startDate = datetime.now() - timedelta(1)
    print("Date today is: " + str(ctime))
    print("Gathering data since: " + str(startDate))
    
    # Tracks position in list of symbols to download
    iteratorPos = 0 
    assetListLen = len(Universe)
    company_dict = {}

    while iteratorPos < assetListLen:
            symbol = Universe[iteratorPos]
            print("Gathering data for " + symbol)
            returned_data = api.get_barset(symbol,timeframe,start=startDate)

            returned_data = returned_data.df[symbol]["open"]

            y = np.array(returned_data)
            if len(y) < 2:
                print("skipping: " + symbol + " because not enough data")
                iteratorPos += 1
                continue
            else:
                z = np.gradient(y)

            

                mean_grad = np.mean(z)

                company_dict[symbol] = mean_grad

                iteratorPos += 1

    sorted_dict = sorted(company_dict.items(), key = lambda x: x[1])
    print(sorted_dict)
    print(sorted_dict[-1])

    
    best_companies.append(sorted_dict[0])
    best_companies.append(sorted_dict[1])
    best_companies.append(sorted_dict[2])
                
            

            # Reads, formats and stores the new bars
        
  
            # Processes all data into numpy arrays for use by talib
           

            
#            # Defines the plot for each trading symbol
#            f, ax = plt.subplots()
#            f.suptitle(symbol)
#            
#            # Plots market data and indicators
#            ax.plot(returned_data,label=symbol,color="black")
#            
#            # Fills the green region if SMA20 > SMA50 and red if SMA20 < SMA50
#            
#            # Adds the legend to the right of the chart
#            ax.legend(loc='center left', bbox_to_anchor=(1.0,0.5))
#            
            

    print(best_companies)
    chosen = random.randrange(0, len(best_companies))
    chosen_company = best_companies[chosen]
    print(chosen_company[0])
    
    return best_companies
    
def buy_shares(company):

    orders = []
    
    number_shares = 1
    symbol = company
    side = "buy"

    orders.append({
        "symbol": symbol,
        "qty": number_shares,
        "side": side,
        })

    buys = [o for o in orders if o['side'] == 'buy']
    for order in buys:

        api.submit_order(
                    symbol=order["symbol"],
                    qty=order["qty"],
                    side="buy",
                    type="market",
                    time_in_force="day",
                )

def sell_shares(company):

    print("selling shares")
    orders = []
    
    number_shares = 1
    symbol = company
    side = "sell"

    orders.append({
        "symbol": symbol,
        "qty": number_shares,
        "side": side,
        })

    sells = [o for o in orders if o['side'] == 'sell']
    for order in sells:

        api.submit_order(
                    symbol=order["symbol"],
                    qty=order["qty"],
                    side="sell",
                    type="market",
                    time_in_force="day",
                )


    

def main():
    clock = api.get_clock()

    total_buys = 3
    companys = choose_company_alt()

    print("Companies in main: " + str(companys))
    
    now = clock.timestamp

    print("The time is currently: " + str(now))
        
    while clock.is_open == True and total_buys != 0:
        for com in companys:
            print("Buying shares now")
            buy_shares(com[0])
            print("Successfully bought shares in: " + com[0])
            total_buys = total_buys - 1 
            time.sleep(60)
            if int(time.strftime("%H")) == 20:
                print("Selling now")
                sell_shares(com[0])
            elif clock.is_open == False:
                weekday_check()
            else:
                print("Not time to sell yet")
                continue
    

def main_alt():
    start = True
    companys = choose_company_alt()
    total_buys = 1
    while start == True:
        clock = api.get_clock()
        now = clock.timestamp
        print("The time is currently: " + str(now))
        if clock.is_open == True:
            if int(time.strftime("%H")) < 20 and total_buys > 0:
                for com in companys:
                    print("Buying shares now")
                    buy_shares(com[0])
                    print("Successfully bought shares in: " + com[0])
                    total_buys = total_buys - 1

                    positions = api.list_positions()
                    

                    
                    time.sleep(30)

            elif int(time.strftime("%H")) == 20:
                print("Time to sell")
                for com in companys:
                    print("Selling " + com[0] + " now")
                    sell_shares(com[0])
                    print("Successfully sold shares in: " + com[0])
                    time.sleep(30)
            else:

                print("Currently open positions are: ")
                positions = api.list_positions()
                if len(positions) > 1:
                    print(positions)
                    print("There are positions to sell at the end of the day")
                else:
                    print("There are no positions to sell at the end of the day")

                print("Currently open orders are: ")
                orders = api.list_orders()
                print(orders)
                
                print("Nothing to do, sleeping zzz")
                print(int(time.strftime("%H")))
                time.sleep(60)
        else:
            print("Market Closed")
            time.sleep(60)
            weekday_check()

main_alt()






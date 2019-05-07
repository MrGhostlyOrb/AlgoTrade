import alpaca_trade_api as tradeapi
import time
import random
import matplotlib.pyplot as plt
from datetime import datetime
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
    key_id='PK4765X8YCO23X3R24IL',
    secret_key='7SeHK5LEVpGwsVQnQiVxn9W75WCjPNn4h4HoYQq6',
    base_url='https://paper-api.alpaca.markets'
)

def weekday_check():
    current_time = datetime.now()
    print(str(current_time))
    current_weekday = current_time.weekday()
    while current_weekday == 5 or 6:
        print("It is currently the weekend")
        time.sleep(10)
    else:
        print("It is no longer a weekend")
        main()


def choose_company():

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
    startDate = "2019-04-22T09:10:00.000Z" # Start date for the market data in ISO8601 format

    # Tracks position in list of symbols to download
    iteratorPos = 0 
    assetListLen = len(Universe)
    final_gradients = []
    final_symbols = []
    company_dict = []

    while iteratorPos < assetListLen:
            symbol = Universe[iteratorPos]
            
            returned_data = api.get_barset(symbol,timeframe,start=startDate)

            returned_data = returned_data.df[symbol]["open"]

            y = np.array(returned_data)
            if len(y) < 2:
                print("skipping, not enough data")
                iteratorPos += 1
                continue
            else:
                z = np.gradient(y)

            

                x = np.mean(z)

                print(z)
                print(x)

                if x > 0:
                    print("Buy " + symbol)
                    best_companies.append(symbol)
                
                
                else:
                    print("Sell " + symbol)
                iteratorPos += 1
            

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
    print(chosen_company)
    
    return chosen_company
    
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

def wait_next_tradeday():

    clock = api.get_clock()

    if clock.next_open < clock.timestamp:
        print("Sleeping till next day")
        time.sleep(5)
        weekday_check()
    else:
        main()
    

def main():
    clock = api.get_clock()

    total_buys = 100
    company = choose_company_alt()

    print("Company in main: " + company)
    
    now = clock.timestamp

    print("The time is currently: " + str(now))

    if clock.is_open == True and total_buys != 0:
        print("Buying shares now")
        buy_shares(company)
        print("Successfully bought shares")
        time.sleep(60)
        print("Selling shares now")
        sell_shares(company)
        print("Successfully sold shares")

        total_buys = total_buys - 1 
        
        main()

    elif clock.is_open == False:
        weekday_check()
    elif total_buys == 0:
        weekday_check()
    
    else:
        print("Else?")
    
    
main()

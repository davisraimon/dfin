# dfin



dfin is a simple package that can be used to get stock details. This is built on yfinance package.
https://pypi.org/project/yfinance/





> In this initial version
> i have included methods for getting stock details,
>plotting multiple data directly and 
>downloading them as CSV file for
> future works.

#### Installation

dfin requires [yfinance](https://pypi.org/project/yfinance/) support since it is built on it
```sh
$ pip install dfin
```

### Stock Tickers
A ticker symbol or stock symbol is an abbreviation used to uniquely identify publicly traded shares of a particular stock on a particular stock market. A stock symbol may consist of letters, numbers or a combination of both.
For example : 
Apple Inc.
NASDAQ: AAPL

### Methods included

> getStockDetails('**stock_ticker**')
Accepts only one argument : stock ticker.

```sh
$ getStockDetails('SBIN.NS')
```
> plotStockDetails('**stock_ticker_list**')
Accepts only one argument : a list of stock tickers.
```sh
$ plotStockDetails(["SBIN.NS","HDFCBANK.NS","INDUSINDBK.NS"])
```

>downloadStockDetailsCSV('**stock_ticker**','**period**')
Accepts two arguments : stock ticker and period for which the data should be retrieved.
period 3y means data will ne retrieved for last 3 years.
```sh
$ downloadStockDetailsCSV("SBIN.NS","3y")
```

Credits : yfinance

This project is completely executed for learning purpose.
Feel free to contact me : davisraimon@gmail.com


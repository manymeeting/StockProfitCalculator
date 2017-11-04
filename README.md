# Financial Tools in Python
This repository comprises python utilities such as command line style stock profit calculator and real-time stock price fetcher.

## Stock Profit Calculator
The calculator is a cmd-like program that will take the following inputs:

- A stock symbol
- Allotment (number of shares)
- Final share price (in dollars)
- Sell commission (in dollars)
- Inital share price (in dollars)
- Buy commission (in dollars)
- Captial gain tax rate (in %)

then output the following items after computation:

- Proceeds (Allotment x Final share price)
- Cost (Allotment x Initial Share Price + commissions + Tax on Capital Gain)
- Net Profit (in dollars)
- Return on investment (in %)
- Break even price (in dollars)

## Real-time Stock Price Fetcher
Before June 2017, Most of the real-time stock price fetching tools depends on Yahoo Finance API, which has been abandoned by its owner in the middle of 2017. In order to get the real-time stock price, I analyzed Google Finance web pages and discovered a relatively stable and simple way to fetch all the necessary values from HTML meta data.

Of course the page view may change in the future, though, I believe this program method will probably work fine as long as the Google keeps their meta tags. For example:

    <meta content="Apple Inc." itemprop="name">
	<meta content="https://www.google.com/finance?cid=22144" itemprop="url">
	<meta content="https://www.google.com/finance/chart?cht=g&amp;q=NASDAQ:AAPL&amp;tkr=1&amp;p=1d&amp;enddatetime=2017-11-03T16:00:01Z" itemprop="imageUrl"/>
	<meta content="AAPL" itemprop="tickerSymbol"/>
	<meta content="NASDAQ" itemprop="exchange"/>
	<meta content="America/New_York" itemprop="exchangeTimezone"/>
	<meta content="172.50" itemprop="price"/>
	<meta content="+4.39" itemprop="priceChange"/>
	<meta content="2.61" itemprop="priceChangePercent"/>
	<meta content="true" itemprop="isAfterHours"/>
	<meta content="172.40" itemprop="afterHoursPrice"/>
	<meta content="-0.10" itemprop="afterHoursPriceChange"/>
	<meta content="-0.06" itemprop="afterHoursPriceChangePercent"/>
	<meta content="2017-11-03T23:59:45Z" itemprop="afterHoursQuoteTime"/>
	<meta content="2017-11-03T16:00:01Z" itemprop="quoteTime">
	<meta content="NASDAQ real-time data" itemprop="dataSource">
	<meta content="//www.google.com/help/stock_disclaimer.html#realtime" itemprop="dataSourceDisclaimerUrl">
	<meta content="USD" itemprop="priceCurrency">
We can get values like price, priceChange, and priceChangePercent directly from the attributes in meta tags.

This program will take a stock symbol as input and output the following:

- Current date and time
- Full name of the company
- Stock price
- Value changes (+ for increase and - for decrease)
- Percentage changes (+ for increase and - for decrease)

A typical use case looks like:

    Input:
	Please enter a symbol ('exit' to quit) :
	ADBE
	Output:
	Sat Nov  4 03:42:50 2017
	Adobe Systems Incorporated (ADBE)
	182.30 +1.36 (0.75)

-------------------------------------------------------------------------------
Copyright (C) 2017 Mutian Wang, licensed under the [MIT License](http://www.opensource.org/licenses/mit-license.php)

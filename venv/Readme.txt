Broker Stock API

These APIs can be used as Broker API
following are the different APIs available in this Rest API

1. Get Quote

    This API will give real time data from stock market for given stock symbol.

    input - stock symbol

    output - Quotes for that symbol


2. Search a symbol for a company

    This API will search for different companies available in the market those contains search string in their name or in stock symbol

    input - search string

    output - company quotes matching given search string

3. Buy Stock

    This API will buy a stock for logged in user. This will update order history as well as update funds and update portfolio
    input - user name, company stock symbol, price, number of shares and other optional inputs
    output - transaction output

            200 - ok

            201 - insufficient funds

            500 - Internal Server Error


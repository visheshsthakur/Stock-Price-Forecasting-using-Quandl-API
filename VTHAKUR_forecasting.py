

QUANDLKEY = "M_z8iQBbA2RrTC3FvVmM"
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import quandl
import numpy as np
import datetime as datetime
quandl.ApiConfig.api_key = QUANDLKEY

#### Question 1 ####
def importQuotes(a, b, c):
    quandl.ApiConfig.api_key = QUANDLKEY
    ticker_symbol = a
    date1      = b
    date2      = c
    dataSource = "EOD/%s" % (ticker_symbol)
    #dataSource = "WIKI/%s" % (ticker_symbol)
    quotes = quandl.get(dataSource, start_date=date1, end_date=date2, returns="numpy")
    #print(quotes)
    #print(quotes.dtype)
    resultA = quotes['Close']
    return(resultA)
    
#### Question 2 ####

def forecastMA(x, resultA, z):
    ma = []
    for i in range(x):
        z = resultA[i-x]
        ma.append(z)
    forecast = (sum(ma))/x
    return(round(forecast, 2)
    
#### Question 3 ####

def forecastLR(period, resultA):
    n = len(resultA)
    P = 0
    Q = 0
    for i in range(n):
        P = P + (i)*resultA[i]
        Q = Q + resultA[i]
    Sxy = n*P - ((n*(n-1))/2)*Q
    Sxx = (n*n*(n+1)*(2*n+1))/6 - (n*n*(n+1)*(n+1))/4
    b = Sxy/Sxx
    R = np.mean(resultA)
    a = R - (b*(n+1))/2
    t = n + period
    Dt = a + b*t
    return(round(Dt,2), b, a)

#### Question 4 ####

def forecastHolt(period, alpha, beta, resultA):
    n = len(resultA)
    P = 0
    Q = 0
    for i in range(n):
        P = P + (i)*resultA[i]
        Q = Q + resultA[i]
    Sxy = n*P - ((n*(n-1))/2)*Q
    Sxx = (n*n*(n+1)*(2*n+1))/6 - (n*n*(n+1)*(n+1))/4
    b = Sxy/Sxx
    R = np.mean(resultA)
    a = R - (b*(n+1))/2
    S = [a]
    G = [b]
    for i in range(0, n):
        A = alpha*resultA[i] + (1 - alpha)*(S[i] + G[i])
        S.append(A)
        B = beta*(S[i+1] - S[i]) + (1 - beta)*G[i]
        G.append(B)
    tau = period
    FHolt = S[-1] + tau*G[-1]
    return(round(FHolt,2))

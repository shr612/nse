import time import urllib2 from urllib2 import urlopen

#  objective of this code is to identify companies with pbr < 0.8 in nse30 -- basic stock screener

nse30 = ['ACC','BHEL','BHARTIARTL','CIPLA','DLF','HDFCBANK','HEROMOTOCO','HINDALCO','HINDUNILVR-EQ','HDFC','ITC','ICICIBANK','INFY','JPASSOCIAT','JINDALSTEL','LT','M&M','MARUTI','NTPC','ONGC','RCOM','RELIANCE','RELINFRA','SBIN', 'TCS', 'TATAMOTORS','TATAPOWER','TATASTEEL','WIPRO']


def yahooKeyStats(stock) :
  try:
      sourceCode = urllib2.urlopen('https://in.finance.yahoo.com/q/ks?s='+stock+'.NS').read()
      pbr = sourceCode.split('Price/Book (mrq):</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
      if float(pbr) <.80 :
        print ('price to book ratio:'),stock,pbr

  except Exception,e:
    print 'Data for '+stock+' not available on yahoo finance '


for eachStock in nse30:
      yahooKeyStats(eachStock)
      #time.sleep(1)

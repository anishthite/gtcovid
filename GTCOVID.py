import requests
import pandas as pd
import lxml
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.metrics import r2_score


page = requests.get('http://health.gatech.edu/coronavirus/health-alerts')
page = page.text[page.text.index('<h3>Current Month</h3>'):]
dfs = pd.read_html(page)
megadf = pd.concat(dfs)
megadf["Date Reported"] = megadf["Date Reported"].astype("datetime64")
megadf.groupby(megadf["Date Reported"].dt.week)[['Date Reported']].count()[:-1].plot(kind="line",legend=None,title="New Covid-19 Cases at GT",figsize=(15,5)).set_xlabel('Week Number')
plt.savefig('gtweekly.png')
megadf.groupby(megadf["Date Reported"].dt.date)[['Date Reported']].count().plot(kind="line",legend=None,title="New Covid-19 Cases at GT",figsize=(15,5)).set_xlabel('Date')
plt.savefig('gtdaily.png')
megadf.groupby(megadf["Date Reported"].dt.date)[['Date Reported']].count().rolling(10).mean().plot(kind="line",legend=None,title="New Covid-19 Cases at GT (10 day rolling mean)",figsize=(15,5)).set_xlabel('Date')
plt.savefig('gtdaily10day.png')

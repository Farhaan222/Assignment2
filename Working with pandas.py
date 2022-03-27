import pandas as pd
data = pd.read_csv("E:/IPL Matches 2008-2020.csv")
data.head(10)
data.tail()
data.info()
data.result_margin.mean()
data.result_margin.median()
data.result_margin.mode()
data.result_margin.std()
data.result_margin.var()
data.result_margin.skew()
data.result_margin.kurt()
data.result_margin.hist()
data.winner.mode()
data.winner.value_counts()
data.toss_winner.value_counts()
data.venue.value_counts()
data.shape
data.size
data.columns

# fintest
finanical dataset for algorithm test
(增量更新，不删除数据 incremental updating mode)

# structure
* dataset:  specific data
* api: api for local dataset

# API
```
fintest.crypto.binance.get_future_klines [data range: 2020-11-01 ~ 2020-12-01]
fintest.crypto.binance.get_future_trades_demo1/get_future_klines_demo1: get `Full` data
```

# Usage
```python
from fintest.crypto.binance import api
data = api.get_future_klines(symbol='BTCUSDT', start_dt='2020-11-20', end_dt='2020-11-21')
assert(len(data) == 12*2*60 + 1)
```

# ChangeLog
* [@2020-12-02 00:24:52] origin https://github.com/gseismic/fintest
* [@2021-07-09 09:21:12] Update 

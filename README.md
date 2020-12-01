# fintest
finanical dataset for algorithm test
(incremental updating mode)

# structure
* dataset:  specific data
* api: api for local dataset

# Usage
```python
from fintest.crypto.binance import api
data = api.get_future_klines(symbol='BTCUSDT', start_dt='2020-11-20', end_dt='2020-11-21')
assert(len(data) == 12*2*60 + 1)
```
# ChangeLog
* [@2020-12-01 23:18:45] origin: /media/lsl/seagate6/git/fintest

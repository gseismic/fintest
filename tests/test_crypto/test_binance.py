import config
config.install()
from fintest.crypto.binance import api


def test_get_future_klines():
    data = api.get_future_klines(symbol='BTCUSDT', 
                                 interval='1m',
                                 start_dt='2020-11-20', 
                                 end_dt='2020-11-25')
    print(data, len(data))
    # assert(len(data) == 12*2*60 + 1)


if __name__ == '__main__':
    if 1:
        test_get_future_klines()

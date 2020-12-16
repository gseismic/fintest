import config
config.install()
from fintest.crypto.binance import api


def test_get_future_klines():
    data = api.get_future_klines(symbol='BTCUSDT', 
                                 interval='1m',
                                 start_dt='2020-11-20', 
                                 end_dt='2020-11-21')
    print(data, len(data))
    # assert(len(data) == 12*2*60 + 1)


def test_future_trades001():
    data = api.load_bntrade_demo()
    print(data, len(data))


if __name__ == '__main__':
    if 0:
        test_get_future_klines()
    if 1:
        test_future_trades001()

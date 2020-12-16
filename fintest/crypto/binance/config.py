import os


DATADIR = os.path.dirname(os.path.abspath(__file__))

BN_BTCUSDT_2020_SQLITE3_BASEFILE = 'dataset/bn_BTCUSDT_2020.sqlite3'
BN_BTCUSDT_2020_SQLITE3 = os.path.join(DATADIR, BN_BTCUSDT_2020_SQLITE3_BASEFILE)

BN_BTCUSDT_20201209_0_TRADES_SQLITE3_BASEFILE = 'dataset/binance_futureusdt_20201209-0_trades.sqlite3'
BN_BTCUSDT_20201209_0_TRADES_SQLITE3 = os.path.join(DATADIR,
                                                    BN_BTCUSDT_20201209_0_TRADES_SQLITE3_BASEFILE)

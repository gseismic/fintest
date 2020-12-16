import arrow
import sqlite3
from fintest.crypto.binance.config import (
    BN_BTCUSDT_2020_SQLITE3, 
    BN_BTCUSDT_20201209_0_TRADES_SQLITE3 
)
from fintest.utils.io import ensure_xzfile_decompressed


def to_unixepoch(any_dt, to_ms=False, to_int=True):
    if to_ms:
        rv = arrow.get(any_dt).datetime.timestamp() * 1000
    else:
        rv = arrow.get(any_dt).datetime.timestamp()
    if to_int:
        rv = int(rv)
    return rv


def get_future_klines(symbol, interval, start_dt, end_dt):
    if interval != '1m':
        raise Exception(f'Unsupported parameter value `interval`{interval}')

    _start_dt = to_unixepoch(start_dt, to_ms=True)
    _end_dt = to_unixepoch(end_dt, to_ms=True)
    _symbol = symbol.upper()
    # [@2020-12-15 16:25:14] fix
    assert(symbol == 'BTCUSDT')
    # if _symbol == 'BTCUSDT': _symbol = 'TBCUSDT'
    ensure_xzfile_decompressed(BN_BTCUSDT_2020_SQLITE3)
    conn = sqlite3.connect(BN_BTCUSDT_2020_SQLITE3)
    conn.row_factory = sqlite3.Row
    try:
        cu = conn.cursor()
        try:
            query_sql = f'''SELECT * 
            FROM TBCUSDT_1m where open_time between
            {_start_dt} and {_end_dt}'''
            cu.execute(query_sql)
            data = [dict(r) for r in cu.fetchall()]
        finally:
            cu.close()
    finally:
        conn.close()
    return data


def load_():
    dbfile = BN_BTCUSDT_20201209_0_TRADES_SQLITE3
    ensure_xzfile_decompressed(dbfile)
    conn = sqlite3.connect(dbfile)
    conn.row_factory = sqlite3.Row
    try:
        cu = conn.cursor()
        try:
            query_sql = f'''SELECT * 
            FROM TBCUSDT_1m where open_time between
            {_start_dt} and {_end_dt}'''
            cu.execute(query_sql)
            data = [dict(r) for r in cu.fetchall()]
        finally:
            cu.close()
    finally:
        conn.close()
    return data

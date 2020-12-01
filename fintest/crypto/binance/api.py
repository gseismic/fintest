import os
import arrow
import sqlite3
from fintest.crypto.binance.config import BN_BTCUSDT_2020_SQLITE3
from fintest.utils.io import ensure_xzfile_decompressed


def to_unixepoch(any_dt, to_ms=False, to_int=True):
    if to_ms:
        rv = arrow.get(any_dt).datetime.timestamp() * 1000
    else:
        rv = arrow.get(any_dt).datetime.timestamp()
    if to_int:
        rv = int(rv)
    return rv


def get_future_klines(symbol, start_dt, end_dt):
    _start_dt = to_unixepoch(start_dt, to_ms=True)
    _end_dt = to_unixepoch(end_dt, to_ms=True)
    _symbol = symbol.upper()

    ensure_xzfile_decompressed(BN_BTCUSDT_2020_SQLITE3)
    conn = sqlite3.connect(BN_BTCUSDT_2020_SQLITE3)
    try:
        cu = conn.cursor()
        try:
            query_sql = f'''SELECT * 
            FROM BTCUSDT_1m where symbol="{_symbol}" and open_time between
            {_start_dt} and {_end_dt}'''
            cu.execute(query_sql)
            data = cu.fetchall()
        finally:
            cu.close()
    finally:
        conn.close()
    return data

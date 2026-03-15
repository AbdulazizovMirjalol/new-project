import MetaTrader5 as mt5
import pandas as pd
from config import SYMBOL


def connect_mt5():
    if not mt5.initialize():
        print("MT5 ulanmayapti")
        return False

    print("MT5 ga muvaffaqiyatli ulandi")
    return True


def disconnect_mt5():
    mt5.shutdown()
    print("MT5 ulanish yopildi")


def get_gold_data(timeframe=mt5.TIMEFRAME_M15, bars=50):
    rates = mt5.copy_rates_from_pos(SYMBOL, timeframe, 0, bars)

    if rates is None:
        print("XAUUSD data olinmadi")
        return None

    df = pd.DataFrame(rates)
    df["time"] = pd.to_datetime(df["time"], unit="s")

    return df
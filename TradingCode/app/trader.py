import MetaTrader5 as mt5
from config import MAGIC_NUMBER


def has_open_position(symbol, magic_number=MAGIC_NUMBER):
    positions = mt5.positions_get(symbol=symbol)
    if positions is None:
        return False

    for pos in positions:
        if pos.magic == magic_number:
            return True
    return False


def place_market_order(symbol, signal, lot_size, sl, tp, magic_number=MAGIC_NUMBER):
    info = mt5.symbol_info(symbol)
    tick = mt5.symbol_info_tick(symbol)

    if info is None:
        return False, f"Symbol topilmadi: {symbol}"

    if tick is None:
        return False, f"Tick topilmadi: {symbol}"

    if not info.visible:
        if not mt5.symbol_select(symbol, True):
            return False, f"Symbolni Market Watch ga qo'shib bo'lmadi: {symbol}"

    if has_open_position(symbol, magic_number):
        return False, f"{symbol} bo'yicha ochiq bot pozitsiyasi bor"

    if signal == "BUY":
        order_type = mt5.ORDER_TYPE_BUY
        price = tick.ask
        if not (sl < price < tp):
            return False, "BUY uchun SL < price < TP noto'g'ri"
    elif signal == "SELL":
        order_type = mt5.ORDER_TYPE_SELL
        price = tick.bid
        if not (tp < price < sl):
            return False, "SELL uchun TP < price < SL noto'g'ri"
    else:
        return False, f"Noto'g'ri signal: {signal}"

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": float(lot_size),
        "type": order_type,
        "price": float(price),
        "sl": float(sl),
        "tp": float(tp),
        "deviation": 20,
        "magic": magic_number,
        "comment": "GoldBot AutoTrade",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)

    if result is None:
        return False, "order_send None qaytardi"

    if result.retcode != mt5.TRADE_RETCODE_DONE:
        return False, f"Order ochilmadi: retcode={result.retcode}, comment={result.comment}"

    return True, f"Order ochildi: ticket={result.order}"
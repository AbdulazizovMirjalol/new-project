# from mt5_client import connect_mt5, disconnect_mt5
# from analyzer import run_analysis
# from reporter import (
#     show_analysis_report,
#     show_price_table,
#     save_analysis_to_file,
#     save_bars_to_csv,
#     show_final_decision,
#     show_run_context,
#     save_signal_journal,
#     show_signal_stats,
#     show_recent_signals,
#     show_actionable_signals,
#     show_hot_signals,
#     show_ready_signal_banner,
#     show_signal_mode,
#     show_execution_signal_banner,
#     play_signal_sound,
# )

# from config import SIGNAL_MODE

# def run_once():
#     if not connect_mt5():
#         return

#     result = run_analysis()

#     if result is not None:
#         show_run_context(
#             symbol=result["symbol"],
#             h1_timeframe_name=result["h1_timeframe_name"],
#             m15_timeframe_name=result["m15_timeframe_name"],
#         )

#         show_signal_mode(SIGNAL_MODE)

#         show_price_table(result["m15_df"])

#         show_analysis_report(
#             h1_timeframe_name=result["h1_timeframe_name"],
#             m15_timeframe_name=result["m15_timeframe_name"],
#             h1_trend=result["h1_trend"],
#             m15_trend=result["m15_trend"],
#             alignment_text=result["alignment_text"],
#             rsi_value=result["last_rsi"],
#             rsi_text=result["rsi_text"],
#             macd_text=result["macd_text"],
#             candle_confirmation=result["candle_confirmation"],
#             support=result["support"],
#             resistance=result["resistance"],
#             atr_value=result["atr_value"],
#             price_location=result["price_location"],
#             entry_zone_text=result["entry_zone_text"],
#             summary=result["summary"],
#             trade_comment=result["trade_comment"],
#             setup_status=result["setup_status"],
#             signal_strength=result["signal_strength"],
#             trade_plan=result["trade_plan"],
#             final_signal=result["final_signal"],
#             alert_message=result["alert_message"],
#             reason=result["reason"],
#             suggested_entry=result["suggested_entry"],
#             suggested_sl=result["suggested_sl"],
#             suggested_tp=result["suggested_tp"],
#             risk_reward_ratio=result["risk_reward_ratio"],
#         )

#         show_final_decision(
#             h1_timeframe_name=result["h1_timeframe_name"],
#             m15_timeframe_name=result["m15_timeframe_name"],
#             final_signal=result["final_signal"],
#             setup_status=result["setup_status"],
#             signal_strength=result["signal_strength"],
#             trade_plan=result["trade_plan"],
#             alert_message=result["alert_message"],
#             reason=result["reason"],
#             signal_mode=SIGNAL_MODE,
#         )

#         play_signal_sound(
#             setup_status=result["setup_status"],
#             final_signal=result["final_signal"],
#         )

#         show_ready_signal_banner(result)
#         show_execution_signal_banner(result)

#         save_analysis_to_file(result)
#         save_bars_to_csv(result)
#         save_signal_journal(result)
#         show_signal_stats()
#         show_recent_signals()
#         show_actionable_signals()
#         show_hot_signals()

#     disconnect_mt5()


# def start():
#     print("======================================")
#     print("   GOLD TRADING ANALYSIS TERMINAL   ")
#     print("======================================")
#     run_once()


# if __name__ == "__main__":
#     start()
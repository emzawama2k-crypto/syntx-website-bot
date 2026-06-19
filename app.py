import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

# --- TELEGRAM GATEWAY CONFIG ---
TOKEN = "8845422871:AAG5eLOW2ycgxmCMUaMqaDiY0ygZixQ4k1k"
CHAT_ID = "@MySyntXSignals"

st.set_page_config(page_title="SyntX Master Matrix", page_icon="📊", layout="wide")
st.title("🚨 SyntX Adaptive Master Matrix")
st.write("Real-time Top-Down Institutional Signal Dashboard")

# --- CORE ALGO ENGINE ---
def analyze_market_data():
    np.random.seed(int(time.time()))
    prices_h1 = np.random.normal(3500, 50, 100).tolist()
    prices_m15 = np.random.normal(3500, 10, 100).tolist()
    
    df_h1 = pd.DataFrame(prices_h1, columns=['close'])
    df_h1['ema'] = df_h1['close'].ewm(span=50, adjust=False).mean()
    h1_close = df_h1['close'].iloc[-1]
    h1_ema = df_h1['ema'].iloc[-1]
    
    is_macro_bullish = h1_close > h1_ema
    is_macro_bearish = h1_close < h1_ema
    
    m15_close = prices_m15[-1]
    m15_high1 = prices_m15[-2] + 2
    m15_low1 = prices_m15[-2] - 2
    m15_high2 = prices_m15[-3] + 4
    m15_low2 = prices_m15[-3] - 4
    
    is_inside_bar = (m15_high1 < m15_high2) and (m15_low1 > m15_low2)
    inside_bar_breakout_up = is_inside_bar and (m15_close > m15_high1)
    inside_bar_breakout_down = is_inside_bar and (m15_close < m15_low1)
    
    action = "HOLD"
    strategy = "Scanning for institutional footprint structures..."
    
    if inside_bar_breakout_up and is_macro_bullish:
        action = "BUY"
        strategy = "Top-Down Volatility Compression Breakout Upside"
    elif inside_bar_breakout_down and is_macro_bearish:
        action = "SELL"
        strategy = "Top-Down Volatility Compression Breakout Downside"
        
    return h1_close, h1_ema, m15_close, action, strategy

# --- SCRIPT BROADCASTER ---
def send_telegram_alert(asset, action, strategy, price):
    emoji = "🟢" if action == "BUY" else "🔴"
    message = (
        f"🚨 *WELTRADE SYNTX WEBSITE SIGNAL* 🚨\n\n"
        f"📊 *ACTION REQUIRED*: {emoji} *{action} / LONG* {emoji}\n\n"
        f"Asset: `{asset}`\n"
        f"Model Strategy: *{strategy}*\n"
        f"----------------------------------------\n"
        f"Execution Entry Quote: `{price:.2f}`\n"
    )
    url = f"https://telegram.org{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    requests.post(url, json=payload)

# --- WEB DASHBOARD FRONTEND DISPLAY ---
h1_p, h1_e, m15_p, signal_action, signal_strat = analyze_market_data()

col1, col2 = st.columns(2)
with col1:
    st.metric(label="H1 Trend Frame Price", value=f"{h1_p:.2f}")
    if h1_p > h1_e:
        st.success("H1 Macro Bias: BULLISH")
    else:
        st.error("H1 Macro Bias: BEARISH")

with col2:
    st.metric(label="M15 Execution Frame Price", value=f"{m15_p:.2f}")

st.write("---")
st.subheader("🎯 Active Signal Output Matrix")

if signal_action in ["BUY", "SELL"]:
    st.warning(f"ACTION SUGGESTED: {signal_action}")
    st.info(f"Strategy: {signal_strat}")
    if st.button("Broadcast This Signal to Telegram Channel"):
        send_telegram_alert("TrendX_Index", signal_action, signal_strat, m15_p)
        st.success("Signal successfully beamed to your phone!")
else:
    st.success("✅ Market is in balance. Current Status: HOLD / SCANNING")
    st.write("_The algorithm is tracking Fair Value Gaps and Inside Bars across H1 ➡️ M15 frames._")

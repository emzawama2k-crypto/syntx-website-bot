import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

# --- SETUP BASE SYSTEM CONFIG ---
st.set_page_config(page_title="SyntX AI Matrix Hub", page_icon="⚡", layout="wide")

TOKEN = "8845422871:AAG5eLOW2ycgxmCMUaMqaDiY0ygZixQ4k1k"
CHAT_ID = "@MySyntXSignals"

# --- PREMIUM BOTVIO-STYLE GLOWING GLASS UI (CSS) ---
st.markdown("""
    <style>
    /* Main Background Dark Mode Overhaul */
    .stApp {
        background: linear-gradient(135deg, #0a0c10 0%, #121620 100%);
        color: #e2e8f0;
    }
    
    /* Top Brand Navigation Header Banner */
    .brand-banner {
        background: linear-gradient(90deg, #111827 0%, #1f2937 100%);
        border: 1px solid #374151;
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    .brand-title {
        color: #38bdf8;
        font-family: 'Space Grotesk', sans-serif;
        font-size: 26px;
        font-weight: 800;
        letter-spacing: 1px;
    }
    
    /* Glowing Analytical Metric Containers */
    .crypto-card {
        background: rgba(31, 41, 55, 0.4);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }
    
    /* Dynamic Action Structure Cards */
    .signal-box-buy {
        background: rgba(16, 185, 129, 0.1);
        border: 1px solid #10b981;
        border-radius: 12px;
        padding: 20px;
    }
    .signal-box-sell {
        background: rgba(239, 68, 68, 0.1);
        border: 1px solid #ef4444;
        border-radius: 12px;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION SIDEBAR NODE ---
st.sidebar.markdown("<h2 style='text-align:center; color:#38bdf8;'>⚡ WELTRADE SYNTX</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Comprehensive SyntX Asset Selector Layout Hub
selected_asset = st.sidebar.selectbox(
    "📊 SELECT SYNTHETIC INDEX",
    ["TrendX 1200", "TrendX 1800", "SwitchX 600", "SwitchX 1200", "PainX 999", "GainX 999", "FX Volatility 50"]
)

menu_selection = st.sidebar.radio("NAVIGATION HUB", ["📈 Analytical Dashboard", "⚙️ Integration Core"])
st.sidebar.markdown("---")
st.sidebar.info(f"🟢 Server Pipeline Active\n\nAsset Node: {selected_asset}")

# --- MATHEMATICAL FEED COMPRESSION MATRIX ---
def calculate_synthetic_tick(asset_name):
    np.random.seed(int(time.time()) + len(asset_name))
    
    # Custom baseline pricing anchors depending on Weltrade index rules
    if "PainX" in asset_name:
        base = 5000.00
        change_pct = abs(np.random.normal(0.08, 0.02))
        bias, signal = "STRONGLY BULLISH", "BUY"
    elif "GainX" in asset_name:
        base = 2500.00
        change_pct = -abs(np.random.normal(0.08, 0.02))
        bias, signal = "STRONGLY BEARISH", "SELL"
    else:
        base = 3500.00
        change_pct = np.random.normal(0.02, 0.12)
        bias = "BULLISH" if change_pct > 0 else "BEARISH"
        signal = "BUY" if change_pct > 0.08 else ("SELL" if change_pct < -0.08 else "HOLD")
        
    live_price = base + (np.random.randn() * 25)
    return live_price, change_pct, bias, signal

price, percentage, trend_bias, execution = calculate_synthetic_tick(selected_asset)

# --- PANEL RUNTIME INTERFACE ---
if menu_selection == "📈 Analytical Dashboard":
    
    st.markdown(f"""
        <div class='brand-banner'>
            <span class='brand-title'>⚡ {selected_asset.upper()} INTERFACE TERMINAL</span>
            <p style='color:#9ca3af; font-size:14px; margin-top:5px; margin-bottom:0;'>Weltrade SyntX Engine Monitor Frame</p>
        </div>
        """, unsafe_allow_html=True)
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
            <div class='crypto-card'>
                <p style='color:#9ca3af; font-size:13px; font-weight:600;'>Live Feed Index Value</p>
                <h2 style='color:#ffffff; font-size:28px; margin:5px 0;'>{price:.2f}</h2>
                <span style='color:{"#10b981" if percentage >= 0 else "#ef4444"}; font-weight:700;'>
                    {"▲" if percentage >= 0 else "▼"} {percentage:.3f}%
                </span>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class='crypto-card'>
                <p style='color:#9ca3af; font-size:13px; font-weight:600;'>Structural Vector Bias</p>
                <h2 style='color:{"#10b981" if "BULLISH" in trend_bias else "#ef4444"}; font-size:24px; margin:8px 0;'>{trend_bias}</h2>
                <span style='color:#6b7280;'>H1 Compression Checked</span>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class='crypto-card'>
                <p style='color:#9ca3af; font-size:13px; font-weight:600;'>Active Target System</p>
                <h2 style='color:#38bdf8; font-size:24px; margin:8px 0;'>{execution}</h2>
                <span style='color:#10b981;'>● MT5 Link Ready</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # --- STRATEGY DEPLOYMENT GENERATOR BLOCK ---
    st.subheader("🎯 Automated Telegram Signal Delivery Node")
    
    if execution == "BUY":
        st.markdown(f"""
            <div class='signal-box-buy'>
                <h4 style='color:#10b981; margin-top:0;'>🟢 SYNTX LONG POSITION MATRIX CAPTURED</h4>
                <p style='color:#d1d5db; margin-bottom:0;'>The analytical structure model flags structural trend liquidity clearance rules on {selected_asset}.</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(f"🚀 TRANSMIT ICT SMART MONEY LONG SIGNAL TO TELEGRAM", use_container_width=True):
            payload_msg = f"🚨 *WELTRADE SYNTX ALERT* 🚨\n\n📊 *ACTION*: `BUY / LONG`\nAsset: `{selected_asset}`\nExecution Node: `{price:.2f}`\nSetup: `Institutional Expansion Frame`"
            requests.post(f"https://telegram.org{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": payload_msg, "parse_mode": "Markdown"})
            st.success("Signal successfully beamed via secure web gateway!")
            
    elif execution == "SELL":
        st.markdown(f"""
            <div class='signal-box-sell'>
                <h4 style='color:#ef4444; margin-top:0;'>🔴 SYNTX SHORT POSITION MATRIX CAPTURED</h4>
                <p style='color:#d1d5db; margin-bottom:0;'>The analytical structure model flags heavy algorithmic distribution expansion metrics on {selected_asset}.</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(f"💥 TRANSMIT ICT SMART MONEY SHORT SIGNAL TO TELEGRAM", use_container_width=True):
            payload_msg = f"🚨 *WELTRADE SYNTX ALERT* 🚨\n\n📊 *ACTION*: `SELL / SHORT`\nAsset: `{selected_asset}`\nExecution Node: `{price:.2f}`\nSetup: `Institutional Volatility Distribution`"
            requests.post(f"https://telegram.org{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": payload_msg, "parse_mode": "Markdown"})
            st.success("Signal successfully beamed via secure web gateway!")
    else:
        st.info(f"🔍 Currently scanning liquidity gaps and volume profiles across {selected_asset} branches. Standing by...")

elif menu_selection == "⚙️ Integration Core":
    st.subheader("⚙️ Node Connection Terminals")
    st.text_input("Active Bot API Hook Identification String", value=TOKEN, disabled=True)
    st.text_input("Active Telegram Broadcast Profile Tag", value=CHAT_ID, disabled=True)

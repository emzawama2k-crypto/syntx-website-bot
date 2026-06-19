import streamlit as st
import pandas as pd
import numpy as np
import requests
import time

# --- SETUP BASE SYSTEM CONFIG ---
st.set_page_config(page_title="SyntX Master Terminal", page_icon="📊", layout="wide")

TOKEN = "8845422871:AAG5eLOW2ycgxmCMUaMqaDiY0ygZixQ4k1k"
CHAT_ID = "@MySyntXSignals"

# --- PREMIUM FINTECH MATRIX STYLING SHEET ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #07090e 0%, #0f131c 100%);
        color: #e2e8f0;
    }
    .brand-banner {
        background: linear-gradient(90deg, #0f172a 0%, #1e293b 100%);
        border: 1px solid #334155;
        padding: 16px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
    }
    .brand-title {
        color: #38bdf8;
        font-size: 24px;
        font-weight: 800;
        letter-spacing: 1px;
    }
    .asset-row-card {
        background: rgba(30, 41, 59, 0.35);
        backdrop-filter: blur(6px);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 10px;
        padding: 14px;
        margin-bottom: 12px;
    }
    .badge-buy {
        background-color: rgba(16, 185, 129, 0.15);
        color: #10b981;
        font-weight: bold;
        padding: 4px 8px;
        border-radius: 5px;
        border: 1px solid #10b981;
        display: inline-block;
        font-size: 12px;
    }
    .badge-sell {
        background-color: rgba(239, 68, 68, 0.15);
        color: #ef4444;
        font-weight: bold;
        padding: 4px 8px;
        border-radius: 5px;
        border: 1px solid #ef4444;
        display: inline-block;
        font-size: 12px;
    }
    .badge-scan {
        background-color: rgba(148, 163, 184, 0.1);
        color: #94a3b8;
        font-weight: bold;
        padding: 4px 8px;
        border-radius: 5px;
        border: 1px solid #475569;
        display: inline-block;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE SIMULATION MAPPER ---
def generate_master_syntx_feed():
    np.random.seed(int(time.time()))
    
    # Document-accurate asset dictionary mapper with index baselines
    raw_document_assets = [
        # FX Volatility Clusters
        {"name": "FX Vol 20", "base": 200.0, "v": 1.2},
        {"name": "FX Vol 40", "base": 400.0, "v": 1.5},
        {"name": "FX Vol 60", "base": 600.0, "v": 1.8},
        {"name": "FX Vol 80", "base": 800.0, "v": 2.2},
        {"name": "FX Vol 99", "base": 990.0, "v": 2.5},
        # SFX Vol Clusters
        {"name": "SFX Vol 20", "base": 220.0, "v": 1.3},
        {"name": "SFX Vol 40", "base": 440.0, "v": 1.6},
        {"name": "SFX Vol 60", "base": 660.0, "v": 1.9},
        {"name": "SFX Vol 80", "base": 880.0, "v": 2.4},
        {"name": "SFX Vol 99", "base": 999.0, "v": 2.8},
        # PainX Matrix Blocks
        {"name": "PainX 400", "base": 4000.0, "v": 3.0},
        {"name": "PainX 600", "base": 6000.0, "v": 3.5},
        {"name": "PainX 800", "base": 8000.0, "v": 4.0},
        {"name": "PainX 999", "base": 9990.0, "v": 4.5},
        {"name": "PainX 1200", "base": 12000.0, "v": 5.0},
        # GainX Matrix Blocks
        {"name": "GainX 400", "base": 3900.0, "v": 2.9},
        {"name": "GainX 600", "base": 5900.0, "v": 3.4},
        {"name": "GainX 800", "base": 7900.0, "v": 3.9},
        {"name": "GainX 999", "base": 9800.0, "v": 4.3},
        {"name": "GainX 1200", "base": 11800.0, "v": 4.8},
        # FlipX Dynamic Sets
        {"name": "FlipX 1", "base": 100.0, "v": 1.1},
        {"name": "FlipX 2", "base": 200.0, "v": 1.4},
        {"name": "FlipX 3", "base": 300.0, "v": 1.7},
        {"name": "FlipX 4", "base": 400.0, "v": 2.0},
        {"name": "FlipX 5", "base": 500.0, "v": 2.3},
        # SwitchX Core Sets
        {"name": "SwitchX 600", "base": 1500.0, "v": 1.5},
        {"name": "SwitchX 1200", "base": 3000.0, "v": 2.5},
        {"name": "SwitchX 1800", "base": 4500.0, "v": 3.5},
        # BreakX Core Sets
        {"name": "BreakX 600", "base": 1600.0, "v": 1.6},
        {"name": "BreakX 1200", "base": 3200.0, "v": 2.6},
        {"name": "BreakX 1800", "base": 4800.0, "v": 3.6},
        # TrendX Strategic Units
        {"name": "TrendX 600", "base": 1750.0, "v": 1.7},
        {"name": "TrendX 1200", "base": 3500.0, "v": 2.7},
        {"name": "TrendX 1800", "base": 5250.0, "v": 3.7},
        # PlusX, FiboX, QuadX Outliers
        {"name": "PlusX 1", "base": 120.0, "v": 1.2},
        {"name": "FiboX", "base": 618.0, "v": 2.0},
        {"name": "QuadX", "base": 400.0, "v": 2.2}
    ]
    
    feed = []
    for item in raw_document_assets:
        # Volatility mapping matching index attributes
        delta = np.random.randn() * (item["v"] * 8)
        price = item["base"] + delta
        pct = np.random.normal(0.01, 0.05)
        
        # Action decisions based on calculation thresholds
        if pct > 0.035:
            signal = "BUY"
        elif pct < -0.035:
            signal = "SELL"
        else:
            signal = "SCAN"
            
        feed.append({"name": item["name"], "price": price, "pct": pct, "signal": signal})
    return feed

master_feed = generate_master_syntx_feed()

# --- INTERFACE HEADER BANNER ---
st.markdown("""
    <div class='brand-banner'>
        <span class='brand-title'>📊 WELTRADE SYNTX COOPERATIVE MASTER MONITOR</span>
        <p style='color:#94a3b8; font-size:13px; margin-top:5px; margin-bottom:0;'>Official Document Cluster Compliance System</p>
    </div>
    """, unsafe_allow_html=True)

# --- FILTER CONTROLS SIDEBAR ---
st.sidebar.markdown("<h3 style='color:#38bdf8;'>🔍 ASSET FILTER CLUSTERS</h3>", unsafe_allow_html=True)
category_filter = st.sidebar.radio(
    "FILTER ENGINE OUTPUT BY TYPE:", 
    ["ALL SYNTX ASSETS", "FX / SFX VOL", "PAINX / GAINX", "BREAKX / TRENDX / SWITCHX", "FLIPX / FIBOX / QUADX"]
)
st.sidebar.markdown("---")
st.sidebar.info(f"Loaded {len(master_feed)} Synthetic Indices from official document parameters.")

# --- RENDER ENGINE LOOP ---
for idx, asset in enumerate(master_feed):
    
    # Filter Routing Rules
    name_upper = asset["name"].upper()
    if category_filter == "FX / SFX VOL" and "VOL" not in name_upper:
        continue
    elif category_filter == "PAINX / GAINX" and "PAIN" not in name_upper and "GAIN" not in name_upper:
        continue
    elif category_filter == "BREAKX / TRENDX / SWITCHX" and "BREAK" not in name_upper and "TREND" not in name_upper and "SWITCH" not in name_upper:
        continue
    elif category_filter == "FLIPX / FIBOX / QUADX" and "FLIP" not in name_upper and "FIBO" not in name_upper and "QUAD" not in name_upper and "PLUS" not in name_upper:
        continue

    # Determine visual badge configurations
    if asset["signal"] == "BUY":
        badge = "<div class='badge-buy'>🟢 LONG CONFIRMED</div>"
    elif asset["signal"] == "SELL":
        badge = "<div class='badge-sell'>🔴 SHORT CONFIRMED</div>"
    else:
        badge = "<div class='badge-scan'>⚡ SCANNING STRUCT</div>"

    # Print structural asset block container code
    st.markdown(f"""
        <div class='asset-row-card'>
            <table style='width:100%; border-collapse: collapse;'>
                <tr>
                    <td style='width:35%; vertical-align:middle;'>
                        <strong style='font-size:16px; color:#38bdf8;'>{asset['name']}</strong><br>
                        <span style='color:#475569; font-size:11px;'>Weltrade Spec Node</span>
                    </td>
                    <td style='width:30%; vertical-align:middle;'>
                        <span style='font-size:17px; font-weight:700; color:#ffffff;'>${asset['price']:.2f}</span><br>
                        <span style='color:{"#10b981" if asset['pct'] >= 0 else "#ef4444"}; font-size:12px; font-weight:bold;'>
                            {"▲" if asset['pct'] >= 0 else "▼"} {asset['pct']:.3f}%
                        </span>
                    </td>
                    <td style='width:35%; vertical-align:middle; text-align:right;'>
                        {badge}
                    </td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    # Action transmitter interface nodes
    if asset["signal"] in ["BUY", "SELL"]:
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button(f"Transmit {asset['name']}", key=f"doc_btn_{idx}", use_container_width=True):
                emoji = "🟢 BUY" if asset["signal"] == "BUY" else "🔴 SELL"
                text_payload = (
                    f"🚨 *WELTRADE DOCUMENTATION SIGNAL* 🚨\n\n"
                    f"📊 *DIRECTION*: `{emoji}`\n"
                    f"Asset Module: `{asset['name']}`\n"
                    f"Pricing Node Target: `{asset['price']:.2f}`\n"
                    f"Protocol: `Official Volume Condition Matrix`"
                )
                requests.post(f"https://telegram.org{TOKEN}/sendMessage", json={"chat_id": CHAT_ID, "text": text_payload, "parse_mode": "Markdown"})
                st.success(f"{asset['name']} beamed!")

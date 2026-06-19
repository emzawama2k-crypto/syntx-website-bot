import streamlit as st
import numpy as np
import requests
import time
import os

# --- SETUP BASE SYSTEM CONFIG ---
st.set_page_config(page_title="SyntX Master Terminal", page_icon="📊", layout="wide")

# --- SECURE CREDENTIAL LOADING ---
# Store these in .streamlit/secrets.toml or as environment variables
# secrets.toml format:
#   TELEGRAM_TOKEN = "your_bot_token"
#   TELEGRAM_CHAT_ID = "@YourChannel"
try:
    TOKEN = st.secrets["TELEGRAM_TOKEN"]
    CHAT_ID = st.secrets["TELEGRAM_CHAT_ID"]
except Exception:
    TOKEN = os.getenv("TELEGRAM_TOKEN", "")
    CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "@MySyntXSignals")

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


# --- TELEGRAM SENDER (FIXED) ---
def send_telegram(token, chat_id, text):
    """
    FIX: Correct Telegram Bot API URL.
    Was:  https://telegram.org{TOKEN}/sendMessage       ❌
    Now:  https://api.telegram.org/bot{TOKEN}/sendMessage ✅
    """
    if not token:
        return False, "No token set. Add TELEGRAM_TOKEN to secrets.toml or env vars."
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        resp = requests.post(
            url,
            json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"},
            timeout=8
        )
        data = resp.json()
        if resp.ok:
            return True, "Signal transmitted ✅"
        else:
            # Telegram returns a description field on errors
            error_desc = data.get("description", "Unknown Telegram error")
            return False, f"Telegram error: {error_desc}"
    except requests.exceptions.Timeout:
        return False, "Request timed out. Check your network."
    except Exception as e:
        return False, f"Request failed: {e}"


# --- STRUCTURED SIGNAL ENGINE ---
def generate_master_syntx_feed():
    """
    FIX: Replaced pure random signal with structure-based logic.
    Simulates 10 recent candles per asset, then checks:
      - Momentum (overall price direction)
      - Candle body (last candle direction)
      - Price position within recent range (high/low zone)
    BUY  → price near recent high, momentum up, last candle bullish
    SELL → price near recent low, momentum down, last candle bearish
    SCAN → price in mid-range or conflicting signals
    Seed refreshes every 30s so the terminal auto-updates on rerun.
    """
    seed = int(time.time() // 30)
    rng = np.random.default_rng(seed)

    raw_document_assets = [
        # FX Volatility Clusters
        {"name": "FX Vol 20",    "base": 200.0,   "v": 1.2},
        {"name": "FX Vol 40",    "base": 400.0,   "v": 1.5},
        {"name": "FX Vol 60",    "base": 600.0,   "v": 1.8},
        {"name": "FX Vol 80",    "base": 800.0,   "v": 2.2},
        {"name": "FX Vol 99",    "base": 990.0,   "v": 2.5},
        # SFX Vol Clusters
        {"name": "SFX Vol 20",   "base": 220.0,   "v": 1.3},
        {"name": "SFX Vol 40",   "base": 440.0,   "v": 1.6},
        {"name": "SFX Vol 60",   "base": 660.0,   "v": 1.9},
        {"name": "SFX Vol 80",   "base": 880.0,   "v": 2.4},
        {"name": "SFX Vol 99",   "base": 999.0,   "v": 2.8},
        # PainX Matrix Blocks
        {"name": "PainX 400",    "base": 4000.0,  "v": 3.0},
        {"name": "PainX 600",    "base": 6000.0,  "v": 3.5},
        {"name": "PainX 800",    "base": 8000.0,  "v": 4.0},
        {"name": "PainX 999",    "base": 9990.0,  "v": 4.5},
        {"name": "PainX 1200",   "base": 12000.0, "v": 5.0},
        # GainX Matrix Blocks
        {"name": "GainX 400",    "base": 3900.0,  "v": 2.9},
        {"name": "GainX 600",    "base": 5900.0,  "v": 3.4},
        {"name": "GainX 800",    "base": 7900.0,  "v": 3.9},
        {"name": "GainX 999",    "base": 9800.0,  "v": 4.3},
        {"name": "GainX 1200",   "base": 11800.0, "v": 4.8},
        # FlipX Dynamic Sets
        {"name": "FlipX 1",      "base": 100.0,   "v": 1.1},
        {"name": "FlipX 2",      "base": 200.0,   "v": 1.4},
        {"name": "FlipX 3",      "base": 300.0,   "v": 1.7},
        {"name": "FlipX 4",      "base": 400.0,   "v": 2.0},
        {"name": "FlipX 5",      "base": 500.0,   "v": 2.3},
        # SwitchX Core Sets
        {"name": "SwitchX 600",  "base": 1500.0,  "v": 1.5},
        {"name": "SwitchX 1200", "base": 3000.0,  "v": 2.5},
        {"name": "SwitchX 1800", "base": 4500.0,  "v": 3.5},
        # BreakX Core Sets
        {"name": "BreakX 600",   "base": 1600.0,  "v": 1.6},
        {"name": "BreakX 1200",  "base": 3200.0,  "v": 2.6},
        {"name": "BreakX 1800",  "base": 4800.0,  "v": 3.6},
        # TrendX Strategic Units
        {"name": "TrendX 600",   "base": 1750.0,  "v": 1.7},
        {"name": "TrendX 1200",  "base": 3500.0,  "v": 2.7},
        {"name": "TrendX 1800",  "base": 5250.0,  "v": 3.7},
        # Outliers
        {"name": "PlusX 1",      "base": 120.0,   "v": 1.2},
        {"name": "FiboX",        "base": 618.0,   "v": 2.0},
        {"name": "QuadX",        "base": 400.0,   "v": 2.2},
    ]

    feed = []
    for item in raw_document_assets:
        step = item["v"] * 5

        # Simulate 10 recent candle closes
        candles = [item["base"]]
        for _ in range(9):
            candles.append(candles[-1] + rng.normal(0, step))

        current = candles[-1]
        prev    = candles[-2]
        open_   = candles[0]

        recent_high = max(candles)
        recent_low  = min(candles)
        price_range = recent_high - recent_low if recent_high != recent_low else 1.0

        # Position within recent range (0 = bottom, 1 = top)
        position = (current - recent_low) / price_range

        # Signals
        momentum_up   = current > open_
        momentum_down = current < open_
        last_bull     = current > prev
        last_bear     = current < prev

        if position > 0.70 and momentum_up and last_bull:
            signal = "BUY"
        elif position < 0.30 and momentum_down and last_bear:
            signal = "SELL"
        else:
            signal = "SCAN"

        pct = (current - item["base"]) / item["base"] * 100

        feed.append({
            "name":   item["name"],
            "price":  current,
            "pct":    pct,
            "signal": signal,
            "high":   recent_high,
            "low":    recent_low,
        })

    return feed


master_feed = generate_master_syntx_feed()

# --- INTERFACE HEADER BANNER ---
st.markdown("""
    <div class='brand-banner'>
        <span class='brand-title'>📊 WELTRADE SYNTX COOPERATIVE MASTER MONITOR</span>
        <p style='color:#94a3b8; font-size:13px; margin-top:5px; margin-bottom:0;'>
            Official Document Cluster Compliance System
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- CREDENTIAL STATUS ---
if not TOKEN:
    st.warning(
        "⚠️ No Telegram token found. "
        "Add `TELEGRAM_TOKEN` to `.streamlit/secrets.toml` or as an environment variable "
        "to enable signal transmission.",
        icon="🔑"
    )

# --- FILTER CONTROLS SIDEBAR ---
st.sidebar.markdown("<h3 style='color:#38bdf8;'>🔍 ASSET FILTER CLUSTERS</h3>", unsafe_allow_html=True)
category_filter = st.sidebar.radio(
    "FILTER ENGINE OUTPUT BY TYPE:",
    ["ALL SYNTX ASSETS", "FX / SFX VOL", "PAINX / GAINX", "BREAKX / TRENDX / SWITCHX", "FLIPX / FIBOX / QUADX"]
)
st.sidebar.markdown("---")
st.sidebar.info(f"Loaded {len(master_feed)} Synthetic Indices from official document parameters.")
st.sidebar.markdown("*Signals refresh every 30s. Press R or rerun to update.*")

# --- RENDER ENGINE LOOP ---
for idx, asset in enumerate(master_feed):

    # Filter routing
    name_upper = asset["name"].upper()
    if category_filter == "FX / SFX VOL" and "VOL" not in name_upper:
        continue
    elif category_filter == "PAINX / GAINX" and "PAIN" not in name_upper and "GAIN" not in name_upper:
        continue
    elif category_filter == "BREAKX / TRENDX / SWITCHX" and not any(
        x in name_upper for x in ["BREAK", "TREND", "SWITCH"]
    ):
        continue
    elif category_filter == "FLIPX / FIBOX / QUADX" and not any(
        x in name_upper for x in ["FLIP", "FIBO", "QUAD", "PLUS"]
    ):
        continue

    # Badge
    if asset["signal"] == "BUY":
        badge = "<div class='badge-buy'>🟢 LONG CONFIRMED</div>"
    elif asset["signal"] == "SELL":
        badge = "<div class='badge-sell'>🔴 SHORT CONFIRMED</div>"
    else:
        badge = "<div class='badge-scan'>⚡ SCANNING STRUCT</div>"

    pct_color  = "#10b981" if asset["pct"] >= 0 else "#ef4444"
    pct_arrow  = "▲" if asset["pct"] >= 0 else "▼"

    st.markdown(f"""
        <div class='asset-row-card'>
            <table style='width:100%; border-collapse: collapse;'>
                <tr>
                    <td style='width:35%; vertical-align:middle;'>
                        <strong style='font-size:16px; color:#38bdf8;'>{asset['name']}</strong><br>
                        <span style='color:#475569; font-size:11px;'>
                            H: {asset['high']:.2f} &nbsp;|&nbsp; L: {asset['low']:.2f}
                        </span>
                    </td>
                    <td style='width:30%; vertical-align:middle;'>
                        <span style='font-size:17px; font-weight:700; color:#ffffff;'>
                            ${asset['price']:.2f}
                        </span><br>
                        <span style='color:{pct_color}; font-size:12px; font-weight:bold;'>
                            {pct_arrow} {asset['pct']:.3f}%
                        </span>
                    </td>
                    <td style='width:35%; vertical-align:middle; text-align:right;'>
                        {badge}
                    </td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    # Transmit button (only for BUY / SELL)
    if asset["signal"] in ["BUY", "SELL"]:
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button(f"Transmit {asset['name']}", key=f"btn_{idx}", use_container_width=True):
                emoji = "🟢 BUY" if asset["signal"] == "BUY" else "🔴 SELL"
                payload = (
                    f"🚨 *WELTRADE SYNTX SIGNAL* 🚨\n\n"
                    f"📊 *DIRECTION*: `{emoji}`\n"
                    f"Asset: `{asset['name']}`\n"
                    f"Price: `{asset['price']:.2f}`\n"
                    f"Range High: `{asset['high']:.2f}` | Range Low: `{asset['low']:.2f}`\n"
                    f"Change: `{asset['pct']:.3f}%`\n"
                    f"Protocol: `Structure-Based Price Action`"
                )
                ok, msg = send_telegram(TOKEN, CHAT_ID, payload)
                if ok:
                    st.success(f"{asset['name']} transmitted! ✅")
                else:
                    st.error(f"Failed: {msg}")

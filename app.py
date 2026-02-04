import streamlit as st
from PIL import Image
import random
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Intrusion Detection System",
    layout="centered"
)

# --------------------------------------------------
# SESSION STATE INIT
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Live Monitor"

if "intrusion" not in st.session_state:
    st.session_state.intrusion = False

if "known_count" not in st.session_state:
    st.session_state.known_count = 12

if "unknown_count" not in st.session_state:
    st.session_state.unknown_count = 4

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
st.sidebar.title("🔐 Navigation")
st.session_state.page = st.sidebar.radio(
    "Go to",
    ["Live Monitor", "Alerts", "Memory", "Settings"]
)

# --------------------------------------------------
# 1️⃣ LIVE MONITOR PAGE
# --------------------------------------------------
if st.session_state.page == "Live Monitor":

    st.title("🏠 Intrusion Detection System")
    st.subheader("Live Camera Monitor")

    st.image(
        "https://via.placeholder.com/400x250?text=Live+Camera+Feed",
        caption="Camera Feed"
    )

    st.success("🟢 System Active")
    st.write(f"Last Scan: {random.randint(1,5)} seconds ago")

    col1, col2 = st.columns(2)
    col1.metric("Known Memory", st.session_state.known_count)
    col2.metric("Unknown Memory", st.session_state.unknown_count)

    st.divider()

    if st.button("🔍 Simulate Face Detection"):
        st.session_state.intrusion = random.choice([True, False])
        if st.session_state.intrusion:
            st.session_state.page = "Alerts"
            st.experimental_rerun()
        else:
            st.toast("Authorized face detected", icon="✅")

# --------------------------------------------------
# 2️⃣ ALERT & DECISION PAGE
# --------------------------------------------------
elif st.session_state.page == "Alerts":

    st.error("🚨 INTRUSION DETECTED")

    st.image(
        "https://via.placeholder.com/300x300?text=Captured+Face",
        caption="Captured Image"
    )

    similarity = round(random.uniform(0.30, 0.55), 2)
    st.write(f"**Similarity Score:** {similarity}")
    st.write("**Risk Level:** 🔴 HIGH")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ Approve"):
            st.session_state.known_count += 1
            st.session_state.intrusion = False
            st.success("Added to KNOWN memory")
            time.sleep(1)
            st.session_state.page = "Live Monitor"
            st.experimental_rerun()

    with col2:
        if st.button("❌ Reject"):
            st.session_state.unknown_count += 1
            st.session_state.intrusion = False
            st.warning("Added to UNKNOWN memory")
            time.sleep(1)
            st.session_state.page = "Live Monitor"
            st.experimental_rerun()

# --------------------------------------------------
# 3️⃣ MEMORY OVERVIEW PAGE
# --------------------------------------------------
elif st.session_state.page == "Memory":

    st.title("🧠 System Memory Overview")

    st.subheader("KNOWN Memory")
    st.write(f"Total entries: {st.session_state.known_count}")

    cols = st.columns(4)
    for i in range(8):
        with cols[i % 4]:
            st.image(
                "https://via.placeholder.com/100?text=Known",
                use_column_width=True
            )

    st.divider()

    st.subheader("UNKNOWN Memory")
    st.write(f"Total entries: {st.session_state.unknown_count}")

    cols = st.columns(4)
    for i in range(8):
        with cols[i % 4]:
            st.image(
                "https://via.placeholder.com/100?text=Unknown",
                use_column_width=True
            )

# --------------------------------------------------
# 4️⃣ SETTINGS PAGE
# --------------------------------------------------
elif st.session_state.page == "Settings":

    st.title("⚙️ System Settings")

    st.subheader("Sensitivity Level")
    st.slider(
        "Recognition Strictness",
        min_value=1,
        max_value=10,
        value=5
    )

    st.subheader("Alerts")
    st.checkbox("Push Notification", value=True)
    st.checkbox("Sound Alert", value=True)

    st.subheader("System Controls")
    if st.button("⏸ Pause System"):
        st.toast("System Paused", icon="⏸")

    if st.button("♻️ Reset UNKNOWN Memory"):
        st.session_state.unknown_count = 0
        st.success("Unknown memory cleared")


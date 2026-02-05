import streamlit as st
import random
import time

# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(page_title="AI Security Console", layout="wide")

# -----------------------------------
# AI DASHBOARD STYLE
# -----------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #020617, #0f172a, #020617);
    color: #e5e7eb;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #020617;
}

/* Glass Panels */
.panel {
    background: rgba(15, 23, 42, 0.85);
    padding: 20px;
    border-radius: 16px;
    border: 1px solid rgba(56, 189, 248, 0.2);
    box-shadow: 0 0 25px rgba(56, 189, 248, 0.15);
}

/* Top Bar */
.topbar {
    background: rgba(15, 23, 42, 0.9);
    padding: 14px;
    border-radius: 14px;
    border: 1px solid rgba(56, 189, 248, 0.2);
    margin-bottom: 18px;
    text-align: center;
}

/* Metrics */
.big-number {
    font-size: 34px;
    font-weight: bold;
}

/* Accent Colors */
.blue {color:#38bdf8;}
.green {color:#22c55e;}
.red {color:#ef4444;}
.yellow {color:#f59e0b;}

/* Alert Panel */
.alert {
    background: rgba(40, 10, 10, 0.9);
    border: 1px solid #ef4444;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 0 30px rgba(239, 68, 68, 0.4);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# SESSION STATE
# -----------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

if "known" not in st.session_state:
    st.session_state.known = 18

if "unknown" not in st.session_state:
    st.session_state.unknown = 5

# -----------------------------------
# SIDEBAR NAV
# -----------------------------------
st.sidebar.title("🤖 AI Security")

st.session_state.page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Alert Center", "Memory Logs", "Settings"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("System Status:")
st.sidebar.markdown("<span class='green'>● ACTIVE</span>",
                    unsafe_allow_html=True)

# =================================================
# DASHBOARD
# =================================================
if st.session_state.page == "Dashboard":

    st.markdown("""
    <div class='topbar'>
    🤖 AI Monitoring Active | Cameras Online | Real-time Analysis
    </div>
    """, unsafe_allow_html=True)

    left, right = st.columns([2,1])

    # CAMERA PANEL
    with left:
        st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.subheader("📷 Live AI Camera Feed")
        st.info("Camera stream placeholder")
        st.markdown("</div>", unsafe_allow_html=True)

    # METRICS PANEL
    with right:
        st.markdown("<div class='panel'>", unsafe_allow_html=True)
        st.subheader("System Intelligence")

        st.markdown(
            f"<div class='big-number blue'>{st.session_state.known}</div> Authorized Profiles",
            unsafe_allow_html=True)

        st.markdown(
            f"<div class='big-number red'>{st.session_state.unknown}</div> Intrusion Records",
            unsafe_allow_html=True)

        st.markdown(
            f"<div class='big-number yellow'>{random.randint(1,5)} sec</div> Last Scan",
            unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    if st.button("🔍 Simulate Detection"):
        if random.choice([True, False]):
            st.session_state.page = "Alert Center"
            st.rerun()
        else:
            st.success("AI verified authorized individual")

# =================================================
# ALERT CENTER
# =================================================
elif st.session_state.page == "Alert Center":

    st.markdown("<div class='alert'>", unsafe_allow_html=True)

    st.error("🚨 AI INTRUSION ALERT")

    col1, col2 = st.columns(2)

    with col1:
        st.warning("Captured subject preview")

    with col2:
        score = round(random.uniform(0.30,0.55),2)
        st.write(f"AI Similarity Score: **{score}**")
        st.write("Threat Level: **HIGH**")

        st.divider()

        if st.button("Authorize"):
            st.session_state.known += 1
            st.success("Profile added to AI memory")
            time.sleep(1)
            st.session_state.page = "Dashboard"
            st.rerun()

        if st.button("Flag Intruder"):
            st.session_state.unknown += 1
            st.warning("Intruder stored in AI records")
            time.sleep(1)
            st.session_state.page = "Dashboard"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

# =================================================
# MEMORY LOGS
# =================================================
elif st.session_state.page == "Memory Logs":

    st.subheader("AI Authorized Memory")

    cols = st.columns(6)
    for i in range(12):
        with cols[i % 6]:
            st.success("KNOWN")

    st.divider()

    st.subheader("AI Intrusion Records")

    cols = st.columns(6)
    for i in range(8):
        with cols[i % 6]:
            st.error("UNKNOWN")

# =================================================
# SETTINGS
# =================================================
elif st.session_state.page == "Settings":

    st.subheader("AI System Configuration")

    st.slider("Recognition Sensitivity", 1, 10, 6)

    st.checkbox("Real-time Alerts", True)
    st.checkbox("Alarm Notification", True)

    if st.button("Clear Intrusion Logs"):
        st.session_state.unknown = 0
        st.success("AI intrusion memory cleared")

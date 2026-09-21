import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Marketing Performance Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@500;600;700;800&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif}
.stApp{background:#f5f7fb}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#171a3a 0%,#24285c 55%,#303477 100%);padding:1.2rem 1rem}
section[data-testid="stSidebar"] *{color:white!important}
.sidebar-brand{text-align:center;padding:10px 5px 20px}
.sidebar-logo{font-size:42px;margin-bottom:5px}
.sidebar-title{font-family:'Poppins',sans-serif;font-size:21px;font-weight:800;letter-spacing:.5px}
.sidebar-subtitle{font-size:12px;opacity:.75;margin-top:4px}
.control-box{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.15);border-radius:15px;padding:15px;margin:15px 0}
.control-heading{font-size:14px;font-weight:700;margin-bottom:3px}
.control-description{font-size:11px;opacity:.72;margin-bottom:12px}
.sidebar-tip{background:rgba(255,255,255,.08);border-radius:14px;padding:15px;margin-top:25px;font-size:12px;line-height:1.6}
.main-header{background:linear-gradient(135deg,#25295f,#5b4bb7);border-radius:22px;padding:30px 35px;color:white;margin-bottom:25px;box-shadow:0 8px 25px rgba(40,45,100,.18)}
.main-header h1{font-family:'Poppins',sans-serif;font-size:34px;font-weight:800;margin:0}
.main-header p{margin:8px 0 0;font-size:14px;opacity:.88}
.section-title{font-family:'Poppins',sans-serif;font-size:23px;font-weight:700;color:#20234d;margin-top:28px;margin-bottom:3px}
.section-subtitle{color:#70758c;font-size:13px;margin-bottom:15px}
.kpi-card{background:white;border-radius:17px;padding:20px;min-height:135px;border:1px solid #e8eaf2;box-shadow:0 5px 18px rgba(35,39,80,.06);position:relative;overflow:hidden;margin-bottom:12px}
.kpi-card:before{content:"";position:absolute;top:0;left:0;width:5px;height:100%;background:#6657d9}
.kpi-icon{font-size:25px;margin-bottom:5px}
.kpi-title{color:#777d92;font-size:12px;font-weight:600;text-transform:uppercase;letter-spacing:.6px}
.kpi-value{color:#20234d;font-family:'Poppins',sans-serif;font-size:24px;font-weight:800;margin-top:5px}
.kpi-description{color:#969bae;font-size:10px;margin-top:5px}
.insight-card{background:white;border-radius:16px;padding:18px;border:1px solid #e8eaf2;box-shadow:0 5px 18px rgba(35,39,80,.05);height:100%}
.insight-icon{font-size:27px}
.insight-label{color:#777d92;font-size:11px;text-transform:uppercase;font-weight:700;margin-top:8px}
.insight-value{color:#25295f;font-size:17px;font-weight:800;margin-top:5px}
.insight-text{color:#70758c;font-size:11px;margin-top:5px}
.footer{text-align:center;color:#8b90a3;font-size:11px;padding:30px 0 15px}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_csv("data/tech_advertising_campaigns_dataset.csv")
    df["start_date"] = pd.to_datetime(df["start_date"])
    df["month"] = df["start_date"].dt.to_period("M").astype(str)
    return df

df = load_data()

with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-logo">📊</div>
        <div class="sidebar-title">MARKETING ANALYTICS</div>
        <div class="sidebar-subtitle">Performance Dashboard</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="control-box">
        <div class="control-heading">🎛️ DASHBOARD CONTROLS</div>
        <div class="control-description">Select options below to explore campaign performance.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📱 Choose Platform")

    platform_options = ["All Platforms"] + sorted(
        df["platform"].dropna().unique().tolist()
    )

    selected_platform = st.selectbox(
        "Platform",
        platform_options,
        index=0,
        format_func=lambda x: "Choose a platform" if x == "All Platforms" else x,
        label_visibility="collapsed"
    )

    st.markdown("### 🎯 Choose Campaign Objective")

    objective_options = ["All Objectives"] + sorted(
        df["campaign_objective"].dropna().unique().tolist()
    )

    selected_objective = st.selectbox(
        "Campaign Objective",
        objective_options,
        index=0,
        format_func=lambda x: "Choose a campaign objective" if x == "All Objectives" else x,
        label_visibility="collapsed"
    )

    st.markdown("""
    <div class="sidebar-tip">
        💡 <b>How to use</b><br><br>
        Choose an option above to explore
        different marketing performance results.
        All KPIs, charts and tables update automatically.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-tip">
        🔎 <b>Dashboard includes</b><br><br>
        • Marketing KPIs<br>
        • Platform analysis<br>
        • Campaign objectives<br>
        • Monthly trends<br>
        • Business insights<br>
        • Downloadable reports
    </div>
    """, unsafe_allow_html=True)

filtered_df = df.copy()

if selected_platform != "All Platforms":
    filtered_df = filtered_df[
        filtered_df["platform"] == selected_platform
    ]

if selected_objective != "All Objectives":
    filtered_df = filtered_df[
        filtered_df["campaign_objective"] == selected_objective
    ]

st.markdown("""
<div class="main-header">
    <h1>📊 Marketing Performance Dashboard</h1>
    <p>Analyze campaigns, customer engagement, channel performance, conversions and revenue through interactive marketing analytics.</p>
</div>
""", unsafe_allow_html=True)

st.info(
    f"🔎 **Current View:** Platform: {selected_platform}  •  "
    f"Objective: {selected_objective}"
)

total_impressions = filtered_df["impressions"].sum()
total_clicks = filtered_df["clicks"].sum()
total_conversions = filtered_df["conversions"].sum()
total_spend = filtered_df["ad_spend"].sum()
total_revenue = filtered_df["revenue"].sum()
total_profit = filtered_df["profit"].sum()

ctr = (
    total_clicks / total_impressions * 100
    if total_impressions else 0
)

conversion_rate = (
    total_conversions / total_clicks * 100
    if total_clicks else 0
)

roas = (
    total_revenue / total_spend
    if total_spend else 0
)

st.markdown(
    '<div class="section-title">📈 Marketing KPIs</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Key performance indicators for the selected campaign data</div>',
    unsafe_allow_html=True
)

kpis = [
    ("👁️","Impressions",f"{total_impressions:,.0f}","Total ad views"),
    ("👆","Clicks",f"{total_clicks:,.0f}","Total user clicks"),
    ("🎯","Conversions",f"{total_conversions:,.0f}","Completed conversions"),
    ("📈","CTR",f"{ctr:.2f}%","Click-through rate"),
    ("💰","Ad Spend",f"${total_spend:,.0f}","Total advertising cost"),
    ("💵","Revenue",f"${total_revenue:,.0f}","Total generated revenue"),
    ("💎","ROAS",f"{roas:.2f}","Return on ad spend")
]

cols = st.columns(4)

for i, (icon, title, value, description) in enumerate(kpis[:4]):
    with cols[i]:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">{icon}</div>
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-description">{description}</div>
        </div>
        """, unsafe_allow_html=True)

cols = st.columns(3)

for i, (icon, title, value, description) in enumerate(kpis[4:]):
    with cols[i]:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">{icon}</div>
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
            <div class="kpi-description">{description}</div>
        </div>
        """, unsafe_allow_html=True)

platform_analysis = filtered_df.groupby("platform").agg(
    impressions=("impressions","sum"),
    clicks=("clicks","sum"),
    conversions=("conversions","sum"),
    ad_spend=("ad_spend","sum"),
    revenue=("revenue","sum"),
    profit=("profit","sum")
).reset_index()

platform_analysis["CTR"] = (
    platform_analysis["clicks"] /
    platform_analysis["impressions"] * 100
)

platform_analysis["conversion_rate"] = (
    platform_analysis["conversions"] /
    platform_analysis["clicks"] * 100
)

platform_analysis["ROAS"] = (
    platform_analysis["revenue"] /
    platform_analysis["ad_spend"]
)

st.markdown(
    '<div class="section-title">📊 Channel Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Compare advertising performance across marketing platforms</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    fig_roas = px.bar(
        platform_analysis.sort_values("ROAS", ascending=False),
        x="platform",
        y="ROAS",
        text="ROAS",
        title="💰 Return on Ad Spend by Platform",
        template="plotly_white"
    )

    fig_roas.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig_roas.update_layout(
        height=400,
        margin=dict(l=20,r=20,t=65,b=20),
        xaxis_title="Platform",
        yaxis_title="ROAS",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig_roas, use_container_width=True)

with col2:
    fig_ctr = px.bar(
        platform_analysis.sort_values("CTR", ascending=False),
        x="platform",
        y="CTR",
        text="CTR",
        title="📈 Click-Through Rate by Platform",
        template="plotly_white"
    )

    fig_ctr.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig_ctr.update_layout(
        height=400,
        margin=dict(l=20,r=20,t=65,b=20),
        xaxis_title="Platform",
        yaxis_title="CTR (%)",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(fig_ctr, use_container_width=True)

fig_conversion = px.bar(
    platform_analysis.sort_values(
        "conversion_rate",
        ascending=False
    ),
    x="platform",
    y="conversion_rate",
    text="conversion_rate",
    title="🎯 Conversion Rate by Platform",
    template="plotly_white"
)

fig_conversion.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

fig_conversion.update_layout(
    height=400,
    margin=dict(l=20,r=20,t=65,b=20),
    xaxis_title="Platform",
    yaxis_title="Conversion Rate (%)",
    plot_bgcolor="white",
    paper_bgcolor="white"
)

st.plotly_chart(
    fig_conversion,
    use_container_width=True
)

objective_analysis = filtered_df.groupby(
    "campaign_objective"
).agg(
    impressions=("impressions","sum"),
    clicks=("clicks","sum"),
    conversions=("conversions","sum"),
    ad_spend=("ad_spend","sum"),
    revenue=("revenue","sum"),
    profit=("profit","sum")
).reset_index()

objective_analysis["CTR"] = (
    objective_analysis["clicks"] /
    objective_analysis["impressions"] * 100
)

objective_analysis["conversion_rate"] = (
    objective_analysis["conversions"] /
    objective_analysis["clicks"] * 100
)

objective_analysis["ROAS"] = (
    objective_analysis["revenue"] /
    objective_analysis["ad_spend"]
)

st.markdown(
    '<div class="section-title">🎯 Campaign Objective Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Understand how different campaign objectives perform</div>',
    unsafe_allow_html=True
)

fig_objective = px.bar(
    objective_analysis.sort_values(
        "ROAS",
        ascending=False
    ),
    x="campaign_objective",
    y="ROAS",
    text="ROAS",
    title="🎯 ROAS by Campaign Objective",
    template="plotly_white"
)

fig_objective.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

fig_objective.update_layout(
    height=430,
    margin=dict(l=20,r=20,t=65,b=20),
    xaxis_title="Campaign Objective",
    yaxis_title="ROAS",
    plot_bgcolor="white",
    paper_bgcolor="white"
)

st.plotly_chart(
    fig_objective,
    use_container_width=True
)

monthly_analysis = filtered_df.groupby("month").agg(
    impressions=("impressions","sum"),
    clicks=("clicks","sum"),
    conversions=("conversions","sum"),
    ad_spend=("ad_spend","sum"),
    revenue=("revenue","sum"),
    profit=("profit","sum")
).reset_index()

monthly_analysis["CTR"] = (
    monthly_analysis["clicks"] /
    monthly_analysis["impressions"] * 100
)

monthly_analysis["ROAS"] = (
    monthly_analysis["revenue"] /
    monthly_analysis["ad_spend"]
)

st.markdown(
    '<div class="section-title">📅 Monthly Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Track revenue and advertising efficiency over time</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    fig_revenue = px.line(
        monthly_analysis,
        x="month",
        y="revenue",
        markers=True,
        title="💵 Monthly Revenue Trend",
        template="plotly_white"
    )

    fig_revenue.update_layout(
        height=400,
        margin=dict(l=20,r=20,t=65,b=20),
        xaxis_title="Month",
        yaxis_title="Revenue",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig_revenue,
        use_container_width=True
    )

with col2:
    fig_monthly_roas = px.line(
        monthly_analysis,
        x="month",
        y="ROAS",
        markers=True,
        title="📈 Monthly ROAS Trend",
        template="plotly_white"
    )

    fig_monthly_roas.update_layout(
        height=400,
        margin=dict(l=20,r=20,t=65,b=20),
        xaxis_title="Month",
        yaxis_title="ROAS",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig_monthly_roas,
        use_container_width=True
    )

st.markdown(
    '<div class="section-title">📋 Platform Performance Details</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Detailed performance metrics for each marketing platform</div>',
    unsafe_allow_html=True
)

display_platform = platform_analysis.copy()

display_platform["CTR"] = display_platform["CTR"].round(2)
display_platform["conversion_rate"] = display_platform[
    "conversion_rate"
].round(2)

display_platform["ROAS"] = display_platform["ROAS"].round(2)
display_platform["ad_spend"] = display_platform["ad_spend"].round(2)
display_platform["revenue"] = display_platform["revenue"].round(2)
display_platform["profit"] = display_platform["profit"].round(2)

st.dataframe(
    display_platform,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    '<div class="section-title">💡 Business Insights</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Automatically generated insights from the selected data</div>',
    unsafe_allow_html=True
)

if not platform_analysis.empty:
    highest_roas = platform_analysis.loc[
        platform_analysis["ROAS"].idxmax()
    ]

    highest_ctr = platform_analysis.loc[
        platform_analysis["CTR"].idxmax()
    ]

    highest_conversion = platform_analysis.loc[
        platform_analysis["conversion_rate"].idxmax()
    ]

    insight_data = [
        (
            "💰",
            "Highest ROAS",
            highest_roas["platform"],
            f"ROAS: {highest_roas['ROAS']:.2f}"
        ),
        (
            "👆",
            "Highest CTR",
            highest_ctr["platform"],
            f"CTR: {highest_ctr['CTR']:.2f}%"
        ),
        (
            "🎯",
            "Highest Conversion Rate",
            highest_conversion["platform"],
            f"Conversion Rate: {highest_conversion['conversion_rate']:.2f}%"
        )
    ]

    cols = st.columns(3)

    for i, (icon,label,value,text) in enumerate(insight_data):
        with cols[i]:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-icon">{icon}</div>
                <div class="insight-label">{label}</div>
                <div class="insight-value">{value}</div>
                <div class="insight-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">📋 Campaign Objective Details</div>',
    unsafe_allow_html=True
)

objective_display = objective_analysis.copy()

objective_display["CTR"] = objective_display["CTR"].round(2)
objective_display["conversion_rate"] = objective_display[
    "conversion_rate"
].round(2)

objective_display["ROAS"] = objective_display["ROAS"].round(2)
objective_display["ad_spend"] = objective_display["ad_spend"].round(2)
objective_display["revenue"] = objective_display["revenue"].round(2)
objective_display["profit"] = objective_display["profit"].round(2)

st.dataframe(
    objective_display,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    '<div class="section-title">📥 Download Marketing Report</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">Download filtered campaign data and performance summaries</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.download_button(
        "📥 Download Campaign Data",
        filtered_df.to_csv(index=False).encode("utf-8"),
        "marketing_campaign_data.csv",
        "text/csv",
        use_container_width=True
    )

with col2:
    st.download_button(
        "📊 Download Platform Summary",
        platform_analysis.to_csv(index=False).encode("utf-8"),
        "platform_performance_summary.csv",
        "text/csv",
        use_container_width=True
    )

st.markdown("""
<div class="footer">
    <hr>
    📊 <b>Marketing Performance Dashboard</b><br>
    Built with Python • Pandas • Streamlit • Plotly
</div>
""", unsafe_allow_html=True)
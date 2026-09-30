
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page config
st.set_page_config(
    page_title="ERX Dashboard",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# Custom CSS for Al-Dawaa Theme
# =========================
st.markdown("""
    <style>
    .header {
        display: flex;
        align-items: center;
        padding: 12px 20px;
        background: linear-gradient(to right, #0c1d4f, #142a63);
        border-radius: 12px;
        margin-bottom: 20px;
        text-align: center;
    }
    .header img {
        height: 60px;
        margin-right: 15px;
    }
    .header h1 {
        color: white;
        font-size: 28px;
        font-weight: 700;
        margin: 0;
        padding: 0;
        text-align: center;
    }
    </style>

    <div class="header">
        <h1>Electronic Prescriptions Dashboard</h1>
    </div>
""", unsafe_allow_html=True)
st.markdown("""
    <style>

    /* ---------- Sidebar Container ---------- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg,#ebbe34);
        padding: 20px;
    }

    /* Text inside sidebar */
    [data-testid="stSidebar"] * {
        color: #182454 !important;
        font-weight: 500;
    }

    /* Hover Animation for Sidebar Items */
    [data-testid="stSidebar"] .css-1n76uvr:hover {
        transform: scale(1.03);
        transition: 0.2s ease-in-out;
        color: #dadad9 !important;
    }

    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>

    .gold-gradient {
        background: linear-gradient(90deg, #e7c341, #f7de87);
        padding: 12px 20px;
        border-radius: 10px;
        font-size: 20px;
        color: #0c1d4f;
        font-weight: 700;
        margin-bottom: 15px;
        text-align: center;
    }

    </style>
""", unsafe_allow_html=True)
st.sidebar.markdown("## 📃 Pages")
st.sidebar.markdown("---")
page = (st.sidebar.radio('Select Page :', ['Clinic Overview', 'Region Overview', 
                                        'PHs Overview', 'Net Value Overview']))
st.sidebar.markdown("---")
if page == 'Clinic Overview':
    # add image 
    st.image("erx.png")
    st.markdown('<div class="gold-gradient">Clinic Analysis Overview</div>', unsafe_allow_html=True)
    st.markdown("""
        <style>
        .kpi-card {
            background-color: #F7DB81;   /* خلفية ناعمة */
            border-radius: 12px;
            padding: 16px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s ease-in-out;
            margin: 8px;
            color: #1C2C54;
        }
        .kpi-card:hover {
            transform: scale(1.02);
            background-color: #EBBE34;   /* Primary */
            color: #182454;
        }
        .kpi-label {
            font-size: 14px;
            font-weight: 400;
            color: #1C2454;
            margin-bottom: 6px;
        }
        .kpi-value {
            font-size: 30px;
            font-weight: 600;
            color: #182460;
            margin-bottom: 4px;
        }
        .kpi-percentage {
        font-size: 14px;
        font-weight: 500;
        color: #B13BFF;  /* أخضر */
        margin-left: 6px;
        }
        .kpi-delta {
            font-size: 14px;
            font-weight: 500;
            color: #8C94AC;
        }
        .kpi-card:hover .kpi-delta {
            color: #DADAD9;
        }
        </style>
    """, unsafe_allow_html=True)
    #data
    @st.cache_data
    def load_cleaned_data():
        return pd.read_excel('dawaarx2026.xlsx', index_col = 0)
    df = load_cleaned_data()
    # filtered_data
    @st.cache_data
    def load_clinic_data_01():
        return pd.read_excel('allerx_clinic_Jan.xlsx', index_col = 0)
    df_clinic_01 = load_clinic_data_01()
    #02
    @st.cache_data
    def load_clinic_data_02():
        return pd.read_excel('allerx_clinic_Feb.xlsx', index_col = 0)
    df_clinic_02 = load_clinic_data_02()
    #03
    @st.cache_data
    def load_clinic_data_03():
        return pd.read_excel('allerx_clinic_Mar.xlsx', index_col = 0)
    df_clinic_03 = load_clinic_data_03()
    #04
    def load_clinic_data_04():
        return pd.read_excel('allerx_clinic_Apr.xlsx', index_col = 0)
    df_clinic_04 = load_clinic_data_04()
    #05
    def load_clinic_data_05():
        return pd.read_excel('allerx_clinic_May.xlsx', index_col = 0)
    df_clinic_05 = load_clinic_data_05()
    #06
    def load_clinic_data_06():
        return pd.read_excel('allerx_clinic_Jun.xlsx', index_col = 0)
    df_clinic_06 = load_clinic_data_06()
    #07
    def load_clinic_data_07():
        return pd.read_excel('allerx_clinic_Jul.xlsx', index_col = 0)
    df_clinic_07 = load_clinic_data_07()
    #08
    def load_clinic_data_08():
        return pd.read_excel('allerx_clinic_Aug.xlsx', index_col = 0)
    df_clinic_08 = load_clinic_data_08()
    #09
    @st.cache_data
    def load_clinic_data_09():
        return pd.read_excel('allerx_clinic_Sep.xlsx', index_col = 0)
    df_clinic_09 = load_clinic_data_09()

    def collected_color(val):
        if val >= 55:
            return 'background-color:#16a34a;color:white'
        elif val >= 40:
            return 'background-color:#fde047'
        else:
            return 'background-color:#dc2626;color:white'

    def cancelled_color(val):
        if val >= 30:
            return 'background-color:#dc2626;color:white'
        elif val >= 15:
            return 'background-color:#fde047'
        else:
            return 'background-color:#16a34a;color:white'
    
    styled_table_01 = (
    df_clinic_01.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_02 = (
    df_clinic_02.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_03 = (
    df_clinic_03.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_04 = (
    df_clinic_04.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_05 = (
    df_clinic_05.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_06 = (
    df_clinic_06.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_07 = (
    df_clinic_07.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_08 = (
    df_clinic_08.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_09 = (
    df_clinic_09.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
        .map(collected_color, subset=['order_collected_%'])
        .map(cancelled_color, subset=['order_cancelled_%'])
    )
    st.markdown("---")
    # ------------------------
    # Sidebar Filters
    # ------------------------
    
    st.sidebar.markdown("## 🧭 Filters")
    st.sidebar.markdown("---")
    
    min_date = df['prescription_date'].min().date()
    max_date = df['prescription_date'].max().date()
    
    start_date, end_date = st.sidebar.date_input(
        "📅 Select Date Range:",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    # select Month
    selceted_month = st.sidebar.selectbox("📅 Select Month :", sorted(df['month_name'].unique()))
       
    if selceted_month == 'Jan':
        st.dataframe(styled_table_01.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Feb':
        st.dataframe(styled_table_02.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Mar':
        st.dataframe(styled_table_03.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Apr':
        st.dataframe(styled_table_04.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'May':
        st.dataframe(styled_table_05.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Jun':
        st.dataframe(styled_table_06.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Jul':
        st.dataframe(styled_table_07.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Aug':
        st.dataframe(styled_table_08.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Sep':
        st.dataframe(styled_table_09.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    
    selected_clinic = st.sidebar.multiselect("Select Clinic(s):", sorted(df['clinic'].unique()))
    selected_status = st.sidebar.multiselect("Select Status:", sorted(df['status'].unique()))
    selected_region = st.sidebar.multiselect("Select Region:", sorted(df['region'].fillna('Unknown').astype(str).unique()))
    selected_pres_method = st.sidebar.multiselect("Select Prescription Method:", sorted(df['prescription_method'].unique()))
    selected_delivery = st.sidebar.multiselect("Select Delivery Method:", sorted(df['delivery_method'].fillna('Unknown').astype(str).unique()))
    # Apply filters
    df_data_filtered = df[(df['prescription_date'] >= pd.to_datetime(start_date)) &
                     (df['prescription_date'] <= pd.to_datetime(end_date))]
    df_filtered = df_data_filtered.copy()
    
    if selected_clinic:
        df_filtered = df_filtered[df_filtered['clinic'].isin(selected_clinic)]
    if selected_status:
        df_filtered = df_filtered[df_filtered['status'].isin(selected_status)]
    if selected_region:
        df_filtered = df_filtered[df_filtered['region'].isin(selected_region)]
    if selected_pres_method:
        df_filtered = df_filtered[df_filtered['prescription_method'].isin(selected_pres_method)]
    if selected_delivery:
        df_filtered = df_filtered[df_filtered['delivery_method'].isin(selected_delivery)]
        ##KPIS
    st.markdown("## 📊 Overview Dashboard")
    
    col1, col2, col3, col4 , col5 = st.columns(5)
    
    total_orders = df_filtered.shape[0]
    total_erx = df_data_filtered.shape[0]
    total_per = round((total_orders / total_erx) * 100, 2)
    collected_orders = df_filtered[df_filtered['status'] == 'Order Collected'].shape[0]
    perc_collected = round((collected_orders / total_orders) * 100, 2)
    cancelled_orders = df_filtered['status'].str.contains('Cancelled|Reject|INVALID', case=False, na=False).sum()
    perc_cancelled = round((cancelled_orders / total_orders) * 100, 2)
    pending_orders = (~df_filtered['status'].str.contains('Cancelled|Reject|INVALID|Collected', case=False, na=False)).sum()
    perc_pending = round((pending_orders / total_orders) * 100, 2)
    Total_value = df_filtered['netvalue'].sum().round(2)
    
    with col1:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">⚕️ Total Orders</div>
                <div class="kpi-value">{total_orders}</div>
                <span class="kpi-percentage">({total_per}%)</span>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">✅️ Order Collected</div>
                <div class="kpi-value">{collected_orders}</div>
                <span class="kpi-percentage">({perc_collected}%)</span>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">❌ Order Cancelled</div>
                <div class="kpi-value">{cancelled_orders}</div>
                 <span class="kpi-percentage">({perc_cancelled}%)</span>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">⏳ Pending Orders</div>
                <div class="kpi-value">{pending_orders}</div>
                <span class="kpi-percentage">({perc_pending}%)</span>
            </div>
        """, unsafe_allow_html=True)
    with col5:
        st.markdown(f"""
            <div class="kpi-card">
                <div class="kpi-label">💰 Total Net Profit</div>
                <div class="kpi-value">{Total_value}</div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        # tabs for choise
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Overview", "📶 Clinic vs Status", "🕒 Clinic vs Region", "💸 Revenue", "📆 YTD"])
    custom_colors = ["#000B58","#003161" ,"#006A67" ,"#473472", "#53629E", "#87BAC3", "#D6F4ED", "#060771", "#BF1A1A", "#BF1A1A"]
    custom_colors_p = ["#000B58","#006A67" , "#53629E", "#87BAC3", "#D6F4ED", "#060771", "#BF1A1A", "#BF1A1A"]
    
    # Clinic vs Day
    with tab1:
        st.markdown("## 📅 Clinics Over Time")
    
        chart_type = st.radio("Select Chart Type:", ["Line Chart", "Bar Chart"], horizontal=True, key='clinic_tab1')
        
        erx_day = df_filtered.groupby('day')['clinic'].count().reset_index()
        
        if chart_type == "Line Chart":
            st.plotly_chart(
                px.line(erx_day, x="day", y="clinic", markers=True,
                        title="Clinics Count Over Time",
                        color_discrete_sequence=custom_colors),
                use_container_width=True
            )
        else:
            st.plotly_chart(
                px.bar(erx_day, x="day", y="clinic",
                       title="Clinics Count Over Time",text_auto= True,
                       color_discrete_sequence=custom_colors),
                use_container_width=True
            )
    
    with tab2:
        st.markdown("## 📶 Clinic vs Status")
        chart_type = st.radio("Select Chart Type:", ["Pie Chart", "Bar Chart"], horizontal=True, key="clinic_tab2")
        
        # Group data
        clinic_status = df_filtered.groupby(['clinic', 'status']).size().reset_index(name='count')
        
        # Select clinics
        selected_clinic = st.multiselect("Select Clinic(s):", sorted(df['clinic'].unique()), default=df['clinic'].unique(), key='clinic_status')
        
        # Filter the data
        filtered_data = clinic_status[clinic_status['clinic'].isin(selected_clinic)]
        
        if chart_type == 'Bar Chart':
            fig = px.bar(
                filtered_data,
                x='clinic',
                y='count',
                color='status',
                barmode='group',color_discrete_sequence=custom_colors,
                title="Clinic vs Status"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == 'Pie Chart':
            
            fig = px.pie(
                filtered_data,
                names='status',
                values='count',
                color='status',  # use 'status' or 'clinic', but make sure it's filtered
                title="Clinic Share by Status",color_discrete_sequence=custom_colors,
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.markdown("## 📶 Clinic vs Region")
        chart_type = st.radio("Select Chart Type:", ["Pie Chart", "Column Chart"], key='clinic_tab3')
        
        # Group data
        clinic_region = df_filtered.groupby(['clinic', 'region']).size().reset_index(name='count').sort_values(by= 'count',ascending=False)
        
        # Select clinics
        selected_clinic_r = st.multiselect("Select Clinic(s):", sorted(df['clinic'].unique()), default=df['clinic'].unique(), key="clinic_region")
        
        # Filter the data
        filtered_data3 = clinic_region[clinic_region['clinic'].isin(selected_clinic_r)]
        
        if chart_type == 'Column Chart':
            fig = px.bar(
                filtered_data3,
                x='clinic',
                y='count',
                color='region',
                barmode='group',color_discrete_sequence=custom_colors,
                title="Clinic vs Region"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == 'Pie Chart':
            
            fig = px.pie(
                filtered_data3,
                names='region',
                values='count',
                color='region',  # use 'status' or 'clinic', but make sure it's filtered
                title="Clinic Share by Region",color_discrete_sequence=custom_colors,
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
    with tab4:
        st.markdown("## 📶 Clinic vs Net Value")
        chart_type = st.radio("Select Chart Type:", ["Pie Chart", "Column Chart"], key='clinic_tab4')
        
        # Group data
        clinic_netvalue = df_filtered.groupby('clinic')['netvalue'].sum('netvalue').reset_index().sort_values(by="netvalue" , ascending = False)
        
        # Select clinics
        selected_clinic_n = st.multiselect("Select Clinic(s):", sorted(df['clinic'].unique()), default=df['clinic'].unique(), key="clinic_net")
        
        # Filter the data
        filtered_data4 = clinic_netvalue[clinic_netvalue['clinic'].isin(selected_clinic_n)]
        
        if chart_type == 'Column Chart':
            fig = px.bar(
                filtered_data4,
                x='clinic',
                y='netvalue',
                barmode='group',color_discrete_sequence=custom_colors,
                title="Clinic vs NetValue"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == 'Pie Chart':
            
            fig = px.pie(
                filtered_data4,
                names='clinic',
                values='netvalue',
                title="Clinic Share by NetValue",color_discrete_sequence=custom_colors,
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.markdown("## 📶 ERX Distributions over Months")
        chart_type = st.radio("Select Chart Type:", ["Table", "Bar Chart"], horizontal=True, key='ytd_tab5')
        # data 
        status_per_month = df.groupby(['month_name', 'status'])['clinic'].count().reset_index(name = 'Count')
        clinic_per_m = df.groupby(['month_name', 'clinic'])['clinic'].count().reset_index(name = 'Count')
        
        if chart_type == 'Bar Chart':
            # selected status
            selected_status_ytd = st.multiselect("Select Status(s):", sorted(df['status'].unique()), 
                                             default = (df['status'].fillna('other').astype(str).unique()),key="status_ytd")
            #filtered data
            df_status_ytd = status_per_month[status_per_month['status'].isin(selected_status_ytd)]
            fig = px.bar(
                df_status_ytd, x='status', y='Count', color='status',facet_col = 'month_name',
                color_discrete_sequence=custom_colors,text_auto = True, title="Status Distributions over Months" )
            st.plotly_chart(fig, use_container_width=True)
            
        elif chart_type == 'Table':
            @st.cache_data
            def load_data_ytd():
                return pd.read_excel('rex_ytd.xlsx', index_col = 0)
            df_ytd = load_data_ytd()
            
            def collected_color(val):
                if val >= 55:
                    return 'background-color:#16a34a;color:white'
                elif val >= 40:
                    return 'background-color:#fde047'
                else:
                    return 'background-color:#dc2626;color:white'
        
            def cancelled_color(val):
                if val >= 30:
                    return 'background-color:#dc2626;color:white'
                elif val >= 15:
                    return 'background-color:#fde047'
                else:
                    return 'background-color:#16a34a;color:white'
            
            styled_table = (
            df_ytd
            .style
            .set_table_styles([
                {
                    'selector': 'th',
                    'props': [
                        ('background-color', '#1f4fd8'),
                        ('color', 'white'),
                        ('font-weight', 'bold'),
                        ('text-align', 'center')]
                },
                {
                    'selector': 'td',
                    'props': [
                        ('text-align', 'center'),   # ✅ أهم سطر
                        ('vertical-align', 'middle')]
                },
                {
                    'selector': 'tr:last-child',
                    'props': [
                        ('background-color', '#e5e7eb'),
                        ('font-weight', 'bold')]
                }])
            .map(collected_color, subset=['order_collected_%'])
            .map(cancelled_color, subset=['order_cancelled_%'])
            )
            st.dataframe(styled_table.format({'netvalue': '{:,.2f}',
                                              'order_collected_%' : '{:,.2f}',
                                             'order_cancelled_%' : '{:,.2f}',
                                             'order_pending_%' :'{:,.2f}'}))
        
    # Footer
    st.markdown("""---""")
    st.markdown("""
                    <p style='text-align: center; font-size: 16px;'>
                        © 2026 | Developed by <strong>Dr.Ahmed Saif</strong> - Insurance Team Leader | 📧 <a href="mailto:drahmed.saif90@gmail.com">Contact</a>
                    </p>
                """, unsafe_allow_html=True)
#---------------------------
if page == 'Region Overview':
    st.markdown('<div class="gold-gradient"> Region Analysis Overview </div>', unsafe_allow_html=True)
    
    @st.cache_data
    def load_cleaned_data():
        return pd.read_excel('dawaarx2026.xlsx', index_col = 0)
    df = load_cleaned_data()
    # filtered_data
    @st.cache_data
    def load_region_data_01():
        return pd.read_excel('rx_region_Jan.xlsx', index_col = 0)
    df_region_01 = load_region_data_01()
    #02
    @st.cache_data
    def load_region_data_02():
        return pd.read_excel('rx_region_Feb.xlsx', index_col = 0)
    df_region_02 = load_region_data_02()
    #03
    @st.cache_data
    def load_region_data_03():
        return pd.read_excel('rx_region_Mar.xlsx', index_col = 0)
    df_region_03 = load_region_data_03()
    #04
    def load_region_data_04():
        return pd.read_excel('rx_region_Apr.xlsx', index_col = 0)
    df_region_04 = load_region_data_04()
    #05
    def load_region_data_05():
        return pd.read_excel('rx_region_May.xlsx', index_col = 0)
    df_region_05 = load_region_data_05()
    #06
    def load_region_data_06():
        return pd.read_excel('rx_region_Jun.xlsx', index_col = 0)
    df_region_06 = load_region_data_06()
    #07
    def load_region_data_07():
        return pd.read_excel('rx_region_Jul.xlsx', index_col = 0)
    df_region_07 = load_region_data_07()
    #08
    def load_region_data_08():
        return pd.read_excel('rx_region_Aug.xlsx', index_col = 0)
    df_region_08 = load_region_data_08()
    #09
    def load_region_data_09():
        return pd.read_excel('rx_region_Sep.xlsx', index_col = 0)
    df_region_09 = load_region_data_09()
    
    def collected_color(val):
        if val >= 55:
            return 'background-color:#16a34a;color:white'
        elif val >= 40:
            return 'background-color:#fde047'
        else:
            return 'background-color:#dc2626;color:white'

    def cancelled_color(val):
        if val >= 30:
            return 'background-color:#dc2626;color:white'
        elif val >= 15:
            return 'background-color:#fde047'
        else:
            return 'background-color:#16a34a;color:white'
    
    styled_table_01 = (
    df_region_01.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_02 = (
    df_region_02.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_03 = (
    df_region_03.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_04 = (
    df_region_04.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_05 = (
    df_region_05.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_06 = (
    df_region_06.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_07 = (
    df_region_07.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_08 = (
    df_region_08.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_09 = (
    df_region_09.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},{'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child', 'props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    st.markdown("---") 
       # ------------------------
    # Sidebar Filters
    # ------------------------
    
    st.sidebar.markdown("## 🧭 Filters")
    st.sidebar.markdown("---")
    
    min_date = df['prescription_date'].min().date()
    max_date = df['prescription_date'].max().date()
    
    start_date, end_date = st.sidebar.date_input("📅 Select Date Range:", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    df_filtered = df[(df['prescription_date'] >= pd.to_datetime(start_date)) &
                     (df['prescription_date'] <= pd.to_datetime(end_date))]
    # select Month
    selceted_month = st.sidebar.selectbox("📅 Select Month :", sorted(df['month_name'].unique()))
       
    if selceted_month == 'Jan':
        st.dataframe(styled_table_01.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Feb':
        st.dataframe(styled_table_02.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Mar':
        st.dataframe(styled_table_03.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Apr':
        st.dataframe(styled_table_04.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'May':
        st.dataframe(styled_table_05.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Jun':
        st.dataframe(styled_table_06.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Jul':
        st.dataframe(styled_table_07.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Aug':
        st.dataframe(styled_table_08.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Sep':
        st.dataframe(styled_table_09.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    # tabs for choise
    tab1, tab2, tab3 = st.tabs(["📈 Overview", "📶 Region vs Status", "💸 Revenue"])
    custom_colors = ["#000B58","#003161" ,"#006A67" ,"#473472", "#53629E", "#87BAC3", "#D6F4ED", "#060771", "#BF1A1A", "#BF1A1A"]

    with tab1:
        st.markdown("## 📊 ERX Distributions per Regions")
        total_orders = df_filtered['region'].value_counts().reset_index()
        
        st.plotly_chart(
                px.bar(total_orders, x="region", y="count",
                       title="ERX Distributions per Regions",text_auto= True,
                       color_discrete_sequence=custom_colors),
                use_container_width=True
            )
    
    with tab2:
        st.markdown("## 📶 Region vs Status")
        chart_type = st.radio("Select Chart Type:", ["Pie Chart", "Bar Chart"], horizontal=True, key="region_tab2")
        
        # Group data
        region_status = df_filtered.groupby(['region', 'status']).size().reset_index(name='count')
        
        # Select clinics
        selected_region = st.multiselect("Select Region(s):", sorted(df['region'].fillna('others').astype(str).unique()),
                                         default=df['region'].fillna('others').astype(str).unique(), key='region_status_tab2')
        
        # Filter the data
        filtered_data_reg = region_status[region_status['region'].isin(selected_region)]
        
        if chart_type == 'Bar Chart':
            fig = px.bar(
                filtered_data_reg,
                x='region',
                y='count',
                color='status',
                barmode='group',color_discrete_sequence=custom_colors,
                title="Region vs Status")
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == 'Pie Chart':
            fig = px.pie(
                filtered_data_reg,
                names='status',
                values='count',
                color='status',  # use 'status' or 'clinic', but make sure it's filtered
                title="Region Share by Status",color_discrete_sequence=custom_colors,
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
    with tab3:
        st.markdown("#### 📈💰📊 Region vs Net Value")
        chart_type = st.radio("Select Chart Type:", ["Line Chart", "Bar Chart"], key='region_tab4')
        
        # Group data
        region_netvalue = df_filtered.groupby('region')['netvalue'].sum('netvalue').reset_index().sort_values(by="netvalue" , ascending = False)
        
        # Select clinics
        selected_region_n = st.multiselect("Select Region(s):", sorted(df['region'].fillna('others').astype(str).unique()),
                                         default=df['region'].fillna('others').astype(str).unique(), key="region_net")
        
        # Filter the data
        filtered_df_reg = region_netvalue[region_netvalue['region'].isin(selected_region_n)]
        
        if chart_type == 'Bar Chart':
            fig = px.bar(
                filtered_df_reg,
                x='region',
                y='netvalue',
                barmode='group',color_discrete_sequence=custom_colors,
                title="Region vs NetValue"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == 'Line Chart':
            
            fig = px.line(
                filtered_df_reg,
               x = 'region', y = 'netvalue', markers = True,
                title="Region Share by NetValue",color_discrete_sequence=custom_colors
            )
            st.plotly_chart(fig, use_container_width=True)
    st.markdown("""---""")
    st.markdown("""
                    <p style='text-align: center; font-size: 16px;'>
                        © 2026 | Developed by <strong>Dr.Ahmed Saif</strong> "Insurance Team Leader" | 📧 <a href="mailto:drahmed.saif90@gmail.com">Contact</a>
                    </p>
                """, unsafe_allow_html=True)
#---------------------
if page == 'PHs Overview':
    st.markdown('<div class="gold-gradient"> PHs Analysis Overview </div>', unsafe_allow_html=True)
    
    @st.cache_data
    def load_data():
        return pd.read_excel('dawaarx2026.xlsx', index_col = 0)
    df = load_data()
    # filtered_data
    #01
    @st.cache_data
    def load_store_data_01():
        return pd.read_excel('allerx_store_Jan.xlsx', index_col = 0)
    df_store_01 = load_store_data_01()
    #02
    @st.cache_data
    def load_store_data_02():
        return pd.read_excel('allerx_store_Feb.xlsx', index_col = 0)
    df_store_02 = load_store_data_02()
    #03
    @st.cache_data
    def load_store_data_03():
        return pd.read_excel('allerx_store_Mar.xlsx', index_col = 0)
    df_store_03 = load_store_data_03()
    #04
    @st.cache_data
    def load_store_data_04():
        return pd.read_excel('allerx_store_Apr.xlsx', index_col = 0)
    df_store_04 = load_store_data_04()
    #05
    @st.cache_data
    def load_store_data_05():
        return pd.read_excel('allerx_store_May.xlsx', index_col = 0)
    df_store_05 = load_store_data_05()
    #06
    @st.cache_data
    def load_store_data_06():
        return pd.read_excel('allerx_store_Jun.xlsx', index_col = 0)
    df_store_06 = load_store_data_06()
    #07
    @st.cache_data
    def load_store_data_07():
        return pd.read_excel('allerx_store_Jul.xlsx', index_col = 0)
    df_store_07 = load_store_data_07()
    #08
    @st.cache_data
    def load_store_data_08():
        return pd.read_excel('allerx_store_Jan.xlsx', index_col = 0)
    df_store_08 = load_store_data_08()
    #09
    @st.cache_data
    def load_store_data_09():
        return pd.read_excel('allerx_store_Sep.xlsx', index_col = 0)
    df_store_09 = load_store_data_09()
    
    def collected_color(val):
        if val >= 55:
            return 'background-color:#16a34a;color:white'
        elif val >= 40:
            return 'background-color:#fde047'
        else:
            return 'background-color:#dc2626;color:white'

    def cancelled_color(val):
        if val >= 30:
            return 'background-color:#dc2626;color:white'
        elif val >= 15:
            return 'background-color:#fde047'
        else:
            return 'background-color:#16a34a;color:white'
    
    styled_table_01 = (
    df_store_01.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_02 = (
    df_store_02.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_03 = (
    df_store_03.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_04 = (
    df_store_04.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_05 = (
    df_store_05.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_06 = (
    df_store_06.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_07 = (
    df_store_07.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_08 = (
    df_store_08.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    styled_table_09 = (
    df_store_09.style.set_table_styles([
        {'selector': 'th','props': [
                ('background-color', '#1f4fd8'),
                ('color', 'white'),
                ('font-weight', 'bold'),
                ('text-align', 'center')]},
        {'selector': 'td','props': [
                ('text-align', 'center'),   # ✅ أهم سطر
                ('vertical-align', 'middle')]},
        {'selector': 'tr:last-child','props': [
                ('background-color', '#e5e7eb'),
                ('font-weight', 'bold')]}])
    .map(collected_color, subset=['order_collected_%'])
    .map(cancelled_color, subset=['order_cancelled_%'])
    )
    st.markdown("---") 
       # ------------------------
    # Sidebar Filters
    # ------------------------
    
    st.sidebar.markdown("## 🧭 Filters")
    st.sidebar.markdown("---")
    
    min_date = df['prescription_date'].min().date()
    max_date = df['prescription_date'].max().date()
    
    start_date, end_date = st.sidebar.date_input("📅 Select Date Range:", value=(min_date, max_date), min_value=min_date, max_value=max_date)
    df_filtered = df[(df['prescription_date'] >= pd.to_datetime(start_date)) &
                     (df['prescription_date'] <= pd.to_datetime(end_date))]

    selceted_month = st.sidebar.selectbox("📅 Select Month :", sorted(df['month_name'].unique()), key = "store_filtered_month")
    if selceted_month == 'Jan':
        st.dataframe(styled_table_01.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Feb':
        st.dataframe(styled_table_02.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Mar':
        st.dataframe(styled_table_03.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Apr':
        st.dataframe(styled_table_04.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'May':
        st.dataframe(styled_table_05.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Jun':
        st.dataframe(styled_table_06.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Jul':
        st.dataframe(styled_table_07.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Aug':
        st.dataframe(styled_table_08.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    elif selceted_month == 'Sep':
        st.dataframe(styled_table_09.format({'netvalue': '{:,.2f}',
                                      'order_collected_%' : '{:,.2f}',
                                     'order_cancelled_%' : '{:,.2f}',
                                     'order_pending_%' :'{:,.2f}'}))
    st.markdown("---") 
    # tabs for choise
    tab1, tab2, tab3 = st.tabs(["📈 Overview", "📶 PHs vs Status", "💸 Revenue"])
    custom_colors = ["#000B58","#003161" ,"#006A67" ,"#473472", "#53629E", "#87BAC3", "#D6F4ED", "#060771", "#BF1A1A", "#BF1A1A"]

    with tab1:
        st.markdown("## 📊 ERX Distributions per Stores")
        total_orders = df_filtered['store_code'].value_counts().reset_index()
        
        st.plotly_chart(
                px.line(total_orders, x="store_code", y="count",
                       title="ERX Distributions per Stores",markers= True,
                       color_discrete_sequence=custom_colors),
                use_container_width=True
            )
    
    with tab2:
        st.markdown("## 📶 Stores vs Status")
        chart_type = st.radio("Select Chart Type:", ["Pie Chart", "Bar Chart"], horizontal=True, key="store_tab2")
        
        # Group data
        store_status = df_filtered.groupby(['store_code', 'status']).size().reset_index(name='count')
        
        #top_n
        top_n = st.slider('Top Stores', min_value = 1, max_value = 100, value=10, key='top_net')
        top_stores = (df['store_code'].fillna('others').astype(str).value_counts().head(top_n).index.tolist())
        st.subheader(f"Top {top_n} Stores by Orders")

        # Select clinics
        selected_store = st.multiselect("Select Store(s):", sorted(df['store_code'].fillna('others').astype(str).unique()),
                                        default = top_stores, key='store_status_tab2')
        # Filter the data
        filtered_data_store = store_status[store_status['store_code'].astype(str).isin(selected_store)]
        
        if chart_type == 'Bar Chart':
            fig = px.bar(
                filtered_data_store,
                x='store_code',
                y='count',
                color='status',
                barmode='group',color_discrete_sequence=custom_colors,
                title="Store vs Status"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == 'Pie Chart':
            fig = px.pie(
                filtered_data_store,
                names='status',
                values='count',
                color='status',  # use 'status' or 'clinic', but make sure it's filtered
                title="Store Share by Status",color_discrete_sequence=custom_colors,
                hole=0.4
            )
            st.plotly_chart(fig, use_container_width=True)
    with tab3:
        st.markdown("#### 💰 Stores vs Net Value")
        chart_type = st.radio("Select Chart Type:", ["Line Chart", "Bar Chart"], horizontal=True, key='store__net_tab3')
        
        # Group data
        store_netvalue = df_filtered.groupby(['store_code', 'prescription_method'])['netvalue'].sum('netvalue').reset_index()

        #top_n
        top_n = st.slider('Top Stores', min_value = 1, max_value = 100, value=10, key='top')
        top_stores = (df['store_code'].fillna('others').astype(str).value_counts().head(top_n).index.tolist())
        st.subheader(f"Top {top_n} Stores by Orders")

        # Select clinics
        selected_store = st.multiselect("Select Store(s):", sorted(df['store_code'].fillna('others').astype(str).unique()),
                                        default = top_stores, key='store_net_tab3')
        # Filter the data
        filtered_data_store = store_netvalue[store_netvalue['store_code'].astype(str).isin(selected_store)]
        
        if chart_type == 'Bar Chart':
            fig = px.bar(
                filtered_data_store,
                x='store_code',
                y='netvalue', color = 'prescription_method', facet_col = 'prescription_method',
                barmode='group',color_discrete_sequence=['#090040', '#B13BFF'],
                title="Region vs NetValue"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        elif chart_type == 'Line Chart':
            
            fig = px.line(
                filtered_data_store,
               x = 'store_code', y = 'netvalue', facet_col = 'prescription_method', markers = True,
                title="Stores Share by NetValue",color_discrete_sequence=['#000B58', '#003161', '#006A67'])
            st.plotly_chart(fig, use_container_width=True)
    st.markdown("""---""")
    st.markdown("""
                    <p style='text-align: center; font-size: 16px;'>
                        © 2026 | Developed by <strong>Dr.Ahmed Saif</strong> "ERX Insurance Team Leader" | 📧 <a href="mailto:drahmed.saif90@gmail.com">Contact</a>
                    </p>
                """, unsafe_allow_html=True)

#----------------------------
if page == 'Net Value Overview':
    st.markdown('<div class="gold-gradient"> 💰 Net Profit Overview </div>', unsafe_allow_html=True)
    #df
    @st.cache_data
    def load_store_data():
        return pd.read_excel('dawaarx2026.xlsx', index_col = 0)
    df = load_store_data()
    clinic_m_status = df.groupby(['clinic', 'prescription_method', 'status']).size().reset_index(name='Count')
    clinic_m_net = df.groupby(['clinic', 'prescription_method'])['netvalue'].sum('netvalue').reset_index()
    
    custom_colors = ["#000B58","#006A67" , "#53629E", "#87BAC3", "#D6F4ED", "#060771", "#BF1A1A", "#BF1A1A"]
    # select clinic
    selected_clinic5 = st.multiselect("Select Clinic(s):", sorted(df['clinic'].unique()), default=df['clinic'].unique(), key = 'clinic_net_val')
    #filter date
    clinic_m_status5 = clinic_m_status[clinic_m_status['clinic'].isin(selected_clinic5)]
    clinic_m_net5 = clinic_m_net[clinic_m_net['clinic'].isin(selected_clinic5)]
    
    fig = px.bar(
    clinic_m_status5, x = 'clinic', y = 'Count', color = 'status',
        facet_col= 'prescription_method', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(
    clinic_m_net5, x = 'clinic', y = 'netvalue', color = 'prescription_method', facet_col= 'prescription_method',
    color_discrete_sequence= custom_colors)
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("""---""")
    st.markdown("""
                    <p style='text-align: center; font-size: 16px;'>
                        © 2026 | Developed by <strong>Dr.Ahmed Saif</strong> "ERX Insurance Team Leader" | 📧 <a href="mailto:drahmed.saif90@gmail.com">Contact us: 01032130013</a>
                    </p>
                """, unsafe_allow_html=True)

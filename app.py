import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Penjualan", layout="wide")

st.title("📊 Dashboard Penjualan Interaktif")
st.write("Upload file CSV penjualan untuk eksplorasi data.")

# Upload file
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    # Load data
    @st.cache_data
    def load_data(file):
        df = pd.read_csv(file, parse_dates=["Date"])
        return df

    df = load_data(uploaded_file)

    # Sidebar filter
    st.sidebar.header("Filter Data")
    start_date = st.sidebar.date_input("Start Date", df["Date"].min())
    end_date = st.sidebar.date_input("End Date", df["Date"].max())
    regions = st.sidebar.multiselect("Pilih Region", df["Region"].unique(), default=df["Region"].unique())

    # Filter data
    df_filtered = df[(df["Date"] >= pd.to_datetime(start_date)) &
                     (df["Date"] <= pd.to_datetime(end_date)) &
                     (df["Region"].isin(regions))]

    # KPI Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"{df_filtered['Sales'].sum():,}")
    col2.metric("Total Revenue", f"${df_filtered['Revenue'].sum():,}")
    col3.metric("Total Profit", f"${df_filtered['Profit'].sum():,}")

    st.markdown("---")

    # Grafik Penjualan per Tanggal
    fig1 = px.line(df_filtered, x="Date", y="Sales", color="Region", title="Sales per Date")
    st.plotly_chart(fig1, use_container_width=True)

    # Grafik Revenue per Region
    fig2 = px.bar(df_filtered.groupby("Region", as_index=False)[["Revenue"]].sum(),
                  x="Region", y="Revenue", title="Revenue per Region")
    st.plotly_chart(fig2, use_container_width=True)

    # Top Produk berdasarkan Sales
    top_products = df_filtered.groupby("Product", as_index=False)[["Sales"]].sum().sort_values("Sales", ascending=False)
    fig3 = px.pie(top_products, names="Product", values="Sales", title="Top Products by Sales")
    st.plotly_chart(fig3, use_container_width=True)

    # Tabel Data
    st.subheader("📑 Data Detail")
    st.dataframe(df_filtered)

else:
    st.info("⬆️ Silakan upload file CSV untuk memulai analisis.")

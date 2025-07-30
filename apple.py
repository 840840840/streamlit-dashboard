import streamlit as st
import pandas as pd
import plotly.express as px
# Set page configuration
st.set_page_config(
    page_title="Apple Sales Dashboard",
    page_icon="🍏",
    layout="wide"
)

# Load data
df = pd.read_csv("apple_sales_2024.csv")
st.title("🍏 Apple Sales Dashboard 2024")
# write my introduction
st.markdown("Muhammad Usama")
st.write("This dashboard provides insights into Apple's sales data across different products and regions in 2024.")


# Sidebar buttons
st.sidebar.title("📊 Dashboard Menu")
page = st.sidebar.radio("Select Analysis Section", ["📌 Basic Overview", "📈 Visual Analysis", "🌎 State-wise Sales", "🧩 Product-wise Sales Comparison"])

# 1. BASIC OVERVIEW
if page == "📌 Basic Overview":
    st.title("📌 Basic Dataset Overview")
    st.write("### Sample Data")
    st.dataframe(df.head())

    st.write("### Columns and Data Types")
    st.write(df.dtypes)

    st.write("### Null Values")
    st.write(df.isnull().sum())

    st.write("### Summary Statistics")
    st.write(df.describe())

# 2. VISUAL ANALYSIS
elif page == "📈 Visual Analysis":
    st.title("🧁 Product-wise Global Sales Pie")
    total_sales = {
        "iPhone": df['iPhone Sales (in million units)'].sum(),
        "iPad": df['iPad Sales (in million units)'].sum(),
        "Mac": df['Mac Sales (in million units)'].sum(),
        "Wearables": df['Wearables (in million units)'].sum()
    }
    pie_df = pd.DataFrame({'Product': total_sales.keys(), 'Sales': total_sales.values()})
    fig = px.pie(pie_df, names='Product', values='Sales', title='Product-wise Sales Distribution')
    st.plotly_chart(fig)

# 3. STATE-WISE SALES
elif page == "🌎 State-wise Sales":
    st.title("🌎 State-wise Product Sales")
    selected_state = st.selectbox("Select a State", df["State"].unique())
    filtered = df[df["State"] == selected_state]

    st.write(f"### Sales in {selected_state}")
    st.dataframe(filtered)

    # Bar Chart
    sales_cols = ["iPhone Sales (in million units)", "Mac Sales (in million units)", 
                  "iPad Sales (in million units)", "Wearables (in million units)"]

    values = filtered[sales_cols].sum().values
    fig = px.bar(
        x=sales_cols,
        y=values,
        labels={'x': 'Product', 'y': 'Sales'},
        title=f"{selected_state} - Product Sales"
    )
    st.plotly_chart(fig, use_container_width=True)

# 4. PRODUCT-WISE SALES COMPARISON
elif page == "🧩 Product-wise Sales Comparison":
    st.title("🧩 Compare Products Across States")

    product = st.selectbox("Select Product", ["iPhone Sales (in million units)", 
                                              "Mac Sales (in million units)", 
                                              "iPad Sales (in million units)", 
                                              "Wearables (in million units)"])
    
    fig = px.bar(
        df,
        x="State",
        y=product,
        color="Region",
        title=f"{product} by State",
        labels={product: "Sales"}
    )
    st.plotly_chart(fig, use_container_width=True)
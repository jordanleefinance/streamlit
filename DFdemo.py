import streamlit as st
import pandas as pd
import altair as alt

from Portfolio_Gui import StockPortfolioAnalysis

from urllib.error import URLError

@st.cache

def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

def get_user_data():
    portfolio1 = "EVH FB MSFT SPY SPYG INDS EQNR GLNCY AAPL ARE IBN SNAP SDY EMR"
    num = "8 0.919447 1 1.42 1.01 1.02 3 5 1 1 4 2 1 1"
    portfolio1 = portfolio1.split()
    num = num.split()
    Portfolio = StockPortfolioAnalysis(portfolio=portfolio1,
                                       num_shares=num,
                                       start_date='2017-01-01', end_date='2022-02-01', freq='D', index_stock='^GSPC')
    df = Portfolio.get_price_df(portfolio=portfolio1,
                                num_shares=num,
                                start_date='2017-01-01', end_date='2022-02-01', freq='D')
    return df

try:
    df = get_user_data()
    countries = st.multiselect(
        "Choose Stocks", list(df.columns), ["EVH", "FB"]
    )
    if not countries:
        st.error("Please select a stock.")
    else:
        data = df[countries]
        st.write("### Stock Prices", data.sort_index())

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "symbols", "value": "Prices"}
        )
        chart = (
            alt.Chart(data)
            .mark_line()
            .encode(
                x="Date:T",
                y="Prices:Q",
                color="symbols:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)

except URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )
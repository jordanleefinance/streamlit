import datetime as datetime
import pandas as pd
import streamlit as st
import datetime
import scipy.optimize as opt


am_schedule_columns = ["Periods", "Date", "Beginning Balance", "Monthly Payment", "Principal", "Interest",
                       "Ending Balance"]


def AMbulid(data):
    # Build formulas and fill down
    for period in range(2, periods + 1):
        data.at[period, "Beginning Balance"] = data.at[period - 1, "Ending Balance"]
        data.at[period, "Monthly Payment"] = data.at[1, "Monthly Payment"]
        data.at[period, "Interest"] = (data.at[period, "Beginning Balance"] * (ir / pper))
        data.at[period, "Principal"] = data.at[period, "Monthly Payment"] - data.at[period, "Interest"]
        data.at[period, "Ending Balance"] = data.at[period, "Beginning Balance"] - data.at[period, "Principal"]

    return data



with st.form("Loan Details"):
    st.write("Please provide the following:")
    loan_amt = st.number_input("Loan Amount", step=1.00, value=100500.00, format="%.2f")
    interest_rate = st.slider("Interest Rate", step=0.001, max_value=50.00, value=5.755, format="%.3f")
    pper = st.number_input("Payments per year", value=12)
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date", max_value=datetime.datetime(2150, 12, 31))

    periods = len(pd.date_range(start_date, end_date - datetime.timedelta(days=1), freq="M"))
    ir = interest_rate/100
    interest = loan_amt * (ir/pper)

    button = st.form_submit_button("Submit")
    if button:
        payment = loan_amt * (ir/pper) * (1-(1/((1+(ir/pper))**periods)))
        # DF creation
        df = pd.DataFrame(columns=am_schedule_columns)

        # Set index -- total periods
        df["Periods"] = range(1, periods+1)
        df.set_index(df["Periods"], inplace=True)
        del(df["Periods"])

        df["Date"] = [d.strftime('%B %d, %Y') for d in pd.date_range(start_date, end_date - datetime.timedelta(days=1),
                                                                     freq="M")]
        # Given
        df.at[1, "Beginning Balance"] = loan_amt

        # Placeholder monthly payment
        df.at[1, "Monthly Payment"] = payment

        # Calculate interest and principal
        if interest>payment:
            df.at[1, "Interest"] = interest # User error prevention placeholder
            df.at[1, "Principal"] = (payment + interest)
        else:
            df.at[1, "Interest"] = interest
            df.at[1, "Principal"] = (payment - interest)

        # Calculate Ending balance
        df.at[1, "Ending Balance"] = (loan_amt - float(df.at[1, "Principal"]))

        # Build formulas and fill down
        for period in range(2, periods + 1):
            df.at[period, "Beginning Balance"] = df.at[period - 1, "Ending Balance"]
            df.at[period, "Monthly Payment"] = df.at[1, "Monthly Payment"]
            df.at[period, "Interest"] = (float(df.at[period, "Beginning Balance"]) * (ir / pper))
            df.at[period, "Principal"] = float(df.at[period, "Monthly Payment"]) - float(df.at[period, "Interest"])
            df.at[period, "Ending Balance"] = float(df.at[period, "Beginning Balance"]) - float(
                df.at[period, "Principal"])

        df["Beginning Balance"].apply(lambda x: "${:,.2f}".format(float(x)))
        df["Monthly Payment"].apply(lambda x: "${:,.2f}".format(float(x)))
        df["Interest"].apply(lambda x: "${:,.2f}".format(float(x)))
        df["Principal"].apply(lambda x: "${:,.2f}".format(float(x)))
        df["Ending Balance"].apply(lambda x: "${:,.2f}".format(float(x)))

        st.dataframe(df, use_container_width=False)

        #  df = opt.root(AMbuild(df), df.at[periods, "Ending Balance"]==0)


        print(df)


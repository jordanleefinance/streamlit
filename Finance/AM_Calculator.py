import datetime as datetime
import pandas as pd
import streamlit as st
import datetime
import numpy as np
import xlsxwriter
import numpy_financial as npf
import scipy.optimize as opt

source_file = r"C:\Users\jorda\OneDrive\Documents\GitHub\streamlit\Finance\AM_Calculator_buoy.xlsx"
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


with st.sidebar.title("Loan Details"):
    st.sidebar.write("Please provide the following:")
    loan_amt = st.sidebar.number_input("Loan Amount", step=1.00, value=147920.00, format="%.2f")
    interest_rate = st.sidebar.number_input("Interest Rate", step=0.001, max_value=50.00, value=7.125, format="%.3f")
    pper = st.sidebar.number_input("Payments per year", value=12)
    start_date = st.sidebar.date_input("Start Date")
    end_date = st.sidebar.date_input("End Date", max_value=datetime.datetime(2150, 12, 31),
                             value=datetime.datetime.now() + datetime.timedelta(days=30*365))

    periods = len(pd.date_range(start_date, end_date - datetime.timedelta(days=1), freq="M"))
    ir = interest_rate/100
    ir_up = (interest_rate + 0.5)/100
    ir_down = (interest_rate - 0.5)/100

    interest = loan_amt * (ir/pper)
    interest_up = loan_amt * (ir_up/pper)
    interest_down = loan_amt * (ir_down / pper)

    button = st.sidebar.button("Submit")

if button:
    payment = -npf.pmt((ir/pper), periods, loan_amt)
    payment_up = -npf.pmt((ir_up/pper), periods, loan_amt)
    payment_down = -npf.pmt((ir_down/pper), periods, loan_amt)

    # DF creation
    df = pd.DataFrame(columns=am_schedule_columns)
    df_up = pd.DataFrame(columns=am_schedule_columns)
    df_down = pd.DataFrame(columns=am_schedule_columns)

    # Set index -- total periods
    df["Periods"] = range(1, periods+1)
    df.set_index(df["Periods"], inplace=True)
    del(df["Periods"])

    df_up["Periods"] = range(1, periods + 1)
    df_up.set_index(df_up["Periods"], inplace=True)
    del (df_up["Periods"])

    df_down["Periods"] = range(1, periods + 1)
    df_down.set_index(df_down["Periods"], inplace=True)
    del (df_down["Periods"])

    df["Date"] = [d.strftime('%B %d, %Y') for d in pd.date_range(start_date, end_date - datetime.timedelta(days=1),
                                                                 freq="M")]
    df_up["Date"] = [d.strftime('%B %d, %Y') for d in pd.date_range(start_date, end_date - datetime.timedelta(days=1),
                                                                    freq="M")]
    df_down["Date"] = [d.strftime('%B %d, %Y') for d in pd.date_range(start_date, end_date - datetime.timedelta(days=1),
                                                                      freq="M")]
    # Given
    df.at[1, "Beginning Balance"] = loan_amt
    df_up.at[1, "Beginning Balance"] = loan_amt
    df_down.at[1, "Beginning Balance"] = loan_amt

    # Placeholder monthly payment
    df.at[1, "Monthly Payment"] = payment
    df_up.at[1, "Monthly Payment"] = payment_up
    df_down.at[1, "Monthly Payment"] = payment_down

    # Calculate interest and principal
    if interest>payment:
        df.at[1, "Interest"] = interest  # User error prevention placeholder
        df.at[1, "Principal"] = (payment + interest)

        df_up.at[1, "Interest"] = interest_up  # User error prevention placeholder
        df_up.at[1, "Principal"] = (payment_up + interest_up)

        df_down.at[1, "Interest"] = interest_down  # User error prevention placeholder
        df_down.at[1, "Principal"] = (payment_down + interest_down)
    else:
        df.at[1, "Interest"] = interest
        df.at[1, "Principal"] = (payment - interest)

        df_up.at[1, "Interest"] = interest_up
        df_up.at[1, "Principal"] = (payment_up - interest_up)

        df_down.at[1, "Interest"] = interest_down
        df_down.at[1, "Principal"] = (payment_down - interest_down)

    # Calculate Ending balance
    df.at[1, "Ending Balance"] = (loan_amt - float(df.at[1, "Principal"]))
    df_up.at[1, "Ending Balance"] = (loan_amt - float(df_up.at[1, "Principal"]))
    df_down.at[1, "Ending Balance"] = (loan_amt - float(df_down.at[1, "Principal"]))

    # Build formulas and fill down
    for period in range(2, periods + 1):
        df.at[period, "Beginning Balance"] = df.at[period - 1, "Ending Balance"]
        df.at[period, "Monthly Payment"] = df.at[1, "Monthly Payment"]
        df.at[period, "Interest"] = (float(df.at[period, "Beginning Balance"]) * (ir / pper))
        df.at[period, "Principal"] = float(df.at[period, "Monthly Payment"]) - float(df.at[period, "Interest"])
        df.at[period, "Ending Balance"] = float(df.at[period, "Beginning Balance"]) - float(
            df.at[period, "Principal"])

        df_up.at[period, "Beginning Balance"] = df_up.at[period - 1, "Ending Balance"]
        df_up.at[period, "Monthly Payment"] = df_up.at[1, "Monthly Payment"]
        df_up.at[period, "Interest"] = (float(df_up.at[period, "Beginning Balance"]) * (ir_up / pper))
        df_up.at[period, "Principal"] = float(df_up.at[period, "Monthly Payment"]) - float(df_up.at[period, "Interest"])
        df_up.at[period, "Ending Balance"] = float(df_up.at[period, "Beginning Balance"]) - float(
            df_up.at[period, "Principal"])

        df_down.at[period, "Beginning Balance"] = df_down.at[period - 1, "Ending Balance"]
        df_down.at[period, "Monthly Payment"] = df_down.at[1, "Monthly Payment"]
        df_down.at[period, "Interest"] = (float(df_down.at[period, "Beginning Balance"]) * (ir_down / pper))
        df_down.at[period, "Principal"] = float(df_down.at[period, "Monthly Payment"]) - float(df_down.at[period, "Interest"])
        df_down.at[period, "Ending Balance"] = float(df_down.at[period, "Beginning Balance"]) - float(
            df_down.at[period, "Principal"])

    df["Cumulative Interest"] = df["Interest"].cumsum()
    df["Cumulative Principal"] = df["Principal"].cumsum()

    df_up["Cumulative Interest"] = df_up["Interest"].cumsum()
    df_up["Cumulative Principal"] = df_up["Principal"].cumsum()

    df_down["Cumulative Interest"] = df_down["Interest"].cumsum()
    df_down["Cumulative Principal"] = df_down["Principal"].cumsum()

    info = {"Loan Amount": loan_amt, "Interest Rate": ir, "Periods": periods,
            "Total Interest": df.at[periods, "Cumulative Interest"]}
    info_df = pd.DataFrame.from_dict(data=info, orient='index')
    info_df.columns = ["Normal"]

    info_up = {"Loan Amount": loan_amt, "Interest Rate": ir_up, "Periods": periods,
               "Total Interest": df_up.at[periods, "Cumulative Interest"]}
    info_df_up = pd.DataFrame.from_dict(data=info_up, orient='index')
    info_df_up.columns = ["50 basis points up"]

    info_down = {"Loan Amount": loan_amt, "Interest Rate": ir_down, "Periods": periods,
                 "Total Interest": df_down.at[periods, "Cumulative Interest"]}
    info_df_down = pd.DataFrame.from_dict(data=info_down, orient='index')
    info_df_down.columns = ["50 basis points down"]


    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    writer = pd.ExcelWriter(source_file, engine='xlsxwriter')

    with open(source_file, "rb") as f:
        info_df.to_excel(writer, sheet_name="AM Schedule", startcol=1, startrow=1)
        df.to_excel(writer, sheet_name="AM Schedule", startcol=3, startrow=6)

        info_df_up.to_excel(writer, sheet_name="AM Schedule - Higher Interest", startcol=1, startrow=1)
        df_up.to_excel(writer, sheet_name="AM Schedule - Higher Interest", startcol=3, startrow=6)

        info_df_down.to_excel(writer, sheet_name="AM Schedule - Lower Interest", startcol=1, startrow=1)
        df_down.to_excel(writer, sheet_name="AM Schedule - Lower Interest", startcol=3, startrow=6)
        writer.save()

        writer.save()
        #workbook.close()


    writer.save()
    writer.close()


    st.table(df, use_container_width=False)

    with open(source_file, "rb") as final:
        st.download_button("Upload variance analysis", data=final, file_name="AM Schedule.xlsx", mime='xlsx')

    #  df = opt.root(AMbuild(df), df.at[periods, "Ending Balance"]==0)



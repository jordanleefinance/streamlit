import pandas as pd
import streamlit as st
import datetime

def get_monthly_pmt(loan_amt, r, n):
    """ calculate monthly payment
    loan_amt: initial loan amount
    r: monthly interest
    n: total number of payments
    """
    return loan_amt * r * (1 + r) ** n / ((1 + r) ** n - 1)








with st.form("Loan Details"):
    st.write("Please provide the following:")
    loan_amt = st.number_input("Loan Amount", step=1)
    interest = st.number_input("Interest Rate", step=0.0001, format="%i")
    pper = st.number_input("Payments per Period", value=12)
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")

    periods = end_date.year - start_date.year * pper
    print(periods)
    button = st.form_submit_button("Submit")
    if button:
        get_monthly_pmt(loan_amt, interest, periods)

def get_principle(loan_amt, A, r, t):
    """ calculate principle for month t
    loan_amt: intial loan amount
    A: monthly payment
    r: monthly intrest
    t: number of payments
    """
    return loan_amt * ((1 + r) ** t) - A * ((1 + r) ** t - 1) / r


def get_schedule(loan_amt, r, n):
    """ calculate the amortization schedule
    loan_amt: intial loan amount
    r: monthly intrest
    n: total number of payments
    """
    monthly = []
    A = get_monthly_pmt(loan_amt, r, n)
    last = loan_amt
    for i in range(1, n + 1):
        curr = get_principle(loan_amt, A, r, i)
        p = last - curr
        monthly.append([i, p, A - p, curr])
        last = curr
    return pd.DataFrame(monthly, columns=['month', 'principle_pmt', 'interest_pmt', 'principle'])

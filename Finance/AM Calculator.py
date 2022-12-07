import pandas as pd
import streamlit as st



def get_monthly_pmt(loan_amt, r, n):
    """ calculate monthly payment
    loan_amt: initial loan amount
    r: monthly interest
    n: total number of payments
    """
    return loan_amt * r * (1 + r) ** n / ((1 + r) ** n - 1)


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

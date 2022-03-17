import pandas as pd
import webbrowser
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

file_path = r'C:/Users/JordanLee/OneDrive/Documents/MFinA/' \
            r'FINC 591 - Integrated Financial Analysis & Strategy/' \
            r'NNPS - Capstone/Compensation Package.xlsx'


st.sidebar.subheader("""City of Newport News Compensation Package""")
user_name = st.sidebar.text_input("Name", "")
user_jobtitle = st.sidebar.text_input("Job Title", "")
user_jobtype = st.sidebar.text_input("Job Type", "Full Time")
user_salary = st.sidebar.number_input("Enter your hourly/annual pay:")
user_coverage = st.sidebar.selectbox("Coverage", ("Employee", "Employee + 1 Child", "Employee + Spouse", "Family"))
user_health_plan = st.sidebar.selectbox("Health Plan", ('Optima Health POS', 'Optima Health POS + FSA',
                           'Optima Equity HDHP', 'Optima Equity HDHP + FSA', 'Optima Equity HDHP + HSA', 'None'))
user_dental_plan = st.sidebar.selectbox("Dental Plan", ('Delta Dental', 'None'))
user_vision_plan = st.sidebar.selectbox("Vision Plan", ('Vision Service Plan', 'Vision INS City', 'None'))
user_hire_date = st.sidebar.selectbox("Hire Date", ('On or After March 1, 2010', 'Before March 1, 2010'))
button_clicked = st.sidebar.button("GO")


def open_excel(file = None):
    if file == None:
        file = file_path
    return webbrowser.open_new(file)

def open_excel_error():
    st.error('Error', 'Please close the file and revalue to see changes.\n\n'
                      'Compare compensation packages change file name, close the file, and revalue.')


def employee_part_time():
    value = 0
    salary = user_salary
    monthly_value = 0
    weekly_pay = 0
    job_title = user_jobtitle
    try:
        hourly_pay = float(salary)
        weekly_pay = float(hourly_pay * 37)
        monthly_value = float(weekly_pay * 4)
        value += (weekly_pay * 52)

    except ValueError:
        open_excel_error()

    fig = plt.figure(figsize=(18, 10.5), dpi=68)
    fig.tight_layout()
    fig.set_facecolor('grey')
    fig.suptitle('A(n) {:s} at NNVA earns ${:,.2f} yearly.\n'
                 'A(n) {:s} at NNVA earns ${:,.2f} monthly.\n'
                 'A(n){:s} at NNVA earns ${:,.2f} weekly.'.format(job_title, value, job_title, monthly_value, job_title, weekly_pay),
                 x=0.5, y=0.5, fontweight='bold', fontsize=30)

    st.pyplot(fig)

def employee():
    ymca_cost = 0
    ymca_nnva_cost = 0
    ymca_benefit = 0
    one_cost = 0
    one_nnva_cost = 0
    one_benefit = 0
    riv_cost = 0
    riv_nnva_cost = 0
    riv_benefit = 0
    value = 0
    monthly_value = 0
    info_dict = {}
    monthly_info_dict = {}
    #labels = []
    colors = ['lightblue', 'white', 'orange', 'green', 'purple', 'blue', 'lightgreen']
    explode = [0.02, 0.012, 0.012, 0.012, 0.0012, 0.0012, 0.0012]
    name = user_name
    job_title = user_jobtitle
    job_type = user_jobtype
    salary = user_salary
    coverage = user_coverage
    health_plan = user_health_plan
    den_plan = user_dental_plan
    vis_plan = user_vision_plan
    hire_date = user_hire_date
    print(user_health_plan)
    ret_plan = ''
    ret_message = ''
    life_message = ''

    if hire_date == 'Hire Date':
        ret_plan = 'VRS'
        ret_message = 'This plan consists of full-time re-hires and employees' \
                      'hired on or after March 1, 2010,\nand those prior active full-time employees who opted to change ' \
                      'to VRS.\nFor additional information, please refer to www.varetire.org'


    # job type test
    if job_type == 'Part Time':
        employee_part_time()
        return None # reset to default ticket

    # name test
    if name != '':
        name += '\'s'

    # no salary test

    try:
        monthly_value += salary / 12
        value += salary
        info_dict['Annual Salary'] = float(salary)
        monthly_info_dict['Monthly Salary'] = float(salary) / 12

    except AttributeError:
        print("error")
        pass
    if salary == 0:
        monthly_value += float(salary) / 12
        value += float(salary)
        info_dict['Annual Salary'] = float(salary)
        monthly_info_dict['Monthly Salary'] = float(salary) / 12

    if coverage == 'Employee':
        ymca_cost = 49.00
        ymca_nnva_cost = 30.00
        ymca_benefit = ymca_cost - ymca_nnva_cost
        one_cost = 39.99
        one_nnva_cost = 25.00
        one_benefit = one_cost - one_nnva_cost
        riv_cost = 50.00
        riv_nnva_cost = 28.00
        riv_benefit = riv_cost - riv_nnva_cost

    if coverage == 'Employee + 1 Child':
        ymca_cost = 64.00
        ymca_nnva_cost = 53.00
        ymca_benefit = ymca_cost - ymca_nnva_cost
        one_cost = 79.98
        one_nnva_cost = 50.00
        one_benefit = one_cost - one_nnva_cost
        riv_cost = 75.00
        riv_nnva_cost = 51.00
        riv_benefit = riv_cost - riv_nnva_cost

    if coverage == 'Family':
        ymca_cost = 79.00
        ymca_nnva_cost = 58.00
        ymca_benefit = ymca_cost - ymca_nnva_cost
        one_cost = 159.96
        one_nnva_cost = 89.00
        one_benefit = one_cost - one_nnva_cost
        riv_cost = 100.00
        riv_nnva_cost = 79.00
        riv_benefit = riv_cost - riv_nnva_cost

    if coverage == 'Employee + Spouse':
        ymca_cost = 98.00
        ymca_nnva_cost = 50.00
        ymca_benefit = ymca_cost - ymca_nnva_cost
        one_cost = 79.98
        one_nnva_cost = 50.00
        one_benefit = one_cost - one_nnva_cost
        riv_cost = 75.00
        riv_nnva_cost = 56.00
        riv_benefit = riv_cost - riv_nnva_cost

    if health_plan == 'Optima Health POS':
        if coverage == 'Employee':
            monthly_value += 546.35
            value += 546.35 * 12
            monthly_info_dict[health_plan] = 546.35
            info_dict[health_plan] = 546.35 * 12
        elif coverage == 'Employee + 1 Child':
            monthly_value += 861.69
            value += 861.69 * 12
            monthly_info_dict[health_plan] = 861.69
            info_dict[health_plan] = 861.69 * 12
        elif coverage == 'Family':
            monthly_value += 1493.78
            value += 1493.78 * 12
            monthly_info_dict[health_plan] = 1493.78
            info_dict[health_plan] = 1493.78 * 12
        elif coverage == 'Employee + Spouse':
            monthly_value += 1114.82
            value += 1114.82 * 12
            monthly_info_dict[health_plan] = 1114.82
            info_dict[health_plan] = 1114.82 * 12

    if health_plan == 'Optima Equity HDHP':
        if coverage == 'Employee':
            monthly_value += 527.54
            value += 527.54 * 12
            monthly_info_dict[health_plan] = 527.54
            info_dict[health_plan] = 527.54 * 12
        elif coverage == 'Employee + 1 Child':
            monthly_value += 836.47
            value += 836.47 * 12
            monthly_info_dict[health_plan] = 836.47
            info_dict[health_plan] = 836.47 * 12
        elif coverage == 'Family':
            monthly_value += 1417.11
            value += 1417.11 * 12
            monthly_info_dict[health_plan] = 1417.11
            info_dict[health_plan] = 1417.11 * 12
        elif coverage == 'Employee + Spouse':
            monthly_value += 1076.19
            value += 1076.19 * 12
            monthly_info_dict[health_plan] = 1076.19
            info_dict[health_plan] = 1076.19 * 12

    if health_plan == 'Optima Health POS + FSA':
        if coverage == 'Employee':
            monthly_value += 479.43
            monthly_value += (2750 * .22) / 13 # Tax Benefit
            value += 479.43 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 479.43 + ((2750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (479.43 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

        elif coverage == 'Employee + 1 Child':
            monthly_value += 861.69
            monthly_value += (7750 * .22) / 13# Tax Benefit
            value += 861.69 * 12
            value += (7750 * .22)
            monthly_info_dict[health_plan] = 861.69 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)
            info_dict[health_plan] = ((861.69 * 12) + (7750 * .22))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif coverage == 'Family':
            monthly_value += 1493.78
            monthly_value += (7750 * .22) / 13# Tax Benefit
            value += 1493.78 * 12
            value += (7750 * .22)
            monthly_info_dict[health_plan] = 1493.78 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22) / 13
            info_dict[health_plan] = ((7750 * .22) + (1493.78 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif coverage == 'Employee + Spouse':
            monthly_value += 1114.82
            monthly_value += (2750 * .22) / 13
            value += 1114.82 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 1114.82 + 62.50
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (1114.82 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

    if health_plan == 'Optima Equity HDHP + FSA':
        if coverage == 'Employee':
            monthly_value += 527.54
            monthly_value += (2750 * .22) / 13
            value += 527.54 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 527.54 + ((2750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (527.54 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

        elif coverage == 'Employee + 1 Child':
            monthly_value += 836.47
            monthly_value += (7750 * .22)/13
            value += 836.47 * 12
            value += (7750 * .22) / 13
            monthly_info_dict[health_plan] = 836.47 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22) / 13
            info_dict[health_plan] = ((836.47 * 12) + (7750 * .22))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif coverage == 'Family':
            monthly_value += 1417.11
            monthly_value += (7750 * .22) / 13 # Tax Benefit
            value += 1417.11 * 12
            value += (7750 * .22)
            monthly_info_dict[health_plan] = 1417.11 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22) / 13
            info_dict[health_plan] = ((7750 * .22) + (1417.11 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif coverage == 'Employee + Spouse':
            monthly_value += 1076.19
            monthly_value += (2750 * .22) / 13
            value += 1076.19 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 1076.19 + ((2750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (1076.19 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

    if health_plan == 'Optima Equity HDHP + HSA':
        if coverage == 'Employee':
            monthly_value += 527.54
            monthly_value += 62.50
            value += (527.54 + 62.50) * 12
            monthly_info_dict[health_plan] = 527.54 + 62.50
            monthly_info_dict['Health Savings Account (HSA)'] = 62.50
            info_dict[health_plan] = (62.50 + 527.54) * 12
            info_dict['Health Savings Account (HSA)'] = 62.50 * 12

        elif coverage == 'Employee + 1 Child':
            monthly_value += 836.47
            monthly_value += 125
            value += (836.47 + 125) * 12
            monthly_info_dict[health_plan] = 836.47 + 125
            monthly_info_dict['Health Savings Account (HSA)'] = 125
            info_dict[health_plan] = (836.47 + 125) * 12
            info_dict['Health Savings Account (HSA)'] = 125 * 12

        elif coverage == 'Family':
            monthly_value += 1417.11 + 125
            value += (1417.11 + 125) * 12
            monthly_info_dict[health_plan] = 1417.11 + 125
            monthly_info_dict['Health Savings Account (HSA)'] = 125
            info_dict[health_plan] = (1417.11 + 125) * 12
            info_dict['Health Savings Account (HSA)'] = 125 * 12

        elif coverage == 'Employee + Spouse':
            monthly_value += 1076.19 + 125
            value += (1076.19 + 125) * 12
            monthly_info_dict[health_plan] = 1076.19 + 125
            monthly_info_dict['Health Savings Account (HSA)'] = 125
            info_dict[health_plan] = (1076.19 + 125) * 12
            info_dict['Health Savings Account (HSA)'] = 125 * 12

    if den_plan == 'Delta Dental':
        if coverage == 'Employee':
            monthly_value += 21.42
            value += 21.42* 12
            monthly_info_dict[den_plan] = 21.42
            info_dict[den_plan] = 21.42 * 12
        elif coverage == 'Employee + 1 Child':
            monthly_value += 38.92
            value += 38.92 * 12
            monthly_info_dict[den_plan] = 38.92
            info_dict[den_plan] = 38.92 * 12
        elif coverage == 'Family' or coverage == 'Employee + Spouse':
            monthly_value += 66.91
            value += 66.91 * 12
            monthly_info_dict[den_plan] = 66.91
            info_dict[den_plan] = 66.91 * 12

    if vis_plan == 'Vision Service Plan':
        if coverage == 'Employee':
            monthly_value += 1
            value += 1 * 12
            monthly_info_dict[vis_plan] = 1
            info_dict[vis_plan] = 1 * 12
        elif coverage == 'Employee + 1 Child':
            monthly_value += 2
            value += 2 * 12
            monthly_info_dict[vis_plan] = 2
            info_dict[vis_plan] = 2 * 12
        elif coverage == 'Family':
            monthly_value += 2
            value += 2 * 12
            monthly_info_dict[vis_plan] = 2
            info_dict[vis_plan] = 2 * 12
        elif coverage == 'Employee + Spouse':
            monthly_value += 2
            value += 2 * 12
            monthly_info_dict[vis_plan] = 2
            info_dict[vis_plan] = 2 * 12

    if vis_plan == 'Vision INS City':
        if coverage == 'Employee':
            monthly_value += 0.8
            value += 0.8 * 12
            monthly_info_dict[vis_plan] = 0.8
            info_dict[vis_plan] = 0.8 * 12
        else:
            monthly_value += 0
            value += 0 * 12
            monthly_info_dict[vis_plan] = 0
            info_dict[vis_plan] = 0 * 12

    # Initialize Add'tl Benefits Ticket
    benefits_title = 'Additional Benefits'
    benefits_title = "\u0332".join(benefits_title)
    text = "\nFitness Benefits\n" \
               "YMCA Benefit: ${:.2f} monthly\n" \
               "Original: ${:.2f}\n" \
               "NNVA rate: ${:.2f}\n" \
               "One Life Fitness Benefit: ${:.2f} monthly\n" \
               "Original: ${:.2f}\n" \
               "NNVA rate: ${:.2f}\n" \
               "Riverside Fitness Center Benefit: ${:.2f} monthly\n" \
               "Original: ${:.2f}\n" \
               "NNVA rate: ${:.2f}\n" \
               "\nDisability Benefits:\n" \
               "Short Term Disability (STD)\n" \
               "Employee purchases coverage: 60%\n" \
               "Benefit Waiting Period: 14 days\n" \
               "Maximum Benefit Period: 90 days then to LTD\n" \
               "Long Term Disability (LTD)\n" \
               "City provided core coverage: 40%\n" \
               "Employee buy up: 10%\n" \
               "Benefit Waiting Period: After 90 days\n" \
               "\n\n" \
               "{:s}\n" \
               "\n\n" \
               "{:s}".format(ymca_benefit, ymca_cost, ymca_nnva_cost,
                             one_benefit, one_cost, one_nnva_cost,
                             riv_benefit, riv_cost, riv_nnva_cost,
                             ret_message, life_message)



    df_annual = pd.DataFrame.from_dict(data=info_dict, orient='index', columns=['Annual Compensation Package'])
    df_monthly = pd.DataFrame.from_dict(data=monthly_info_dict, orient='index',
                                        columns=['Monthly Compensation Package'])
    main_df = pd.concat([df_annual, df_monthly], axis=1)
    main_df.fillna(0, inplace=True)
    main_df = main_df.applymap(lambda x: "${:,.2f}".format(x),
                               na_action='ignore')
    st.write("### {:s} Total Compensation Package".format(name), main_df)

    return df_annual, df_monthly, text, benefits_title


user = employee()

df = user[0]
monthly_df = user[1]

df = df.T.reset_index()
df = pd.melt(df, id_vars=["index"]).rename(
            columns={"index": "attributes", "variable":"Benefits"}
        )
chart1 = alt.Chart(df).encode(
    theta=alt.Theta('value:Q', stack=True),
    color="Benefits:N"
).properties(title="Annual Compensation Package")
pie1 = chart1.mark_arc(outerRadius=70)
pie1_text = chart1.mark_text(align='center', radius=110, size=9).encode(text="Benefits:N")
st.altair_chart(pie1 + pie1_text, use_container_width=True)
df = user[0]
df = df.applymap(lambda x: "${:,.2f}".format(x),
                           na_action='ignore')
st.write("### Annual Compensation Package", df)



monthly_df = monthly_df.T.reset_index()
monthly_df = pd.melt(monthly_df, id_vars=["index"]).rename(
            columns={"index": "attributes", "variable":"Benefits"}
        )
chart2 = alt.Chart(monthly_df).encode(
    theta=alt.Theta('value:Q', stack=True),
    color="Benefits:N"
).properties(title="Monthly Compensation Package")
pie2 = chart2.mark_arc(outerRadius=70)
pie2_text = chart2.mark_text(align='center', radius=110, size=9).encode(text="Benefits:N")

monthly_df = user[1]
monthly_df = monthly_df.applymap(lambda x: "${:,.2f}".format(x),
                                           na_action='ignore')
st.altair_chart(pie2 + pie2_text, use_container_width=True)
st.write("### Monthly Compensation Package", monthly_df)

benefits_subtitle = user[3]
st.subheader(benefits_subtitle)

st.text(user[2])

if button_clicked == 'GO':
    employee()



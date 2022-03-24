import pandas as pd
import webbrowser
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt
import os

start = r"C:\Users\data\Sampledata.xlsx"
path1 = r"C:\Users\data"

path = r"C:\Users\jorda\OneDrive\Documents\GitHub\streamlit\Sampledata.xlsx"
DB_path = os.path.join(path1, "Sampledata.xlsx")


@st.cache
def load_data():
    df = pd.read_excel(path, index_col=[1, 2], header=[2], sheet_name=None)
    df1 = pd.concat(df.values(), axis=0)
    df1 = df1[:8]
    return df1


file_path = r'C:/Users/JordanLee/OneDrive/Documents/MFinA/' \
            r'FINC 591 - Integrated Financial Analysis & Strategy/' \
            r'NNPS - Capstone/Compensation Package.xlsx'

st.sidebar.subheader("""**City of Newport News Compensation Package**""")
user_name = st.sidebar.text_input("Name", "Jetson George")
user_jobtitle = st.sidebar.selectbox("Job Title", ("Treasurer", 'Fire', 'Police',
                                                   'Finance', 'Human Resources',
                                                   'Engineering', 'Libraries', 'Information Technology'))
user_jobtype = st.sidebar.radio("Job Type", ["Full Time", "Part Time"])
user_salary = st.sidebar.number_input("Enter your hourly/annual pay:", value=80857.45)
user_coverage = st.sidebar.selectbox("Coverage", ("Employee", "Employee + 1 Child", "Employee + Spouse", "Family"))
user_health_plan = st.sidebar.selectbox("Health Plan", ('Optima Health POS', 'Optima Health POS + FSA',
                                                        'Optima Equity HDHP', 'Optima Equity HDHP + FSA',
                                                        'Optima Equity HDHP + HSA', 'None'))
user_dental_plan = st.sidebar.radio('Dental Plan', ['Delta Dental', 'None'])
user_vision_plan = st.sidebar.radio("Vision Plan", ['Vision Service Plan', 'Vision INS City', 'None'])

file = st.sidebar.file_uploader("Upload Database:", 'xlsx')
button_clicked = st.sidebar.button("GO")
try:
    df = load_data()
except FileNotFoundError:
    if file:
        df2 = pd.read_excel(file, index_col=[1, 2], header=[2], sheet_name=None)
        df1 = pd.concat(df2.values(), axis=0)
        df = df1[:8]
    elif file is None:
        st.error("Please upload a database in the sidebar to calculate entire package.")
        pass

PPL_data = [['Up to 5 years in service', "6 hours", "9.25 hours"],
            ['Over 5 years in service', "7.5 hours", "11.75 hours"],
            ['Over 10 years in service', "8.5 hours", "12.5 hours"],
            ['Over 15 years in service', "9 hours", "13 hours"],
            ['Over 20 years in service', "9.25 hours", "14 hours"]]

PPL_df = pd.DataFrame(PPL_data, columns=['YEARS OF SERVICE', 'FULL-TIME EMPLOYEES', '24-HOUR FIRE EMPLOYEES*'])


def open_excel(file=None):
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
    fig.set_facecolor('white')
    fig.suptitle('A(n) {:s} at NNVA earns ${:,.2f} yearly.\n\n'
                 'A(n) {:s} at NNVA earns ${:,.2f} monthly.\n\n'
                 'A(n){:s} at NNVA earns ${:,.2f} weekly.'.format(job_title, value, job_title, monthly_value, job_title,
                                                                  weekly_pay),
                 x=0.5, y=0.5, fontweight='bold', fontsize=30)

    st.pyplot(fig)
    pass


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
    labels = []
    monthly_labels = []
    colors = ['lightblue', 'firebrick', 'goldenrod', 'hotpink', 'green', 'purple', 'orange', 'blue', 'lightgreen',
              'lightcyan', 'violet']
    explode = [0.002, 0.152, 0.252, 0.392, 0.452, 0.532, 0.622, 0.712, 0.805, 0.905, 0.95, 1.05]
    name = user_name
    first_name = ''
    last_name = ''
    job_title = user_jobtitle.upper()
    job_type = user_jobtype
    salary = user_salary
    coverage = user_coverage
    health_plan = user_health_plan
    den_plan = user_dental_plan
    vis_plan = user_vision_plan
    ret_plan = ''
    lt_dis_plan = 'Long Term Dis.'
    ret_health_plan = 'Retiree Health'
    life_plan = 'Basic Life'

    # job type test
    if job_type == 'Part Time':
        employee_part_time()
        return None  # reset to default ticket

    # name test
    if name != '':
        first_name = name.split()[0]
        try:
            last_name = name.split()[1]
        except IndexError:
            pass
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
            monthly_value += (2750 * .22) / 13  # Tax Benefit
            value += 479.43 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 479.43 + ((2750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (479.43 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

        elif coverage == 'Employee + 1 Child':
            monthly_value += 861.69
            monthly_value += (7750 * .22) / 13  # Tax Benefit
            value += 861.69 * 12
            value += (7750 * .22)
            monthly_info_dict[health_plan] = 861.69 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)
            info_dict[health_plan] = ((861.69 * 12) + (7750 * .22))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif coverage == 'Family':
            monthly_value += 1493.78
            monthly_value += (7750 * .22) / 13  # Tax Benefit
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
            monthly_value += (7750 * .22) / 13
            value += 836.47 * 12
            value += (7750 * .22) / 13
            monthly_info_dict[health_plan] = 836.47 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22) / 13
            info_dict[health_plan] = ((836.47 * 12) + (7750 * .22))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif coverage == 'Family':
            monthly_value += 1417.11
            monthly_value += (7750 * .22) / 13  # Tax Benefit
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
            value += 21.42 * 12
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
            monthly_value += 1.8
            value += 1.8 * 12
            monthly_info_dict[vis_plan] = 1.8
            info_dict[vis_plan] = 1.8 * 12
        elif coverage == 'Employee + 1 Child':
            monthly_value += 2.8
            value += 2.8 * 12
            monthly_info_dict[vis_plan] = 2.8
            info_dict[vis_plan] = 2.8 * 12
        elif coverage == 'Family':
            monthly_value += 2.8
            value += 2.8 * 12
            monthly_info_dict[vis_plan] = 2.8
            info_dict[vis_plan] = 2.8 * 12
        elif coverage == 'Employee + Spouse':
            monthly_value += 2.8
            value += 2.8 * 12
            monthly_info_dict[vis_plan] = 2.8
            info_dict[vis_plan] = 2.8 * 12

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
    try:
        for i in range(len(df)):
            if df.iloc[i].name == (last_name, first_name) or \
                    df.iloc[i].loc['Location Code Desc'] == job_title:
                ret_plan = df.iloc[i].loc['Retirement Plan']

                if ret_plan == 'NNER  CITY OF NEWPORT NEWS RET':
                    ret_plan = 'NNER - City of Newport News Ret'
                elif ret_plan == 'VRS - VIRGINIA RETIREMENT SYST':
                    ret_plan = 'VRS - Virginia Retirement System'
                elif ret_plan == 'VRSH - VIRGINIA RET SYS HYBRID':
                    ret_plan = 'VRSH - Virginia Retirement System Hybrid'

                user_data = df.iloc[i].loc['DB Retirement City']
                monthly_value += user_data.astype(float)
                value += user_data.astype(float) * 12
                monthly_info_dict[ret_plan] = user_data.astype(float)
                info_dict[ret_plan] = float(user_data) * 12

                lt_dis_data = df.iloc[i].loc['LTD City']
                monthly_value += float(lt_dis_data)
                value += float(lt_dis_data) * 12
                monthly_info_dict[lt_dis_plan] = float(lt_dis_data)
                info_dict[lt_dis_plan] = float(lt_dis_data) * 12

                retiree_data = df.iloc[i].loc['OPEB City or HRA City']
                monthly_value += float(retiree_data)
                value += float(retiree_data) * 12
                monthly_info_dict[ret_health_plan] = float(retiree_data)
                info_dict[ret_health_plan] = float(retiree_data) * 12

                life_data = df.iloc[i].loc['Life City']
                monthly_value += float(life_data)
                value += float(life_data) * 12
                monthly_info_dict[life_plan] = float(life_data)
                info_dict[life_plan] = float(life_data) * 12

                if ret_plan == 'VRSH - Virginia Retirement System Hybrid':
                    hybrid_data = df.iloc[i].loc['DC Plan City']
                    monthly_value += float(hybrid_data)
                    value += float(hybrid_data) * 12
                    monthly_info_dict['Hybrid Mandatory'] = float(hybrid_data)
                    info_dict['Hybrid Mandatory'] = float(hybrid_data) * 12

                    hybrid_optional_data = df.iloc[i].loc['Opt DC City']
                    print(hybrid_optional_data)
                    monthly_value += float(hybrid_optional_data)
                    value += float(hybrid_optional_data) * 12
                    monthly_info_dict['Hybrid Mandatory (Optional)'] = float(hybrid_optional_data)
                    info_dict['Hybrid Mandatory (Optional)'] = float(hybrid_optional_data) * 12

                    VLDP_data = df.iloc[i].loc['VLDP City']
                    monthly_value += float(VLDP_data)
                    value += float(VLDP_data) * 12
                    monthly_info_dict['Disability (Hybrid Only)'] = float(VLDP_data)
                    info_dict['Disability (Hybrid Only)'] = float(VLDP_data) * 12
    except NameError:
        pass

    for key, val in list(info_dict.items()):
        if val > 0:
            labels.append(key)
        else:
            info_dict.pop(key)

    for mkey, mval in list(monthly_info_dict.items()):
        if mval > 0:
            monthly_labels.append(mkey)
        else:
            monthly_info_dict.pop(mkey)

    for j in range(len(labels)):
        if labels[j] == "Flexible Spending Account (FSA)":
            labels[j] = "FSA"
        if labels[j] == "Health Savings Account (HSA)":
            labels[j] = "HSA"
        if labels[j] == health_plan:
            labels[j] = "Health"
        if labels[j] == den_plan:
            labels[j] = "Dental"
        if labels[j] == vis_plan:
            labels[j] = "Vision"
        if labels[j] == ret_plan:
            labels[j] = "Retirement"
        if labels[j] == life_plan:
            labels[j] = "Life"

    for mj in range(len(monthly_labels)):
        if monthly_labels[mj] == "Flexible Spending Account (FSA)":
            monthly_labels[mj] = "FSA"
        if monthly_labels[mj] == "Health Savings Account (HSA)":
            monthly_labels[mj] = "HSA"
        if monthly_labels[mj] == health_plan:
            monthly_labels[mj] = "Health"
        if monthly_labels[mj] == den_plan:
            monthly_labels[mj] = "Dental"
        if monthly_labels[mj] == vis_plan:
            monthly_labels[mj] = "Vision"
        if monthly_labels[mj] == ret_plan:
            monthly_labels[mj] = "Retirement"
        if monthly_labels[mj] == life_plan:
            monthly_labels[mj] = "Life"

    # Graph results
    # Set figure and axis with 2 pie charts

    fig1, ax1 = plt.subplots(figsize=(12, 9))
    fig1.tight_layout()
    fig1.set_facecolor('white')

    ax1.pie(info_dict.values(), explode=explode[:len(info_dict.values())],
            labels=labels,
            colors=colors[:len(info_dict.values())], autopct='%1.1f%%', startangle=190,
            pctdistance=0.7, labeldistance=1.05, radius=0.83)

    ax1.legend(labels=[str('{:s}, ${:,.2f}').format(i, j) for i, j in zip(info_dict.keys(), info_dict.values())],
               shadow=True, loc=(0.8, 0.75), fontsize=10)

    ax1.set_title('{:s} Annual Compensation Package\n {:s}'.format(name, job_title.capitalize()), fontweight='bold',
                  fontsize=30)

    fig1.suptitle('A(n) {:s} at NNVA earns ${:,.2f} yearly\n'
                  'Health Plan: {:s}\n'
                  'Dental Plan: {:s}\n'
                  'Vision Plan: {:s}\n'
                  'Retirement Plan: {:s}\n'
                  'Life Plan: {:s}'.format(job_title.capitalize(), float(value),
                                           health_plan, den_plan, vis_plan, ret_plan, life_plan),
                  x=0.521, y=0.15, fontsize=17)

    fig2, ax2 = plt.subplots(figsize=(18.5, 12.5))
    fig2.tight_layout()
    fig2.set_facecolor('white')

    ax2.pie(monthly_info_dict.values(), explode=explode[:len(monthly_info_dict.values())],
            labels=monthly_labels,
            colors=colors[:len(monthly_info_dict.values())], autopct='%1.1f%%', startangle=190,
            pctdistance=0.7, labeldistance=1.05, radius=0.65)

    ax2.legend(labels=[str('{:s}, ${:,.2f}').format(i, float(j)) for i, j in
                       zip(monthly_info_dict.keys(), monthly_info_dict.values())],
               shadow=True, loc=(0.65, 0.75), fontsize=13)

    ax2.set_title('{:s} Monthly Compensation Package\n {:s}'.format(name, job_title.capitalize()), fontweight='bold',
                  fontsize=25)

    fig2.suptitle('A(n) {:s} at NNVA earns ${:,.2f} monthly\n'
                  'Health Plan: {:s}\n'
                  'Dental Plan: {:s}\n'
                  'Vision Plan: {:s}\n'
                  'Retirement Plan: {:s}\n'
                  'Life Plan: {:s}'.format(job_title.capitalize(), float(monthly_value),
                                           health_plan, den_plan, vis_plan, ret_plan, life_plan),
                  x=0.521, y=0.18, fontsize=15)

    # Initialize Add'tl Benefits Ticket
    benefits_title = '**Additional Benefits**'
    text1 = "\n**FITNESS BENEFITS**\n" \
            "YMCA Benefit: ${:.2f} monthly\n" \
            "\tOriginal: ${:.2f}\n" \
            "\tNNVA rate: ${:.2f}\n" \
            "One Life Fitness Benefit: ${:.2f} monthly\n" \
            "\tOriginal: ${:.2f}\n" \
            "\tNNVA rate: ${:.2f}\n" \
            "Riverside Fitness Center Benefit: ${:.2f} monthly\n" \
            "\tOriginal: ${:.2f}\n" \
            "\tNNVA rate: ${:.2f}\n" \
            "\n**DISABILITY BENEFITS**\n" \
            "Short Term Disability (STD)\n" \
            "\tEmployee purchases coverage: 60%\n" \
            "\tBenefit Waiting Period: 14 days\n" \
            "\tMaximum Benefit Period: 90 days then to LTD\n" \
            "Long Term Disability (LTD)\n" \
            "\tCity provided core coverage: 40%\n" \
            "\tEmployee buy up: 10%\n" \
            "\tBenefit Waiting Period: After 90 days\n" \
            "\n**PAID HOLIDAYS**\n Regular, full-time City employees are eligible for paid holidays,\n provided they are in an active " \
            "pay status the working day prior to the holiday.\n\t• New Year’s Day (January 1)\n\t• Dr. Martin Luther King’s Birthday (Third Monday in January)\n" \
            "\t• President’s Day & George Washington’s Birthday (Third Monday in February)\n" \
            "\t• Memorial Day (Last Monday in May)\n" \
            "\t• Juneteenth (June 19)\n" \
            "\t• Independence Day (July 4)\n" \
            "\t• Labor Day (First Monday in September)\n" \
            "\t• Veterans Day (November 11)\n" \
            "\t• Thanksgiving Day (Fourth Thursday in November)\n" \
            "\t• The Friday following Thanksgiving Day\n" \
            "\t• Christmas Eve (December 24) – Observed as four hours only, and provided\n\tthat December 24 falls during the normal Monday through Friday work week\n" \
            "\t• Christmas Day (December 25)\n\n".format(ymca_benefit, ymca_cost, ymca_nnva_cost,
                                                         one_benefit, one_cost, one_nnva_cost,
                                                         riv_benefit, riv_cost, riv_nnva_cost)

    df_annual = pd.DataFrame.from_dict(data=info_dict, orient='index', columns=['Annual Compensation Package'])
    df_annual.loc['Total'] = value
    df_monthly = pd.DataFrame.from_dict(data=monthly_info_dict, orient='index',
                                        columns=['Monthly Compensation Package'])
    df_monthly.loc['Total'] = monthly_value
    main_df = pd.concat([df_annual, df_monthly], axis=1)
    main_df = main_df.applymap(lambda x: "${:,.2f}".format(float(x)),
                               na_action='ignore')
    main_df.fillna("", inplace=True)

    return df_annual, df_monthly, main_df, text1, benefits_title, fig1, fig2


try:
    user = employee()
    df = user[0]
    monthly_df = user[1]
    total_df = user[2]
    text = user[3]
    benefits_title = user[4]
    annual_fig = user[5]
    monthly_fig = user[6]

    st.pyplot(annual_fig)
    df = df.applymap(lambda x: "${:,.2f}".format(float(x)),
                     na_action='ignore')
    st.table(df)

    st.pyplot(monthly_fig)
    monthly_df = monthly_df.applymap(lambda x: "${:,.2f}".format(float(x)),
                                     na_action='ignore')
    st.table(monthly_df)
    st.header(benefits_title)

    st.text(text)
    st.subheader(
        "**PAID PERSONAL LEAVE (PPL)**\nPaid personal leave covers vacation, absences for personal business and"
        "\nsome medical leave. Regular, full-time employees and 24-hour "
        "fire employees\nearn PPL according to the following bi-weekly accrual schedule:")
    st.table(PPL_df.set_index('YEARS OF SERVICE'))
    st.subheader("\n**PAID MEDICAL LEAVE (PML)**\n"
                 "Paid medical leave can be used for certain personal "
                 "and family\nmedical-related absences. Regular, full-time employees accrue 2.75 hours\n"
                 "bi-weekly and 24-hour fire employees accrue 7.5 hours bi-weekly.")
except TypeError:
    pass
if button_clicked == 'GO':
    employee()

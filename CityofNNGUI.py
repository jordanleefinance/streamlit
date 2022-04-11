import pandas as pd
import webbrowser
import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from openpyxl import load_workbook
import os

start = r"C:\Users\data\Sampledata.xls"
path1 = r"C:\Users\data"

path = r"C:\Users\jorda\OneDrive\Documents\GitHub\streamlit\Sampledata.xlsx"
DB_path = os.path.join(path1, "Sampledata.xlsx")

@st.cache
def load_data():
    df = pd.read_excel(start, index_col=[1, 2], header=[2], sheet_name='Sheet1')
    df1 = pd.concat(df.values, axis=0)
    df1 = df1[:8]
    return df1


try:
    workbook = load_workbook(filename="Sampledata.xlsx", data_only=True)
    workbook = workbook['Sheet1']
    data = workbook.values
    df = pd.DataFrame(data)
    header = df.iloc[2]
    df = df.iloc[3:, :]
    df = df.drop([0], axis=1)
    df.columns = header[1:]
    df = df.set_index(['Last Name', 'First Name'])[:8]
except FileNotFoundError:
    df = load_data()


file_path = r'C:/Users/JordanLee/OneDrive/Documents/MFinA/' \
            r'FINC 591 - Integrated Financial Analysis & Strategy/' \
            r'NNPS - Capstone/Compensation Package.xlsx'
st.title("Calculate Your Total Compensation")
statement = "Below is a personalized statement prepared specifically for you. This statement shows the " \
            "contributions made by the City of Newport News " \
            "toward your total compensation package. As you " \
            "review this statement, you will see the value of your " \
            "benefits, added to your annual pay, producing your total " \
            "compensation. The calculator is most beneficial for evaluating full time employees.\n\n" \
            "This tool can help you:\n\n" \
            "\n\t• Budget for yourself or your team" \
            "\n\n\t• Understand how city-paid benefits factor into total compensation" \
            "\n\n\t• Determine the total compensation of prospective employees" \
            "\n\nTips:\n\n" \
            "\n\t• Open left sidebar to make adjustments to the modeled employee" \
            "\n\n\t• Hover your mouse over different pie pieces to view the benefit name and value" \
            "\n\n\t• Click on the legend items to adjust the amount of benefits on the charts" \
            "\n\n\t• See the full breakdown by clicking the dropdown bar below the graph" \
            "\n\n\t• See the additional benefits by clicking the dropdown bar below the full breakdown\n\n" \

st.write(statement, unsafe_allow_html=False)

st.sidebar.subheader("""**Total Compensation**""")
user_name = st.sidebar.text_input("Name", "George Jetson")
user_jobtitle = st.sidebar.selectbox("Location/Department", ("Treasurer", 'Fire', 'Police',
                                                             'Finance', 'Human Resources',
                                                             'Engineering', 'Libraries', 'Information Technology'))
user_jobtype = st.sidebar.radio("Job Type", ["Full Time", "Part Time"])
if user_jobtype == "Full Time":
    user_salary = st.sidebar.number_input("Annual Base Pay:", value=80857.45, step=500.00)
elif user_jobtype == "Part Time":
    user_salary = st.sidebar.number_input("Hourly Rate:", value=15.66, step=0.50)

user_health_coverage = st.sidebar.selectbox("Health Coverage", (
    "Employee (Health)", "Employee + 1 Child (Health)", "Employee + Spouse (Health)", "Family (Health)"))
user_health_plan = st.sidebar.selectbox("Health Plan", ('Optima Health POS + FSA', 'Optima Health POS', 'None',
                                                        'Optima Equity HDHP', 'Optima Equity HDHP + FSA',
                                                        'Optima Equity HDHP + HSA'))

user_dental_coverage = st.sidebar.selectbox("Dental Coverage", (
    "Employee (Dental)", "Employee + 1 Child (Dental)", "Employee + Spouse (Dental)", "Family (Dental)"))
user_dental_plan = st.sidebar.radio('Dental Plan', ['None', 'Delta Dental'])

user_vision_coverage = st.sidebar.selectbox("Vision Coverage", (
    "Employee (Vision)", "Employee + 1 Child (Vision)", "Employee + Spouse (Vision)", "Family (Vision)"))
user_vision_plan = st.sidebar.radio("Vision Plan", ['None', 'Vision Service Plan', 'Vision INS City'])

button_clicked = st.sidebar.button("GO")


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
    name = user_name
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
    fig.suptitle('{:s} earns ${:,.2f} yearly.\n\n'
                 '{:s} earns ${:,.2f} monthly.\n\n'
                 '{:s} earns ${:,.2f} weekly.'.format(name, value, name, monthly_value, name,
                                                      weekly_pay),
                 x=0.5, y=0.5, fontweight='bold', fontsize=30)

    st.pyplot(fig)
    pass


def employee():
    global fig_df, new_df
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
    explode = [0.00, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    name = user_name
    first_name = ''
    last_name = ''
    job_title = user_jobtitle.upper()
    job_type = user_jobtype
    salary = user_salary
    health_coverage = user_health_coverage
    dental_coverage = user_dental_coverage
    vision_coverage = user_vision_coverage
    health_plan = user_health_plan
    den_plan = user_dental_plan
    vis_plan = user_vision_plan
    ret_plan = ''
    lt_dis_plan = 'Long Term Dis.'
    ret_health_plan = 'RHS'
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

    if health_coverage == 'Employee (Health)':
        ymca_cost = 49.00
        ymca_nnva_cost = 30.00
        ymca_benefit = ymca_cost - ymca_nnva_cost
        one_cost = 39.99
        one_nnva_cost = 25.00
        one_benefit = one_cost - one_nnva_cost
        riv_cost = 50.00
        riv_nnva_cost = 28.00
        riv_benefit = riv_cost - riv_nnva_cost

    if health_coverage == 'Employee + 1 Child (Health)':
        ymca_cost = 64.00
        ymca_nnva_cost = 53.00
        ymca_benefit = ymca_cost - ymca_nnva_cost
        one_cost = 79.98
        one_nnva_cost = 50.00
        one_benefit = one_cost - one_nnva_cost
        riv_cost = 75.00
        riv_nnva_cost = 51.00
        riv_benefit = riv_cost - riv_nnva_cost

    if health_coverage == 'Family (Health)':
        ymca_cost = 79.00
        ymca_nnva_cost = 58.00
        ymca_benefit = ymca_cost - ymca_nnva_cost
        one_cost = 159.96
        one_nnva_cost = 89.00
        one_benefit = one_cost - one_nnva_cost
        riv_cost = 100.00
        riv_nnva_cost = 79.00
        riv_benefit = riv_cost - riv_nnva_cost

    if health_coverage == 'Employee + Spouse (Health)':
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
        if health_coverage == 'Employee (Health)':
            monthly_value += 546.35
            value += 546.35 * 12
            monthly_info_dict[health_plan] = 546.35
            info_dict[health_plan] = 546.35 * 12
        elif health_coverage == 'Employee + 1 Child (Health)':
            monthly_value += 861.69
            value += 861.69 * 12
            monthly_info_dict[health_plan] = 861.69
            info_dict[health_plan] = 861.69 * 12
        elif health_coverage == 'Family (Health)':
            monthly_value += 1493.78
            value += 1493.78 * 12
            monthly_info_dict[health_plan] = 1493.78
            info_dict[health_plan] = 1493.78 * 12
        elif health_coverage == 'Employee + Spouse (Health)':
            monthly_value += 1114.82
            value += 1114.82 * 12
            monthly_info_dict[health_plan] = 1114.82
            info_dict[health_plan] = 1114.82 * 12

    if health_plan == 'Optima Equity HDHP':
        if health_coverage == 'Employee (Health)':
            monthly_value += 527.54
            value += 527.54 * 12
            monthly_info_dict[health_plan] = 527.54
            info_dict[health_plan] = 527.54 * 12
        elif health_coverage == 'Employee + 1 Child (Health)':
            monthly_value += 836.47
            value += 836.47 * 12
            monthly_info_dict[health_plan] = 836.47
            info_dict[health_plan] = 836.47 * 12
        elif health_coverage == 'Family (Health)':
            monthly_value += 1417.11
            value += 1417.11 * 12
            monthly_info_dict[health_plan] = 1417.11
            info_dict[health_plan] = 1417.11 * 12
        elif health_coverage == 'Employee + Spouse (Health)':
            monthly_value += 1076.19
            value += 1076.19 * 12
            monthly_info_dict[health_plan] = 1076.19
            info_dict[health_plan] = 1076.19 * 12

    if health_plan == 'Optima Health POS + FSA':
        if health_coverage == 'Employee (Health)':
            monthly_value += 479.43
            monthly_value += (2750 * .22) / 13  # Tax Benefit
            value += 479.43 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 479.43 + ((2750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (479.43 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

        elif health_coverage == 'Employee + 1 Child (Health)':
            monthly_value += 861.69
            monthly_value += (7750 * .22) / 13  # Tax Benefit
            value += 861.69 * 12
            value += (7750 * .22)
            monthly_info_dict[health_plan] = 861.69 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)
            info_dict[health_plan] = ((861.69 * 12) + (7750 * .22))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif health_coverage == 'Family (Health)':
            monthly_value += 1493.78
            monthly_value += (7750 * .22) / 13  # Tax Benefit
            value += 1493.78 * 12
            value += (7750 * .22)
            monthly_info_dict[health_plan] = 1493.78 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22) / 13
            info_dict[health_plan] = ((7750 * .22) + (1493.78 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif health_coverage == 'Employee + Spouse (Health)':
            monthly_value += 1114.82
            monthly_value += (2750 * .22) / 13
            value += 1114.82 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 1114.82 + 62.50
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (1114.82 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

    if health_plan == 'Optima Equity HDHP + FSA':
        if health_coverage == 'Employee (Health)':
            monthly_value += 527.54
            monthly_value += (2750 * .22) / 13
            value += 527.54 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 527.54 + ((2750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (527.54 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

        elif health_coverage == 'Employee + 1 Child (Health)':
            monthly_value += 836.47
            monthly_value += (7750 * .22) / 13
            value += 836.47 * 12
            value += (7750 * .22) / 13
            monthly_info_dict[health_plan] = 836.47 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22) / 13
            info_dict[health_plan] = ((836.47 * 12) + (7750 * .22))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif health_coverage == 'Family (Health)':
            monthly_value += 1417.11
            monthly_value += (7750 * .22) / 13  # Tax Benefit
            value += 1417.11 * 12
            value += (7750 * .22)
            monthly_info_dict[health_plan] = 1417.11 + ((7750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (7750 * .22) / 13
            info_dict[health_plan] = ((7750 * .22) + (1417.11 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (7750 * .22)

        elif health_coverage == 'Employee + Spouse (Health)':
            monthly_value += 1076.19
            monthly_value += (2750 * .22) / 13
            value += 1076.19 * 12
            value += (2750 * .22)
            monthly_info_dict[health_plan] = 1076.19 + ((2750 * .22) / 13)
            monthly_info_dict['Flexible Spending Account (FSA)'] = (2750 * .22) / 13
            info_dict[health_plan] = ((2750 * .22) + (1076.19 * 12))
            info_dict['Flexible Spending Account (FSA)'] = (2750 * .22)

    if health_plan == 'Optima Equity HDHP + HSA':
        if health_coverage == 'Employee (Health)':
            monthly_value += 527.54
            monthly_value += 62.50
            value += (527.54 + 62.50) * 12
            monthly_info_dict[health_plan] = 527.54 + 62.50
            monthly_info_dict['Health Savings Account (HSA)'] = 62.50
            info_dict[health_plan] = (62.50 + 527.54) * 12
            info_dict['Health Savings Account (HSA)'] = 62.50 * 12

        elif health_coverage == 'Employee + 1 Child (Health)':
            monthly_value += 836.47
            monthly_value += 125
            value += (836.47 + 125) * 12
            monthly_info_dict[health_plan] = 836.47 + 125
            monthly_info_dict['Health Savings Account (HSA)'] = 125
            info_dict[health_plan] = (836.47 + 125) * 12
            info_dict['Health Savings Account (HSA)'] = 125 * 12

        elif health_coverage == 'Family (Health)':
            monthly_value += 1417.11 + 125
            value += (1417.11 + 125) * 12
            monthly_info_dict[health_plan] = 1417.11 + 125
            monthly_info_dict['Health Savings Account (HSA)'] = 125
            info_dict[health_plan] = (1417.11 + 125) * 12
            info_dict['Health Savings Account (HSA)'] = 125 * 12

        elif health_coverage == 'Employee + Spouse (Health)':
            monthly_value += 1076.19 + 125
            value += (1076.19 + 125) * 12
            monthly_info_dict[health_plan] = 1076.19 + 125
            monthly_info_dict['Health Savings Account (HSA)'] = 125
            info_dict[health_plan] = (1076.19 + 125) * 12
            info_dict['Health Savings Account (HSA)'] = 125 * 12

    if den_plan == 'Delta Dental':
        if dental_coverage == 'Employee (Dental)':
            monthly_value += 21.42
            value += 21.42 * 12
            monthly_info_dict[den_plan] = 21.42
            info_dict[den_plan] = 21.42 * 12
        elif dental_coverage == 'Employee + 1 Child (Dental)':
            monthly_value += 38.92
            value += 38.92 * 12
            monthly_info_dict[den_plan] = 38.92
            info_dict[den_plan] = 38.92 * 12
        elif dental_coverage == 'Family (Dental)' or dental_coverage == 'Employee + Spouse (Dental)':
            monthly_value += 66.91
            value += 66.91 * 12
            monthly_info_dict[den_plan] = 66.91
            info_dict[den_plan] = 66.91 * 12

    if vis_plan == 'Vision Service Plan':
        if vision_coverage == 'Employee (Vision)':
            monthly_value += 1.80
            value += 1.80 * 12
            monthly_info_dict[vis_plan] = 1.80
            info_dict[vis_plan] = 1.80 * 12
        elif vision_coverage == 'Employee + 1 Child (Vision)':
            monthly_value += 2.80
            value += 2.80 * 12
            monthly_info_dict[vis_plan] = 2.80
            info_dict[vis_plan] = 2.80 * 12
        elif vision_coverage == 'Family (Vision)':
            monthly_value += 2.80
            value += 2.80 * 12
            monthly_info_dict[vis_plan] = 2.80
            info_dict[vis_plan] = 2.80 * 12
        elif vision_coverage == 'Employee + Spouse (Vision)':
            monthly_value += 2.80
            value += 2.80 * 12
            monthly_info_dict[vis_plan] = 2.80
            info_dict[vis_plan] = 2.80 * 12

    if vis_plan == 'Vision INS City':
        if vision_coverage == 'Employee (Vision)':
            monthly_value += 0.80
            value += 0.80 * 12
            monthly_info_dict[vis_plan] = 0.80
            info_dict[vis_plan] = 0.80 * 12
        else:
            monthly_value += 0
            value += 0 * 12
            monthly_info_dict[vis_plan] = 0
            info_dict[vis_plan] = 0 * 12
    try:
        for i in range(len(df)):
            # df.iloc[i].name == (first_name, last_name) or
            if df.iloc[i].loc['Location Code Desc'] == job_title:
                ret_plan = df.iloc[i].loc['Retirement Plan']

                if ret_plan == 'NNER  CITY OF NEWPORT NEWS RET':
                    ret_plan = 'NNER - City of Newport News Ret'
                elif ret_plan == 'VRS - VIRGINIA RETIREMENT SYST':
                    ret_plan = 'VRS - Virginia Retirement System'
                elif ret_plan == 'VRSH - VIRGINIA RET SYS HYBRID':
                    ret_plan = 'VRSH - Virginia Retirement System Hybrid'

                user_data = df.iloc[i].loc['DB Retirement City']
                monthly_value += float(user_data)
                value += float(user_data) * 12
                monthly_info_dict[ret_plan] = float(user_data)
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
                monthly_value += round(float(life_data), 2)
                value += round(float(life_data) * 12, 2)
                monthly_info_dict[life_plan] = round(float(life_data), 2)
                info_dict[life_plan] = round(float(life_data) * 12, 2)

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
                    monthly_value += round(float(VLDP_data), 2)
                    value += round(float(VLDP_data) * 12, 2)
                    monthly_info_dict['Disability (Hybrid Only)'] = round(float(VLDP_data), 2)
                    info_dict['Disability (Hybrid Only)'] = round(float(VLDP_data) * 12, 2)
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

    # Initialize Add'tl Benefits Ticket
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
            "\tBenefit Waiting Period: After 90 days\n".format(ymca_benefit, ymca_cost, ymca_nnva_cost,
                                                               one_benefit, one_cost, one_nnva_cost,
                                                               riv_benefit, riv_cost, riv_nnva_cost)

    df_annual = pd.DataFrame.from_dict(data=info_dict, orient='index', columns=['Annual Compensation Package'])
    try:
        fig_df = df_annual.loc[[health_plan, den_plan, vis_plan], :]
        new_df = df_annual.drop(["Annual Salary", health_plan, den_plan, vis_plan])

    except KeyError:
        pass

    voluntary_labels = labels
    mandatory_labels = labels
    if health_plan == "Optima Health POS + FSA" or health_plan == "Optima Equity HDHP + FSA":
        if den_plan != "None" and vis_plan != "None":
            fig_df = df_annual.loc[[health_plan, "Flexible Spending Account (FSA)", den_plan, vis_plan], :]
            new_df = df_annual.drop(
                [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3], df_annual.index[4]])
            voluntary_labels = voluntary_labels[1:5]
            mandatory_labels = mandatory_labels[5:]

        elif den_plan == "None" and vis_plan != "None":
            fig_df = df_annual.loc[[health_plan, "Flexible Spending Account (FSA)", vis_plan], :]
            new_df = df_annual.drop(
                [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
            voluntary_labels = voluntary_labels[1:4]
            mandatory_labels = mandatory_labels[4:]

        elif vis_plan == "None" and den_plan != "None":
            fig_df = df_annual.loc[[health_plan, "Flexible Spending Account (FSA)", den_plan], :]
            new_df = df_annual.drop(
                [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
            voluntary_labels = voluntary_labels[1:4]
            mandatory_labels = mandatory_labels[4:]

        elif den_plan == "None" and vis_plan == "None":
            fig_df = df_annual.loc[[health_plan, "Flexible Spending Account (FSA)"], :]
            new_df = df_annual.drop(
                [df_annual.index[0], df_annual.index[1], df_annual.index[2]])
            voluntary_labels = voluntary_labels[1:3]
            mandatory_labels = mandatory_labels[3:]
            print(fig_df)
            print(voluntary_labels)
            print(mandatory_labels)

    if health_plan == "Optima Equity HDHP + HSA":
        if den_plan != "None" and vis_plan != "None":
            fig_df = df_annual.loc[[health_plan, "Health Savings Account (HSA)", den_plan, vis_plan], :]
            new_df = df_annual.drop(
                [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3], df_annual.index[4]])
            voluntary_labels = voluntary_labels[1:5]
            mandatory_labels = mandatory_labels[5:]

        elif den_plan == "None" and vis_plan != "None":
            fig_df = df_annual.loc[[health_plan, "Health Savings Account (HSA)", vis_plan], :]
            new_df = df_annual.drop(
                [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
            voluntary_labels = voluntary_labels[1:4]
            mandatory_labels = mandatory_labels[4:]

        elif vis_plan == "None" and den_plan != "None":
            fig_df = df_annual.loc[[health_plan, "Health Savings Account (HSA)", den_plan], :]
            new_df = df_annual.drop(
                [df_annual.index[0], df_annual.index[1], df_annual.index[2], df_annual.index[3]])
            voluntary_labels = voluntary_labels[1:4]
            mandatory_labels = mandatory_labels[4:]

        elif den_plan == "None" and vis_plan == "None":
            fig_df = df_annual.loc[[health_plan, "Health Savings Account (HSA)"], :]
            new_df = df_annual.drop(
                [df_annual.index[0], df_annual.index[1], df_annual.index[2]])
            voluntary_labels = voluntary_labels[1:3]
            mandatory_labels = mandatory_labels[3:]

    if den_plan == "None" and vis_plan == "None" and health_plan != "Optima Health POS + FSA" and health_plan != "Optima Equity HDHP + FSA" and health_plan != 'Optima Equity HDHP + HSA':
        fig_df = df_annual.loc[[health_plan], :]
        new_df = df_annual.drop([df_annual.index[0], df_annual.index[1]])
        voluntary_labels = voluntary_labels[1:2]
        mandatory_labels = mandatory_labels[2:]

    if health_plan == "None" and den_plan != "None" and vis_plan == "None":
        fig_df = df_annual.loc[[den_plan], :]
        new_df = df_annual.drop([df_annual.index[0], df_annual.index[1]])
        voluntary_labels = voluntary_labels[1:2]
        mandatory_labels = mandatory_labels[2:]

    if health_plan == "None" and den_plan == "None" and vis_plan != "None":
        fig_df = df_annual.loc[[vis_plan], :]
        new_df = df_annual.drop(["Annual Salary", vis_plan])
        voluntary_labels = voluntary_labels[1:2]
        mandatory_labels = mandatory_labels[2:]

    if health_plan == "None" and den_plan == "None" and vis_plan == "None":
        fig_df = df_annual
        new_df = df_annual.drop([df_annual.index[0]])
        voluntary_labels = voluntary_labels
        mandatory_labels = mandatory_labels[1:]

    print(fig_df)
    print(new_df)

    # fig_df = fig_df.T

    plots = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "pie"}, {"rowspan": 2, "type": "pie"}],
               [{"type": "pie"}, None]],

        subplot_titles=("Voluntary Benefits", "Full Compensation Package", "Mandatory Benefits"),
        horizontal_spacing=0.25
    )
    plots.add_trace(
        go.Pie(values=df_annual['Annual Compensation Package'], labels=labels,
               pull=[i for i in explode[:len(labels)]],
               hovertemplate='%{label}: %{value:$,.2f}<extra></extra> \n\t%{percent}'),
        row=1, col=2

    )

    plots.add_trace(
        go.Pie(values=fig_df['Annual Compensation Package'], labels=voluntary_labels,
               hoverinfo='label+value+percent'),
        row=1, col=1

    )

    plots.add_trace(
        go.Pie(values=new_df['Annual Compensation Package'], labels=mandatory_labels,
               hoverinfo='label+value+percent'),
        row=2, col=1

    )
    plots.update_layout(height=600, width=1500, legend_title="Legend", legend_font_size=14,
                        legend_title_font_size=19, legend=dict(orientation="v", x=1.15))

    plots.update_annotations(y=1.085, selector={'text': 'Voluntary Benefits'})
    plots.update_annotations(y=0.41, selector={'text': 'Mandatory Benefits'})
    plots.update_annotations(y=1.002, selector={'text': 'Full Compensation Package'})

    # fig2 = px.bar(new_df, x=new_df.index, y=columns_list, barmode='stack', labels=labels)

    # fig2.update_traces(textfont_size=12, textposition="outside")
    # fig2.update_xaxes(title='Compensation')
    # fig2.update_yaxes(title='Total Value ($)')
    # fig2.update_layout(legend_title='Benefits')

    df_annual.loc['Total'] = value

    df_monthly = pd.DataFrame.from_dict(data=monthly_info_dict, orient='index',
                                        columns=['Monthly Compensation Package'])
    df_monthly.loc['Total'] = monthly_value
    main_df = pd.concat([df_annual, df_monthly], axis=1)
    main_df = main_df.applymap(lambda x: "${:,.2f}".format(float(x)), na_action='ignore')
    main_df.fillna("", inplace=True)

    return df_annual, df_monthly, main_df, text1, plots, name


try:
    user = employee()
    n = user[5]
    final_df = user[0]
    monthly_df = user[1]
    total_df = user[2]
    figure = user[4]
    # figure2 = user[6]

    title = "\t\t{:s} Compensation Package".format(n)
    st.subheader(title)
    st.plotly_chart(figure, use_container_width=True, sharing='streamlit')
    # st.plotly_chart(figure2, use_container_width=True, sharing='streamlit')
    st.caption("This graph will automatically be created and changed as data is entered. "
             "This statement is designed to show how much your service is valued by us.")

    with st.expander("See Full Breakdown"):
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.write("Base Pay")
            st.write("${:,.2f}".format(final_df['Annual Compensation Package'].iloc[0]))
        with col2:
            st.subheader(" + ")
        with col3:
            st.write("City Paid Benefits")
            st.write("${:,.2f}".format(final_df['Annual Compensation Package'].iloc[1:-1].sum()))
        with col4:
            st.subheader("\t\n\t=")
        with col5:
            st.write("**Total Comp.**")
            st.write("**${:,.2f}**".format(final_df['Annual Compensation Package'].iloc[-1]))


        def df_style(val):
            return "font-weight: bold"

        last_row = pd.IndexSlice[final_df.index[final_df.index == "Total"], :]

        final_df = final_df.applymap(lambda x: "${:,.2f}".format(float(x)),
                                     na_action='ignore').style.applymap(df_style, subset=last_row)
        st.dataframe(final_df)
except TypeError:
    pass

finally:
    with st.expander("See Additional Benefits"):
        benefits_title = '**Additional Benefits**'
        st.title(benefits_title)

        st.subheader("\n**RETIREMENT HEALTH SAVINGS (RHS) PLAN**\n"
                     "The Retirement Health Savings (RHS) Plan is a city-funded tax-advantaged spending account "
                     "that provides regular active full-time employees of the City hired after February 28, 2010, "
                     "the ability to accumulate assets on a tax-free basis, for reimbursements of qualified medical "
                     "expenses during retirement.  The city contributes 3% of earnings on behalf of each eligible "
                     "employee.  \n\n*Definition of Earnings: Average City full-time salary annualized and calculated"
                     " at the beginning of each Fiscal Year.  For more information on the Retirement Health Savings "
                     "(RHS) Plan, please visit https://www.nnva.gov/2673/Retirement-Health-Savings-Plan-RHS. ")

        text = "\n**PAID HOLIDAYS**\n" \
               "Regular, full-time City employees are eligible for paid holidays, provided\nthey are in an active " \
               "pay status the working day prior to the holiday.\n\n" \
               "\t• New Year’s Day (January 1)\n" \
               "\t• Dr. Martin Luther King’s Birthday (Third Monday in January)\n" \
               "\t• President’s Day & George Washington’s Birthday (Third Monday in February)\n" \
               "\t• Memorial Day (Last Monday in May)\n" \
               "\t• Juneteenth (June 19)\n" \
               "\t• Independence Day (July 4)\n" \
               "\t• Labor Day (First Monday in September)\n" \
               "\t• Veterans Day (November 11)\n" \
               "\t• Thanksgiving Day (Fourth Thursday in November)\n" \
               "\t• The Friday following Thanksgiving Day\n" \
               "\t• Christmas Eve (December 24) – Observed as four hours only, and provided\n" \
               "\tthat December 24 falls during the normal Monday through Friday work week\n" \
               "\t• Christmas Day (December 25)\n\n"
        st.subheader(text)

        st.subheader(
            "**PAID PERSONAL LEAVE (PPL)**\nPaid personal leave covers vacation, absences for personal business and"
            "\nsome medical leave. Regular, full-time employees and 24-hour "
            "fire employees\nearn PPL according to the following bi-weekly accrual schedule:")
        st.table(PPL_df.set_index('YEARS OF SERVICE'))
        st.subheader("\n**PAID MEDICAL LEAVE (PML)**\n"
                     "Paid medical leave can be used for certain personal "
                     "and family\nmedical-related absences. Regular, full-time employees accrue 2.75 hours\n"
                     "bi-weekly and 24-hour fire employees accrue 7.5 hours bi-weekly.\n\n")

        st.subheader("\n**TUITION REIMBURSEMENT**\n"
                     "Tuition reimbursement is intended to encourage employee development and improve work-related "
                     "knowledge, skills, and abilities through the pursuit of educational programs leading to a college "
                     "degree or industry-related certification or licensure that enhances City operations. Tuition "
                     "reimbursement is a benefit for active full-time employees. ")

        st.subheader("\n**TICKETSATWORK.COM**\n"
                     "Employees gain access to employee discounts and special "
                     "offers not available to the general public. "
                     "Save on Travel, Theme Parks & Attractions, Movie Tickets, Shopping Deals, Hotels, Shows & Events,"
                     " plus so much more. ")

        st.subheader("\n**FITNESS CENTER DISCOUNTS**\n"
                     "As part of the City’s Wellness Initiate, the City of Newport News offers all full time "
                     "employees access to fitness center memberships at a discounted rate. ")

        st.subheader("\n**RENEWAL EMPLOYEE WELLNESS PROGRAM**\n"
                     "We care about our employees! The City of Newport News offers an amazing Wellness Program "
                     "entitled Renew. The goal of the Renew Wellness Program is to enrich the significance of life for City "
                     "of Newport News employees by promoting and implementing remarkable holistic wellness "
                     "programming. We strive to deliver proactive activities that promote a well-rounded, more engaged, "
                     "and healthier lifestyle for our employee workforce by exploring the Eight {8} Dimensions of "
                     "Wellness: Emotional Wellness, Environmental Wellness, Financial Wellness, Intellectual Wellness, "
                     "Occupational Wellness, Physical Wellness, Social Wellness and Spiritual Wellness.")

        st.subheader("\n**EMPLOYEE ASSISTANCE PROGRAM (EAP)**\n"
                     "All City of Newport News employees and their immediate family members are eligible for a city-paid "
                     "benefit called Employee Assistance. An Employee Assistance Program or EAP is a special benefit to "
                     "help you and your family members with personal, marital, family and job-related problems. The goal"
                     " of the program is to assist employees in achieving and maintaining happy, healthy and fully"
                     " productive lives both on and off the job. ")

        st.subheader("\n**iPROPEL**\n"
                     "iPROPEL is the City’s online employee recognition platform that is available to all full-time"
                     " and parttime employees. It is a great way to connect with other City employees and to "
                     "recognize each other for all of the things that we have been doing to keep the "
                     "City running smoothly, protecting our citizens, putting ourselves on the front line"
                     " during this crisis, and continuing to prove that the City ofNewport News has the best "
                     "employees anywhere! iPROPEL is an acronym that identifies the values exemplified by our "
                     "employees: Integrity, Partnerships, Respect, Opportunities, Performance, Ethics, "
                     "and Leadership and the platform lets us all join together to celebrate and acknowledge our "
                     "achievements! When supervisors or Department Directors award recognition badges in the iPROPEL "
                     "system, employees will be eligible to receive system points that can be used to select the items "
                     "available in the online catalog.")

        st.subheader("\n**VOLUNTARY WHOLE LIFE INSURANCE**\n"
                     "Full-time city employees have the option of enrolling in Whole Life Insurance, "
                     "with Optional Riders, "
                     "regardless of their retirement plan. ")

        st.subheader("\n**VOLUNTARY TAX ADVANTAGE 457 DEFERRED COMPENSATION AND ROTH IRA PLAN OPTIONS**\n"
                     "Our third party vendor is committed to helping employees build retirement security through "
                     "retirement programs, investment products, and educational tools and services. ")


if button_clicked == 'GO':
    employee()

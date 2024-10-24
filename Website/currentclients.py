import streamlit as st
import pandas as pd
import win32com.client
import os
from openpyxl import load_workbook
from openpyxl.utils.exceptions import InvalidFileException
from datetime import datetime, timedelta

# Set up dictionary for valid clients (Client ID: Password)
valid_clients = {
    "EI": "EI2024!",
    "AL": "A&L2024!",
    "DLI": "DLI2024!",
}
valid_client_names = {
    "EI": "Est Institute",
    "AL": "A&L Home Builders",
    "DLI": "Legacy Tattoo",
}

# Set a maximum number of attempts
max_attempts = 5


# Track the number of attempts
#if 'attempts' not in st.session_state:
    #st.session_state['attempts'] = 0
#if 'authenticated' not in st.session_state:
    #st.session_state.authenticated = False

# Sidebar form for client authentication
st.sidebar.title("Client Authentication")
client_id = st.sidebar.text_input("Client ID", "DLI")
client_password = st.sidebar.text_input("Client Password", "DLI2024!", type="password")

# If attempts exceed max_attempts, lock access
#if st.session_state['attempts'] >= max_attempts:
    #st.sidebar.error("Maximum login attempts exceeded.")
    #st.stop()

# Function to check authentication
def authenticate(client_id, client_password):
    if client_id not in valid_clients:
        return "Client ID not found"
    elif valid_clients[client_id] != client_password:
        return "Incorrect password"
    else:
        return "Authenticated"

# Handle authentication attempts
if st.sidebar.button("Submit"):
    #st.session_state.attempts += 1  # Increment attempts
    auth_status = authenticate(client_id, client_password)

    if auth_status == "Authenticated":
        st.session_state.authenticated = True
    else:
        st.sidebar.error(auth_status)

# If authenticated, proceed to search for the file
if 'authenticated' in st.session_state and st.session_state.authenticated:
    st.sidebar.success("Authentication successful!")
    
    # Search for the financial forecast model using the Client ID and password
    folder_path = r"C:\Users\jorda\OneDrive\Documents\GitHub\streamlit\Website"  # Replace with actual folder path
    file_name = f"{client_id}_FFM.xlsx"
    file_path = os.path.join(folder_path, file_name)
    
    if os.path.exists(file_path):
        try:
            # Attempt to load the workbook using the password
            excel = win32com.client.Dispatch("Excel.Application")
            excel.Visible = False  # Set to True if you want to see Excel
            workbook = excel.Workbooks.Open(file_path, Password=client_password)

            #new_file_path = os.path.join(folder_path, f'{client_id}_FFM_no_passowrd.xlsx')
            new_file_path = folder_path + f'{client_id}_FFM_no_password.xlsx'
            # Save a new copy without password protection
            workbook.SaveAs(new_file_path, Password='', FileFormat=51)  # 51 for .xlsx
            print(f"Password removed successfully. New file saved as: {new_file_path}")
            '''if os.path.exists(new_file_path)==False:

                # Save a new copy without password protection
                workbook.SaveAs(new_file_path, Password='', FileFormat=51)  # 51 for .xlsx
                print(f"Password removed successfully. New file saved as: {new_file_path}")
            else:
                # Save a new copy without password protection
                workbook.Save(new_file_path)  # 51 for .xlsx
                print(f"Password removed successfully. New file saved as: {new_file_path}")'''
            
            workbook.Close(SaveChanges=True)
            excel.Quit()

            #excel = win32com.client.Dispatch("Excel.Application")
            #excel.Visible = False
            #new_workbook = excel.Workbooks.Open(new_file_path)
            #new_workbook.Close(SaveChanges=True)
            new_workbook = load_workbook(filename=new_file_path, data_only=True, read_only=True, keep_vba=True)
            
            st.success(f"Successfully opened {file_name}")
            
            # Display the available sheets in the Excel file
            sheet_names = ['Monthly Detail', 'Annual Summary', '2024 Overview']
            st.write(f"Available sheets: {sheet_names}")
            
            # Let the user select a sheet to view
            selected_sheet = st.selectbox("Select a sheet to view:", sheet_names)
            
            # Load the selected sheet into a DataFrame
            active_sheet = new_workbook[selected_sheet]
            data = active_sheet.values
            sheet_data = pd.DataFrame(data)
            # sheet_data = pd.read_excel(new_file_path, sheet_name=selected_sheet)
            #active_workbook.Close(SaveChanges=True)
            
            # Display the sheet data
            st.dataframe(sheet_data)
        except InvalidFileException:
            st.error("Unable to open the file. The file may be corrupt or inaccessible.")
        except KeyError:
            st.error("Incorrect password for this file.")
    else:
        st.error(f"No financial forecast model found for Client ID '{client_id}'.")

else:
    st.write("Please enter your credentials to proceed.")

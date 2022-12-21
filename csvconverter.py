import pandas as pd

to_path = r"C:\Users\data\Sampledata.csv"
df = pd.read_excel(r"C:\Users\data\Sampledata.xlsx", index_col=[1, 2], header=[2], sheet_name=None)
print(df)
df = pd.DataFrame.from_dict(df)
df.to_csv(to_path)

'''bookie = xlsxwriter.Workbook(f)

        workbook = writer.book
        accounting_format = workbook.add_format({'num_format': '$#,##0.00'})
        percentage_format = workbook.add_format({'num_format': '0%'})
        sheet = bookie.worksheets()

        sheet.set_column(6, 12, None, cell_format=accounting_format)
        for sheet in workbook.worksheets():
            sheet('F8:L{}'.format(periods), cell_format=accounting_format)
            sheet.write("C3", cell_format=accounting_format)
            sheet.write("C6", cell_format=accounting_format)'''

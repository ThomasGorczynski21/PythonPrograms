import pandas as pd
prinnt(pandas.path)
pandas.path.apend('/Users/tom_8/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/site-packages')

# Load Excel data into a Pandas DataFrame
excel_data = pd.read_excel('input_file.xlsx')

# Convert the DataFrame to a JSON string
json_data = excel_data.to_json(orient='records')

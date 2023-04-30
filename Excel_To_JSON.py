##Targets the library location 
import sys
sys.path.append('C:/Users/tom_8/source/PythonPrograms/lib/site-packages')

##need to add this line to find all libraries
sys.path.append('/Users/tom_8/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0/LocalCache/local-packages/Python311/site-packages')

import pandas as pd

# Load Excel data into a Pandas DataFrame
excel_data = pd.read_excel('input_file.xlsx')

# Convert the DataFrame to a JSON string
json_data = excel_data.to_json(orient='records')

# Write the JSON string to a file
with open('output_file.json', 'w') as json_file:
    json_file.write(json_data)

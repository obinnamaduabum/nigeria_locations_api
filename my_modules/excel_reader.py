import pandas as pd

class ExcelReader:

    
    def fetch_excel_reader(self):
        data = pd.read_excel('./assets/excel/nigeria-state-and-localities.xlsx')
        # area_name_list = data['Area Name'].tolist()
        # locality_list = data['Locality Name'].tolist()
        # area_name_set = set(area_name_list)
        # locality_set = set(locality_list)
        # print(data)
        return data
    